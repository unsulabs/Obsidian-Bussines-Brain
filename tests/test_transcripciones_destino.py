"""Synthetic private destinations, permissions, classification and reversibility."""
from copy import deepcopy
import base64
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import test_transcripciones_fichas
import transcripciones_integracion as ti
from transcripciones_fichas import render_source, propose_navigation
from transcripciones_destino import destination, classification


class DestinationTests(unittest.TestCase):
    def setUp(self):
        self.f = test_transcripciones_fichas.FichaTests()
        self.f.setUp()
        self.addCleanup(self.f.tearDown)
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.vault = self.root / 'vault'
        self.vault.mkdir()
        self.policy_path = self.root / 'policy.json'
        self.policy = dict(schema=1, active=True, vault=str(self.vault),
                           company=self.f.profile['company'], audience=self.f.profile['audience'],
                           purposes=['local_analysis', 'internal_query'],
                           allowed_sensitivities=['interno', 'confidencial', 'restringido'],
                           source_sensitivity={self.f.fixture.tr: 'restringido'},
                           authorization=dict(responsable='Synthetic owner', referencia='Synthetic explicit authorization'))
        self.bind()

    def bind(self):
        self.policy_path.write_text(json.dumps(self.policy))
        self.binding = dict(path=str(self.policy_path), sha256=ti._sha(self.policy_path.read_bytes()))
        self.profile = dict(self.f.profile, destination_profile=self.binding, vault=str(self.vault))
        self.snapshot = dict(vault=str(self.vault), backup_dir=str(self.root / 'backup'),
                             bank_root=str(self.f.bank), destination_profile=self.binding)

    def candidates(self):
        candidates = render_source(self.f.fixture.tr, 'RUN-fixture', self.profile)['candidates']
        return candidates + propose_navigation(candidates, self.profile['vault_snapshot'])

    def apply(self, manifest):
        return ti.apply_batch(manifest, dict(manifest_sha=manifest['manifest_sha'], scope='apply_batch',
                              writers_quiescent=True, responsable='Synthetic', referencia='Synthetic'), 1)

    def test_three_levels_and_rollback_preserve_originals(self):
        original = self.f.fixture.snapshot_bytes()
        for level in ('interno', 'confidencial', 'restringido'):
            with self.subTest(level=level):
                self.policy['source_sensitivity'][self.f.fixture.tr] = level
                self.bind()
                candidates = self.candidates()
                self.assertTrue(all(c['sensibilidad'] == level for c in candidates))
                m = ti.prepare_batch(candidates, self.snapshot)
                self.apply(m)
                self.assertEqual(self.f.fixture.snapshot_bytes(), original)
                ti.rollback_batch(m)
                self.assertEqual(ti._inventory(self.vault), {})
                # New vault identity avoids reusing a writer fence for another batch.
                self.vault = self.root / ('vault-' + level)
                self.vault.mkdir()
                self.policy['vault'] = str(self.vault)

    def test_policy_change_wrong_destination_unknown_source_and_export(self):
        candidates = self.candidates()
        other = self.root / 'other'
        other.mkdir()
        with self.assertRaisesRegex(ValueError, 'DESTINATION'):
            ti.prepare_batch(candidates, dict(self.snapshot, vault=str(other)))
        with self.assertRaisesRegex(ValueError, 'DESTINATION_SOURCE_DENIED'):
            classification(self.policy, [{'tr_id': 'TR-unknown'}])
        with self.assertRaisesRegex(ValueError, 'DESTINATION_POLICY_INVALID'):
            destination(self.binding, self.vault, dict(self.f.fixture.scope, purpose='export'))
        m = ti.prepare_batch(candidates, self.snapshot)
        self.policy['active'] = False
        self.policy_path.write_text(json.dumps(self.policy))
        with self.assertRaisesRegex(ValueError, 'DESTINATION_POLICY_CHANGED'):
            self.apply(m)
        self.assertEqual(ti._inventory(self.vault), {})

    def test_revocation_at_render_prepare_and_apply(self):
        candidates = self.candidates()
        m = ti.prepare_batch(candidates, self.snapshot)
        self.f.fixture.grant('internal_query', 'revoke')
        for operation in (self.candidates, lambda: ti.prepare_batch(candidates, self.snapshot), lambda: self.apply(m)):
            with self.assertRaises(ValueError):
                operation()
        self.assertEqual(ti._inventory(self.vault), {})

    def test_no_declassification_or_policy_bypass(self):
        for change in ('candidate', 'content', 'dependency', 'binding'):
            candidates = self.candidates()
            c = candidates[0]
            if change == 'candidate':
                c['sensibilidad'] = 'interno'
            elif change == 'content':
                c['content'] = c['content'].replace('sensibilidad: restringido', 'sensibilidad: interno')
            elif change == 'dependency':
                candidates[-1]['access_checks'][0]['sensibilidad'] = 'interno'
            else:
                c.pop('destination_profile')
            with self.subTest(change=change), self.assertRaises(ValueError):
                ti.prepare_batch(candidates, self.snapshot)

    def test_mixed_dependencies_use_maximum_and_postedit_is_preserved(self):
        candidates = self.candidates()
        internal = deepcopy(candidates[0])
        internal.update(tr_id='TR-other', sensibilidad='interno', local_private_only=False)
        mixed = propose_navigation([internal, candidates[0]], {})
        self.assertTrue(all(c['sensibilidad'] == 'restringido' for c in mixed))
        nav = next(c for c in candidates if c['kind'] == 'navigation')
        self.assertIn('sensibilidad: restringido', nav['content'])
        m = ti.prepare_batch(candidates, self.snapshot)
        self.apply(m)
        path = self.vault / candidates[0]['path']
        path.write_text(path.read_text() + '\nManual edit\n')
        with self.assertRaisesRegex(ValueError, 'Edición posterior'):
            ti.rollback_batch(m)
        self.assertTrue(path.read_text().endswith('Manual edit\n'))

    def test_existing_generic_base_is_not_rewritten(self):
        candidates = self.candidates()
        base = next(c for c in candidates if c['kind'] == 'base_view')
        old = base['content'].replace('sensibilidad: restringido', 'sensibilidad: interno') + 'custom: preserved\n'
        path = self.vault / base['path']
        path.parent.mkdir(parents=True)
        path.write_text(old)
        self.profile['vault_snapshot'] = {base['path']: old}
        m = ti.prepare_batch(self.candidates(), self.snapshot)
        self.apply(m)
        self.assertIn('custom: preserved', path.read_text())
        self.assertEqual(path.read_text(), old)
        ti.rollback_batch(m)
        self.assertEqual(path.read_text(), old)

    def test_partial_apply_and_revoked_policy_rollback(self):
        m = ti.prepare_batch(self.candidates(), self.snapshot)
        def crash(stage, path):
            if stage == 'file_written':
                raise RuntimeError('Synthetic crash')
        with patch('transcripciones_integracion._checkpoint', side_effect=crash), self.assertRaises(RuntimeError):
            self.apply(m)
        self.policy_path.write_text('{}')
        ti.rollback_batch(m)
        self.assertEqual(ti._inventory(self.vault), {})

    def test_navigation_append_preserves_body_and_upgrades_metadata(self):
        text = '---\nid: NAV-start\ntipo: manual\nsensibilidad: interno\n---\n# Existing\n'
        (self.vault / 'Inicio.md').write_text(text)
        self.profile['vault_snapshot'] = {'Inicio.md': text}
        m = ti.prepare_batch(self.candidates(), self.snapshot)
        self.apply(m)
        result = (self.vault / 'Inicio.md').read_text()
        self.assertIn('sensibilidad: restringido', result)
        self.assertIn('# Existing\n', result)
        ti.rollback_batch(m)
        self.assertEqual((self.vault / 'Inicio.md').read_text(), text)

    def test_private_navigation_resealed_manifest_cannot_erase_or_change_body(self):
        text = '---\nid: NAV-start\ntipo: manual\nsensibilidad: interno\n---\n# Existing\nKeep instructions.\n'
        (self.vault / 'Inicio.md').write_text(text)
        self.profile['vault_snapshot'] = {'Inicio.md': text}
        manifest = ti.prepare_batch(self.candidates(), self.snapshot)
        before = ti._inventory(self.vault)
        for replacement in (b'', b'# Replaced\n'):
            with self.subTest(replacement=replacement):
                m = deepcopy(manifest)
                e = next(e for e in m['entries'] if e['kind'] == 'navigation_append')
                raw = base64.b64decode(e['content_b64']).replace(b'# Existing\nKeep instructions.\n', replacement)
                e['content_b64'] = base64.b64encode(raw).decode()
                e['proposed_sha'] = ti._sha(raw)
                m['manifest_sha'] = ti._sha(ti._json({k: v for k, v in m.items() if k != 'manifest_sha'}))
                with self.assertRaisesRegex(ValueError, 'append'):
                    self.apply(m)
                self.assertEqual(ti._inventory(self.vault), before)
                self.assertFalse(Path(m['backup_dir']).exists())

    def test_existing_source_keeps_bound_historical_access(self):
        candidates = self.candidates()
        m = ti.prepare_batch(candidates, self.snapshot)
        self.apply(m)
        self.profile['vault_snapshot'] = {c['path']: c['content'] for c in candidates}
        rerender = self.candidates()
        self.assertEqual(rerender[0]['access_checks'][0]['destination_profile'], self.binding)
        ti.prepare_batch(rerender, self.snapshot)
