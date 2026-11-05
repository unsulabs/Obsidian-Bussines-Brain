"""Synthetic render/link/privacy acceptance; no production vault or corpus IO."""
from copy import deepcopy
import json
from pathlib import Path
import re
import sys
import unittest
from unittest.mock import patch
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import test_transcripciones_pipeline
from transcripciones_pipeline import consolidate_analysis
from transcripciones_modelo import ModelError, json_bytes, sha256_bytes, load_json
from transcripciones_fichas import render_source, propose_navigation, batch_subjects
from transcripciones_representaciones import importar_representacion


class FichaTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_transcripciones_pipeline.PipelineTests()
        self.fixture.setUp()
        self.bank = self.fixture.bank
        self.submission = self.fixture.submission()
        self.submission['global_reconciliation']['open_conflicts'] = ['Conflicto sintético aún abierto']
        consolidate_analysis(self.bank, self.submission, **self.fixture.scope, commit=True)
        self.profile = dict(bank=self.bank, **self.fixture.scope, vault_snapshot={},
                            source_sensitivity={self.fixture.tr: 'interno'})

    def tearDown(self):
        self.fixture.tearDown()

    def render(self):
        return render_source(self.fixture.tr, 'RUN-fixture', self.profile)

    def test_every_subject_claim_reason_exception_conflict_and_uncertainty(self):
        before = self.fixture.snapshot_bytes()
        result = self.render()
        text = result['candidates'][0]['content']
        for subject in self.submission['subject_matrix']:
            self.assertIn(subject['description'], text)
            for value in subject['reasons'] + subject['exceptions']:
                self.assertIn(value, text)
        for claim in self.submission['claims']:
            self.assertIn(claim['content'], text)
            self.assertIn(claim['attribution_state'], text)
        self.assertIn('Conflicto sintético aún abierto', text)
        self.assertIn(self.submission['relations'][0]['rationale'], text)
        self.assertIn('pending_independent_review', text)
        self.assertFalse(result['evidence']['ratified'])
        self.assertEqual(before, self.fixture.snapshot_bytes())

    def test_raw_full_and_all_wikilinks_resolve_with_backlinks(self):
        result = self.render()
        files = {c['path']: c['content'] for c in result['candidates']}
        full = next(c['content'] for c in result['candidates'] if c['kind'] == 'transcript_view')
        self.assertIn(self.fixture.authored['data'].decode(), full)
        self.assertIn('file://', full)
        for text in files.values():
            for target in re.findall(r'\[\[([^]|]+)(?:\|[^]]*)?\]\]', text):
                path, _, anchor = target.partition('#')
                self.assertIn(path, files)
                if anchor.startswith('^'):
                    self.assertIn('\n' + anchor + '\n', files[path])
                elif anchor:
                    self.assertIn('## ' + anchor, files[path])
        self.assertIn('Volver a ficha', full)

    def test_duplicate_tr_keeps_existing_identity_and_name(self):
        rendered = self.render()['candidates']
        first = rendered[0]
        renamed = '50_Fuentes/Conversación conservada.md'
        content = first['content'].replace(first['id'], 'F-existing')
        self.profile['vault_snapshot'] = {c['path']: c['content'] for c in rendered[1:]}
        self.profile['vault_snapshot'][renamed] = content
        note = self.render()['candidates'][0]
        self.assertEqual(note['id'], 'F-existing')
        self.assertEqual(note['path'], renamed)
        self.assertEqual(note['expected_sha256'], sha256_bytes(content.encode()))
        self.profile['vault_snapshot']['50_Fuentes/Duplicada.md'] = content
        with self.assertRaisesRegex(ModelError, 'DUPLICATE_TR_NOTE'):
            self.render()

    def test_readable_title_filename_and_collision_keep_links_and_identity(self):
        from transcripciones_custodia import load_catalog
        rows = load_catalog(self.bank)
        rows[0]['title_reported'] = 'Estrategia de consultoría y plataforma agente'
        with patch('transcripciones_fichas.load_catalog', return_value=rows):
            first = self.render()
            source = first['candidates'][0]
            self.assertEqual(source['path'], '50_Fuentes/Estrategia de consultoría y plataforma agente.md')
            self.assertNotIn(self.fixture.tr, source['path'])
            navigation = propose_navigation(first['candidates'], {})
            corpus = next(c['content'] for c in navigation if c['kind'] == 'navigation')
            self.assertIn('|' + Path(source['path']).stem + ']]', corpus)
            self.assertNotIn('|' + source['id'] + ']]', corpus)
            legacy_corpus = corpus.replace('|' + Path(source['path']).stem + ']]', '|' + source['id'] + ']]')
            preserved = propose_navigation(first['candidates'], {'00_Mapas/Corpus de transcripciones.md': legacy_corpus})
            self.assertFalse(any(c['kind'] == 'navigation' for c in preserved))
            self.profile['vault_snapshot'] = {source['path']: '---\nid: UNRELATED\ntipo: manual\n---\n# Otro\n'}
            collision = self.render()
            second = collision['candidates'][0]
            self.assertEqual(second['id'], source['id'])
            self.assertEqual(second['path'], source['path'][:-3] + ' — ' + sha256_bytes(self.fixture.tr.encode())[:8] + '.md')
            for c in collision['candidates']:
                if c['kind'] == 'transcript_view':
                    self.assertIn('[[' + second['path'] + '|Volver a ficha]]', c['content'])
            self.profile['vault_snapshot'][second['path']] = second['content']
            self.profile['vault_snapshot'].update({c['path']: c['content'] for c in collision['candidates'][1:]})
            self.assertEqual(self.render()['candidates'][0]['path'], second['path'])

    def test_original_changed_and_permission_denied(self):
        self.fixture.grant('local_analysis', 'revoke')
        with self.assertRaises(ModelError):
            self.render()
        self.fixture.grant('local_analysis')
        blob = next((self.bank / 'originales').glob('*.bin'))
        blob.write_bytes(b'changed synthetic original')
        with self.assertRaisesRegex(ModelError, 'SOURCE_CHANGED|HASH_MISMATCH'):
            self.render()

    def test_other_audience_denied_and_unknown_sensitivity_never_downgraded(self):
        self.profile['audience'] = 'outside'
        with self.assertRaises(ModelError):
            self.render()
        self.profile['audience'] = 'internal'
        self.profile.pop('source_sensitivity')
        result = self.render()
        self.assertTrue(all(c['local_private_only'] for c in result['candidates']))
        self.assertIn('sensibilidad: restringido', result['candidates'][0]['content'])
        note = result['candidates'][0]
        self.profile['vault_snapshot'] = {c['path']: c['content'] for c in result['candidates']}
        self.profile['source_sensitivity'] = {self.fixture.tr: 'interno'}
        self.assertTrue(self.render()['candidates'][0]['local_private_only'])

    def test_semantic_review_exact_external_binding_no_approval(self):
        submission = self.bank.parent / 'sealed-submission.json'
        submission.write_text(json.dumps(self.submission), encoding='utf-8')
        review = self.bank.parent / 'review.md'
        review.write_text('Synthetic independent review: all five subjects inspected. Not business ratification.')
        self.profile['semantic_review'] = dict(run_id='RUN-fixture', reviewer='Synthetic independent reviewer',
            status='reviewed', submission_path=str(submission), review_path=str(review),
            submission_file_sha256=sha256_bytes(submission.read_bytes()),
            submission_sha256=sha256_bytes(json_bytes(self.submission)), review_sha256=sha256_bytes(review.read_bytes()))
        result = self.render()
        self.assertIn('estado_editorial: en_revision', result['candidates'][0]['content'])
        self.assertFalse(result['evidence']['ratified'])
        self.profile['semantic_review']['submission_sha256'] = '0' * 64
        with self.assertRaisesRegex(ModelError, 'SEMANTIC_REVIEW_UNBOUND'):
            self.render()
        self.profile['semantic_review']['submission_sha256'] = sha256_bytes(json_bytes(self.submission))
        review.write_text('Changed')
        with self.assertRaisesRegex(ModelError, 'SEMANTIC_REVIEW_CHANGED'):
            self.render()

    def test_batch_more_than_thirty_retains_all_and_obeys_bytes(self):
        subjects = []
        for i in range(65):
            subject = deepcopy(self.submission['subject_matrix'][0])
            subject['subject_id'] = f'SUBJECT-{i}'
            subject['description'] = 'X' * 4000
            subjects.append(subject)
        parent = batch_subjects(subjects, parent_id='BATCH-test')
        self.assertEqual(subjects, [s for b in parent['batches'] for s in b['subjects']])
        self.assertGreater(len(parent['batches']), 2)
        for batch in parent['batches']:
            self.assertLessEqual(len(batch['subjects']), 30)
            self.assertLessEqual(len(batch['destination_ids']), 30)
            self.assertLessEqual(len(json_bytes(batch)), 90000)
        self.assertFalse(parent['canonical_units_generated'])

    def test_navigation_preserves_sixteen_bases_and_custom_pages(self):
        snapshot = {f'90_Sistema/Vistas/Original-{i}.base': 'filters: personalizado\n' for i in range(16)}
        snapshot.update({'Inicio.md': '---\nid: HOME\ntipo: inicio\n---\n# Inicio\n\nMi personalización\n',
                         'Como_usar.md': '---\nid: MANUAL\ntipo: manual\n---\n# Cómo usar\nAtajos propios\n'})
        before = deepcopy(snapshot)
        sources = self.render()['candidates']
        navigation = propose_navigation(sources, snapshot)
        self.assertEqual(snapshot, before)
        self.assertFalse(set(c['path'] for c in navigation) & {p for p in before if p.endswith('.base')})
        for candidate in navigation:
            if candidate['path'].endswith('.base'):
                self.assertIn('views', yaml.safe_load(candidate['content']))
            if candidate['kind'] == 'navigation_append':
                self.assertTrue(candidate['content'].startswith(before[candidate['path']]))
        snapshot.update({c['path']: c['content'] for c in navigation})
        self.assertEqual(propose_navigation(sources, snapshot), [])

    def test_auxiliary_headers_verified_and_kept_unresolved(self):
        raw = self.fixture.authored['data']
        header = 'Persona de proveedor sin identidad resuelta 00:00:03'
        headered = header.encode() + b'\n' + raw
        dom = dict(meeting_id='S1', sha256=sha256_bytes(raw), with_speakers_sha256=sha256_bytes(headered),
                   groups=[dict(header=header, sentences=[dict(id='sentence-1', source_id='provider-1', text=raw.decode())])])
        artifacts = {'dom_source': self.bank.parent / 'dom.json', 'with_speakers': self.bank.parent / 'headered.txt'}
        artifacts['dom_source'].write_bytes(json_bytes(dom))
        artifacts['with_speakers'].write_bytes(headered)
        hashes = {k: sha256_bytes(p.read_bytes()) for k, p in artifacts.items()}
        output = importar_representacion(self.bank, self.fixture.tr, self.fixture.vid, artifacts, hashes,
                                        company='synthetic', audience='internal', commit=True)
        result = self.render()
        full = next(c['content'] for c in result['candidates'] if c['kind'] == 'transcript_view')
        self.assertIn(header, full)
        self.assertIn('Etiquetas sin resolver', full)
        self.assertEqual(len(result['evidence']['representation_ids']), 1)
        manifest = load_json(self.bank / output['outputs'][0]['path'])
        (self.bank / manifest['artifacts']['with_speakers']['path']).write_bytes(b'changed')
        with self.assertRaisesRegex(ModelError, 'REPRESENTATION_CHANGED'):
            self.render()

    def test_stale_analysis_is_not_rendered(self):
        self.fixture.grant('local_analysis', 'revoke')
        self.fixture.grant('local_analysis')
        with self.assertRaisesRegex(ModelError, 'ANALYSIS_NOT_CURRENT'):
            self.render()


if __name__ == '__main__':
    unittest.main()
