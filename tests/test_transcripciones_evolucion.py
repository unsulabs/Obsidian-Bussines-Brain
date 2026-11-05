"""Evolución de versiones y análisis con archivos/banco sintéticos."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import test_transcripciones_pipeline
from transcripciones_pipeline import consolidate_analysis
from transcripciones_ingreso import ingest
from transcripciones_fichas import render_source
from transcripciones_modelo import sha256_bytes, ModelError
from lib_ce import make_note, split_frontmatter
from transcripciones_evolucion import START, END, lineage
import transcripciones_integracion as integration


class EvolutionTests(unittest.TestCase):
    def setUp(self):
        self.fixture = test_transcripciones_pipeline.PipelineTests(); self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.bank = self.fixture.bank
        self.vault = self.bank.parent / 'vault'; self.vault.mkdir()
        self.snapshot = dict(vault=str(self.vault), bank_root=str(self.bank), backup_dir=str(self.bank.parent / 'backup'))
        self.first_submission = self.fixture.submission()
        consolidate_analysis(self.bank, self.first_submission, **self.fixture.scope, commit=True)
        initial = self.render('RUN-fixture')
        self.source_path = initial['candidates'][0]['path']
        self.first_version = self.fixture.vid
        self.old_view = next(c['path'] for c in initial['candidates'] if c['kind'] == 'transcript_view')
        self.first_id = initial['candidates'][0]['id']
        self.first_manifest = integration.prepare_batch(initial['candidates'], self.snapshot)
        self.apply(self.first_manifest, 1)

    def render(self, run):
        return render_source(self.fixture.tr, run, dict(bank=self.bank, **self.fixture.scope,
            vault_snapshot={p.relative_to(self.vault).as_posix(): p.read_text(encoding='utf-8') for p in self.vault.rglob('*.md')},
            source_sensitivity={self.fixture.tr: 'interno'}))

    def apply(self, manifest, token=2):
        return integration.apply_batch(manifest, dict(manifest_sha=manifest['manifest_sha'], scope='apply_batch',
            writers_quiescent=True, responsable='Fixture', referencia='Evolución sintética autorizada'), token)

    def new_analysis(self, run='RUN-next', *, new_version=True, supersedes=None, attempt='A2', narrow=False):
        if new_version:
            data = self.fixture.authored['data'][:-1] + (b'\n' if attempt == 'A2' else b'.')
            receipt = ingest(self.bank, job_id='J1', account_id='local', source_id='S1', attempt_id=attempt,
                parts=[(1, data)], expected_parts=1, closed=True, commit=True)
            self.fixture.vid = receipt['evidence']['version_id']
            self.fixture.authored['data'] = data
            self.fixture.grant('local_analysis'); self.fixture.grant('internal_query')
            def spans(value):
                if isinstance(value, list):
                    for x in value: spans(x)
                elif isinstance(value, dict):
                    if 'excerpt_sha256' in value:
                        value['text_sha256'] = sha256_bytes(data)
                        value['excerpt_sha256'] = sha256_bytes(data[value['start']:value['end']])
                    for x in value.values(): spans(x)
            spans(self.fixture.authored)
        submitted = self.fixture.submission()
        mapping = {'RUN-fixture': run, **{c['claim_id']: run + '-' + c['claim_id'] for c in submitted['claims']}}
        def rename(value):
            if isinstance(value, str): return mapping.get(value, value)
            if isinstance(value, list): return [rename(x) for x in value]
            if isinstance(value, dict): return {k: rename(v) for k, v in value.items()}
            return value
        submitted = rename(submitted)
        if narrow:
            raw = self.fixture.authored['data']
            def narrow_span(value):
                if isinstance(value, list):
                    for child in value: narrow_span(child)
                elif isinstance(value, dict):
                    if 'excerpt_sha256' in value and value['start'] == 0:
                        value['end'] -= 1
                        value['excerpt_sha256'] = sha256_bytes(raw[:value['end']])
                    for child in value.values(): narrow_span(child)
            narrow_span(submitted)
        submitted['supersedes_run_id'] = supersedes
        submitted['global_reconciliation']['summary'] = 'Revisión sintética ' + run
        consolidate_analysis(self.bank, submitted, **self.fixture.scope, commit=True)
        return submitted

    def test_new_version_preserves_identity_views_customizations_and_exact_rollback(self):
        source_file = self.vault / self.source_path
        fm, body = split_frontmatter(source_file.read_text(encoding='utf-8')); fm['tags'] = ['revision-propia']
        source_file.write_text(make_note(fm, body + '\n## Anotación propia\nConservar este destino del equipo.\n'), encoding='utf-8', newline='\n')
        (self.vault / self.old_view).write_text((self.vault / self.old_view).read_text(encoding='utf-8') + '\nAnotación de vista anterior.\n', encoding='utf-8', newline='\n')
        before = integration._inventory(self.vault)
        self.new_analysis()
        output = self.render('RUN-next'); source = output['candidates'][0]
        self.assertEqual((source['id'], source['path']), (self.first_id, self.source_path))
        self.assertIn('Conservar este destino del equipo.', source['content'])
        self.assertIn('revision-propia', source['content'])
        self.assertIn('Historial de propuestas', source['content'])
        self.assertIn('completeness: ver_evidencia_de_esta_version', source['content'])
        self.assertIn('completeness_evidence:', source['content'])
        self.assertFalse(any(c['path'] == self.old_view for c in output['candidates']))
        manifest = integration.prepare_batch(output['candidates'], self.snapshot)
        with self.assertRaisesRegex(ValueError, 'Fencing'):
            self.apply(manifest, 1)
        self.apply(manifest); self.apply(manifest)
        self.assertEqual(sha256_bytes((self.vault / self.old_view).read_bytes()), before[self.old_view])
        next_render = self.render('RUN-next')
        self.assertEqual(next_render['candidates'][0]['content'], (self.vault / self.source_path).read_text(encoding='utf-8'))
        self.assertNotIn('source_transition', next_render['candidates'][0])
        integration.rollback_batch(manifest)
        self.assertEqual(before, integration._inventory(self.vault))

    def test_same_version_new_analysis_requires_direct_supersession(self):
        self.new_analysis(new_version=False, supersedes='RUN-fixture')
        output = self.render('RUN-next')
        manifest = integration.prepare_batch(output['candidates'], self.snapshot)
        before = integration._inventory(self.vault)
        self.apply(manifest)
        self.assertEqual(split_frontmatter((self.vault / self.source_path).read_text(encoding='utf-8'))[0]['version_id'], self.first_version)
        integration.rollback_batch(manifest)
        self.assertEqual(before, integration._inventory(self.vault))

    def test_same_version_analysis_branch_and_version_skip_rejected(self):
        self.new_analysis(new_version=False)
        with self.assertRaisesRegex(ModelError, 'ANALYSIS_NOT_DIRECT_SUCCESSOR'):
            self.render('RUN-next')
        self.new_analysis(run='RUN-v2', attempt='A2')
        self.new_analysis(run='RUN-v3', attempt='A3')
        with self.assertRaisesRegex(ModelError, 'VERSION_NOT_DIRECT_SUCCESSOR'):
            self.render('RUN-v3')

    def test_historical_permission_revocation_blocks_apply(self):
        self.new_analysis(); output = self.render('RUN-next')
        manifest = integration.prepare_batch(output['candidates'], self.snapshot)
        current = self.fixture.vid; self.fixture.vid = self.first_version
        self.fixture.grant('internal_query', 'revoke'); self.fixture.vid = current
        before = integration._inventory(self.vault)
        with self.assertRaises(ValueError): self.apply(manifest)
        self.assertEqual(before, integration._inventory(self.vault))

    def test_parallel_analysis_successors_are_not_chosen_implicitly(self):
        self.new_analysis(run='RUN-a', new_version=False, supersedes='RUN-fixture')
        self.new_analysis(run='RUN-b', new_version=False, supersedes='RUN-fixture')
        with self.assertRaisesRegex(ModelError, 'BRANCH_AMBIGUOUS'):
            self.render('RUN-a')

    def test_removing_historical_access_checks_does_not_bypass_transition_permissions(self):
        self.new_analysis(); output = self.render('RUN-next')
        for candidate in output['candidates']:
            candidate.pop('access_checks', None)
        current = self.fixture.vid; self.fixture.vid = self.first_version
        self.fixture.grant('internal_query', 'revoke'); self.fixture.vid = current
        with self.assertRaises(ValueError): integration.prepare_batch(output['candidates'], self.snapshot)

    def test_concurrent_note_or_historical_view_edit_is_not_overwritten(self):
        self.new_analysis(); output = self.render('RUN-next')
        manifest = integration.prepare_batch(output['candidates'], self.snapshot)
        (self.vault / self.old_view).write_text((self.vault / self.old_view).read_text(encoding='utf-8') + '\nEdición posterior.\n', encoding='utf-8', newline='\n')
        before = integration._inventory(self.vault)
        with self.assertRaises(ValueError): self.apply(manifest)
        self.assertEqual(before, integration._inventory(self.vault))

    def test_approved_source_and_unproved_transition_rejected(self):
        self.new_analysis(); output = self.render('RUN-next')
        bad = deepcopy(output['candidates']); del bad[0]['source_transition']
        with self.assertRaisesRegex(ValueError, 'transición'): integration.prepare_batch(bad, self.snapshot)
        truncated = deepcopy(output['candidates']); truncated[0]['source_transition']['history_views'] = []
        with self.assertRaisesRegex(ModelError, 'HISTORICAL_VIEW_MISSING'):
            integration.prepare_batch(truncated, self.snapshot)
        path = self.vault / self.source_path; path.write_text(path.read_text(encoding='utf-8').replace('estado_editorial: borrador', 'estado_editorial: aprobado'), encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ModelError, 'EDITORIAL_INVALID'): self.render('RUN-next')

    def test_transition_requires_exact_history_entry_and_preserved_chain(self):
        self.new_analysis(); output = self.render('RUN-next')
        def rejects_histories(candidates):
            fm, body = split_frontmatter(candidates[0]['content'])
            history = fm['historial_fuentes']
            invalid = [[], history[:-1], history + [history[-1]]]
            for field in ('version_id', 'run_id', 'source_sha256', 'view_path'):
                changed = deepcopy(history); changed[-1][field] = 'forged'
                invalid.append(changed)
            if len(history) > 1:
                invalid.extend([history[1:], list(reversed(history))])
            for value in invalid:
                with self.subTest(history=value):
                    bad = deepcopy(candidates)
                    bad[0]['content'] = make_note({**fm, 'historial_fuentes': value}, body)
                    before = integration._inventory(self.vault)
                    with self.assertRaisesRegex(ModelError, 'SOURCE_HISTORY_LOST'):
                        integration.prepare_batch(bad, self.snapshot)
                    self.assertEqual(before, integration._inventory(self.vault))
        rejects_histories(output['candidates'])
        self.apply(integration.prepare_batch(output['candidates'], self.snapshot))
        self.new_analysis(run='RUN-third', attempt='A3')
        third = self.render('RUN-third')
        rejects_histories(third['candidates'])
        before = integration._inventory(self.vault)
        manifest = integration.prepare_batch(third['candidates'], self.snapshot)
        self.apply(manifest, 3)
        integration.rollback_batch(manifest)
        self.assertEqual(before, integration._inventory(self.vault))

    def test_same_version_new_passages_create_separate_immutable_view(self):
        self.new_analysis(new_version=False, supersedes='RUN-fixture', narrow=True)
        output = self.render('RUN-next')
        new_view = next(c for c in output['candidates'] if c['kind'] == 'transcript_view')
        self.assertNotEqual(new_view['path'], self.old_view)
        self.assertIn('view_variant:', new_view['content'])
        before = integration._inventory(self.vault)
        manifest = integration.prepare_batch(output['candidates'], self.snapshot)
        self.apply(manifest)
        self.assertEqual(sha256_bytes((self.vault / self.old_view).read_bytes()), before[self.old_view])
        integration.rollback_batch(manifest)
        self.assertEqual(before, integration._inventory(self.vault))

    def test_foreign_version_and_later_edit_in_new_view_are_preserved(self):
        foreign = ingest(self.bank, job_id='J2', account_id='local', source_id='OTHER', attempt_id='B1',
            parts=[(1, b'Fuente ajena sintetica')], expected_parts=1, closed=True, commit=True)
        with self.assertRaisesRegex(ModelError, 'NOT_IN_CATALOG'):
            lineage(self.bank, self.fixture.tr, self.first_version, foreign['evidence']['version_id'])
        self.new_analysis(); output = self.render('RUN-next')
        manifest = integration.prepare_batch(output['candidates'], self.snapshot); self.apply(manifest)
        new_view = next(c['path'] for c in output['candidates'] if c['kind'] == 'transcript_view')
        path = self.vault / new_view; path.write_text(path.read_text(encoding='utf-8') + '\nEdición posterior en vista nueva.\n', encoding='utf-8', newline='\n')
        before = integration._inventory(self.vault)
        with self.assertRaises(ValueError): integration.rollback_batch(manifest)
        self.assertEqual(before, integration._inventory(self.vault))

    def test_legacy_without_markers_keeps_entire_body_as_history(self):
        path = self.vault / self.source_path
        meta, body = split_frontmatter(path.read_text(encoding='utf-8'))
        meta.pop('view_path')
        legacy_body = body.replace(START, '').replace(END, '') + '\nAnotación legacy irremplazable.\n'
        path.write_text(make_note(meta, legacy_body), encoding='utf-8', newline='\n')
        before = integration._inventory(self.vault)
        self.new_analysis(); output = self.render('RUN-next')
        self.assertIn(legacy_body, output['candidates'][0]['content'])
        manifest = integration.prepare_batch(output['candidates'], self.snapshot); self.apply(manifest)
        integration.rollback_batch(manifest)
        self.assertEqual(before, integration._inventory(self.vault))


if __name__ == '__main__':
    unittest.main()
