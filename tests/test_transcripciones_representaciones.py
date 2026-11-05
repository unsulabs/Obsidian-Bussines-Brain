"""Synthetic only: representation fidelity, permission boundary and byte mapping."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from test_transcripciones_custodia import capture
from transcripciones_custodia import register_capture, load_catalog
from transcripciones_modelo import ModelError, json_bytes, load_json, sha256_bytes, utc_now
from transcripciones_permisos import record_decision
from transcripciones_representaciones import importar_representacion
import transcripciones_representaciones as representations


class RepresentationTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        self.bank = self.root / 'bank'
        self.groups = [dict(header='Hablante A 00:01:03', html='<b>synthetic</b>', sentences=[
            dict(id='s-1', source_id='src-1', text='Sí 🙂'),
            dict(id='s-2', source_id='src-2', text='Repetido')]),
            dict(header='Hablante B0000:02:00', html='<b>second</b>', sentences=[
                dict(id='s-3', source_id='src-3', text='Repetido')])]
        self.raw = '\n'.join(s['text'] for g in self.groups for s in g['sentences']).encode()
        ids = register_capture(self.bank, capture(self.root, self.raw), commit=True)['evidence']
        self.tr, self.vid = ids['tr_id'], ids['version_id']
        self.grant()
        self.artifacts = {k:self.root / (k + '.bin') for k in ('dom_source', 'with_speakers', 'html')}
        self.artifacts['html'].write_bytes(b'<html>synthetic auxiliary</html>')
        self.seal()

    def grant(self, action='grant'):
        record_decision(self.bank, dict(tr_id=self.tr, version_id=self.vid,
            company='synthetic', audience='internal', purpose='local_analysis', action=action,
            authority='Fixture owner', evidence=['Synthetic authorization'], decided_at=utc_now()), commit=True)

    def seal(self):
        headered = '\n\n'.join(g['header']+'\n'+'\n'.join(s['text'] for s in g['sentences']) for g in self.groups).encode()
        self.artifacts['with_speakers'].write_bytes(headered)
        self.dom = dict(meeting_id='meeting-a', groups=self.groups, sha256=sha256_bytes(self.raw),
            with_speakers_sha256=sha256_bytes(headered), sentence_count=3, arbitrary_metadata={'preserved':True})
        self.artifacts['dom_source'].write_bytes(json_bytes(self.dom))
        self.hashes = {k:sha256_bytes(p.read_bytes()) for k,p in self.artifacts.items()}

    def run_import(self, **kwargs):
        return importar_representacion(self.bank, self.tr, self.vid, self.artifacts, self.hashes,
                                       company='synthetic', audience='internal', **kwargs)

    def snapshot(self):
        return {str(p.relative_to(self.bank)):p.read_bytes() for p in self.bank.rglob('*') if p.is_file()}

    def test_roundtrip_offsets_and_idempotence(self):
        before = load_catalog(self.bank)
        output = self.run_import(commit=True)
        manifest = load_json(self.bank / output['outputs'][0]['path'])
        headered = self.artifacts['with_speakers'].read_bytes()
        for s, expected in zip(manifest['sentences'], [b'S\xc3\xad \xf0\x9f\x99\x82',b'Repetido',b'Repetido']):
            self.assertEqual(self.raw[s['raw_start']:s['raw_end']], expected)
            self.assertEqual(headered[s['headered_start']:s['headered_end']], expected)
        self.assertNotEqual(manifest['sentences'][1]['provider_sentence_id'], manifest['sentences'][2]['provider_sentence_id'])
        self.assertEqual(manifest['groups'][0]['time_seconds'],63)
        self.assertIsNone(manifest['groups'][1]['time_seconds'])
        self.assertEqual(manifest['groups'][1]['provider_header'],self.groups[1]['header'])
        for role, artifact in manifest['artifacts'].items():
            self.assertEqual((self.bank / artifact['path']).read_bytes(),self.artifacts[role].read_bytes())
        snapshot=self.snapshot()
        self.assertTrue(self.run_import(commit=True)['evidence']['idempotent'])
        self.assertEqual(self.snapshot(),snapshot)
        self.assertEqual(load_catalog(self.bank),before)

    def test_dry_run_no_writes(self):
        before=self.snapshot()
        self.assertFalse(self.run_import()['evidence']['committed'])
        self.assertEqual(self.snapshot(),before)

    def test_changed_sidecar_rejected(self):
        self.artifacts['dom_source'].write_bytes(b'{}')
        with self.assertRaisesRegex(ModelError,'HASH_MISMATCH'): self.run_import(commit=True)
        self.assertFalse((self.bank/'representaciones').exists())

    def test_raw_reconstruction_mismatch_even_with_fresh_sidecar_hash(self):
        self.groups[0]['sentences'][0]['text']='changed'
        self.seal()
        with self.assertRaisesRegex(ModelError,'RAW_RECONSTRUCTION_MISMATCH'): self.run_import()

    def test_headered_mismatch_even_with_matching_claimed_hash(self):
        data=self.artifacts['with_speakers'].read_bytes()+b'\n'
        self.artifacts['with_speakers'].write_bytes(data)
        self.dom['with_speakers_sha256']=sha256_bytes(data)
        self.artifacts['dom_source'].write_bytes(json_bytes(self.dom))
        self.hashes={k:sha256_bytes(p.read_bytes()) for k,p in self.artifacts.items()}
        with self.assertRaisesRegex(ModelError,'HEADERED_RECONSTRUCTION_MISMATCH'): self.run_import()

    def test_permission_checked_before_content_read(self):
        self.grant('revoke')
        with patch('transcripciones_representaciones.load_catalog',side_effect=AssertionError('read too early')):
            with self.assertRaisesRegex(ModelError,'PERMISSION_DENIED'): self.run_import()

    def test_wrong_audience_and_omitted_scope_denied(self):
        with self.assertRaisesRegex(ModelError,'PERMISSION_DENIED'):
            importar_representacion(self.bank,self.tr,self.vid,self.artifacts,self.hashes,company='synthetic',audience='public')
        with self.assertRaises(TypeError): importar_representacion(self.bank,self.tr,self.vid,self.artifacts,self.hashes)

    def test_duplicate_sentence_id_rejected(self):
        self.groups[1]['sentences'][0]['id']='s-1'
        self.seal()
        with self.assertRaisesRegex(ModelError,'PROVIDER_SENTENCE_ID_DUPLICATE'): self.run_import()

    def test_tampered_canonical_raw_rejected(self):
        next((self.bank/'originales').glob('*.bin')).write_bytes(b'tampered')
        with self.assertRaisesRegex(ModelError,'HASH_MISMATCH'): self.run_import()

    def test_tampered_committed_blob_rejected_without_repair(self):
        output=self.run_import(commit=True)
        manifest=load_json(self.bank/output['outputs'][0]['path'])
        path=self.bank/manifest['artifacts']['html']['path']
        path.write_bytes(b'tampered')
        with self.assertRaisesRegex(ModelError,'HASH_MISMATCH'): self.run_import(commit=True)
        self.assertEqual(path.read_bytes(),b'tampered')

    def test_correction_appends_no_overwrite(self):
        first=self.run_import(commit=True)
        path=self.bank/first['outputs'][0]['path']; before=path.read_bytes()
        self.groups[0]['header']='Hablante corregido 00:01:03'; self.seal()
        second=self.run_import(commit=True)
        self.assertNotEqual(first['evidence']['representation_id'],second['evidence']['representation_id'])
        self.assertEqual(path.read_bytes(),before)
        self.assertEqual(len(load_catalog(self.bank)),1)
        self.assertEqual(len(load_catalog(self.bank)[0]['version_ids']),1)

    def test_foreign_meeting_rejected(self):
        self.dom['meeting_id']='another-meeting'
        self.artifacts['dom_source'].write_bytes(json_bytes(self.dom))
        self.hashes['dom_source']=sha256_bytes(self.artifacts['dom_source'].read_bytes())
        with self.assertRaisesRegex(ModelError,'PROVIDER_MEETING_MISMATCH'): self.run_import()

    def test_missing_hash_or_extra_unpinned_artifact_rejected(self):
        del self.hashes['html']
        with self.assertRaisesRegex(ModelError,'ARTIFACTS_INVALID'): self.run_import()

    def test_crash_before_manifest_is_invisible_and_retryable(self):
        original_write=representations.atomic_write
        def fail_manifest(bank,path,data):
            if '/manifests/' in path: raise OSError('synthetic interrupted write')
            return original_write(bank,path,data)
        with patch('transcripciones_representaciones.atomic_write',side_effect=fail_manifest):
            with self.assertRaises(OSError): self.run_import(commit=True)
        self.assertFalse(list((self.bank/'representaciones'/'manifests').glob('*.json')))
        self.assertTrue(self.run_import(commit=True)['evidence']['committed'])

    def test_manifest_tampering_never_overwritten(self):
        output=self.run_import(commit=True)
        path=self.bank/output['outputs'][0]['path']
        path.write_bytes(b'{}')
        with self.assertRaisesRegex(ModelError,'IMMUTABLE_CONFLICT'): self.run_import(commit=True)
        self.assertEqual(path.read_bytes(),b'{}')

    def test_bank_in_git_or_vault_rejected(self):
        for marker in ('.git','.obsidian'):
            root=self.root/marker[1:];root.mkdir();(root/marker).mkdir()
            with self.assertRaisesRegex(ModelError,'BANK_INSIDE_'):
                importar_representacion(root/'bank',self.tr,self.vid,self.artifacts,self.hashes,
                                         company='synthetic',audience='internal',commit=True)
            self.assertFalse((root/'bank').exists())


if __name__ == '__main__':
    unittest.main()
