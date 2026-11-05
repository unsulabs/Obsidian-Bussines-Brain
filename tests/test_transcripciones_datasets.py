"""Synthetic U29 purpose, exact-byte lineage, split and transaction boundaries."""
from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from test_transcripciones_custodia import capture
from transcripciones_custodia import register_capture, load_catalog
from transcripciones_modelo import ModelError, load_json, sha256_bytes, utc_now
from transcripciones_modelo import json_bytes
from transcripciones_permisos import record_decision, permission_snapshot
from transcripciones_datasets import prepare_export, inspect_exports
import transcripciones_datasets as datasets


class DatasetTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.bank = self.root / 'bank'
        self.raw = 'Contexto. Sí 🙂 funciona. Fin.'.encode()
        self.ref = self.source(self.raw)
        self.grant(self.ref)
        self.selection = self.select(self.ref, self.raw)

    def source(self, data, **kwargs):
        e = register_capture(self.bank, capture(self.root, data, **kwargs), commit=True)['evidence']
        return e['tr_id'], e['version_id']

    def grant(self, ref, purpose='evaluation', action='grant'):
        record_decision(self.bank, dict(tr_id=ref[0], version_id=ref[1], company='fixture',
            audience='internal', purpose=purpose, action=action, authority='Synthetic owner',
            evidence=['Synthetic purpose permission'], decided_at=utc_now()), commit=True)

    def select(self, ref, data):
        return dict(allow_historical=False, identities={r['tr_id']:dict(client=None,
            project=None, evidence='Synthetic fixture has no client or project') for r in load_catalog(self.bank)},
            candidates=[dict(candidate_id='c1', task='Explain fixture', criterion='Accurate',
                expected_result='Synthetic result', exception=None, observed_response='Synthetic answer',
                expert_correction=None, passages=[dict(tr_id=ref[0], version_id=ref[1],
                    source_sha256=sha256_bytes(data), start=0, end=len(data), context_start=0,
                    context_end=len(data), passage_sha256=sha256_bytes(data), context_sha256=sha256_bytes(data))])])

    def snap(self, purpose='evaluation', selection=None):
        s = selection or self.selection
        return permission_snapshot(self.bank, source_refs=datasets._refs(s),
                                   company='fixture', audience='internal', purpose=purpose)

    def export(self, purpose='evaluation', **kwargs):
        return prepare_export(self.selection, purpose, kwargs.pop('snapshot', self.snap(purpose)),
            bank=self.bank, company='fixture', audience='internal', **kwargs)

    def test_preview_commit_lineage_and_idempotence(self):
        before = {str(p):p.read_bytes() for p in self.bank.rglob('*') if p.is_file()}
        preview = self.export()
        self.assertEqual(before, {str(p):p.read_bytes() for p in self.bank.rglob('*') if p.is_file()})
        committed = self.export(commit=True)
        self.assertEqual(preview['evidence']['manifest']['candidates'], committed['evidence']['manifest']['candidates'])
        manifest = load_json(self.bank / committed['outputs'][0]['path'])
        self.assertEqual(manifest['candidates'][0]['passages'][0]['text'].encode(), self.raw)
        self.assertEqual(manifest['status'], 'proposed')
        self.assertFalse(manifest['trained'])
        self.assertEqual(committed, self.export(commit=True))

    def test_exact_purpose_scope_and_revocation(self):
        self.grant(self.ref, 'internal_query')
        self.assertEqual(self.export('training')['evidence']['manifest']['candidates'], [])
        self.export(commit=True)
        old = self.snap()
        self.grant(self.ref, action='revoke')
        with self.assertRaisesRegex(ModelError, 'PERMISSION_SNAPSHOT_CHANGED'):
            self.export(snapshot=old, commit=True)
        self.assertFalse(inspect_exports(bank=self.bank)[0]['permission_current'])
        self.assertEqual(self.export()['evidence']['manifest']['candidates'], [])
        with self.assertRaisesRegex(ModelError, 'PERMISSION_SNAPSHOT_CHANGED'):
            prepare_export(self.selection,'evaluation',self.snap(),bank=self.bank,company='other',audience='internal')

    def test_hash_offsets_context_and_utf8(self):
        original = deepcopy(self.selection)
        for key, value, error in [('source_sha256','0'*64,'HASH_MISMATCH'),
                ('passage_sha256','0'*64,'HASH_MISMATCH'),('context_sha256','0'*64,'HASH_MISMATCH'),
                ('end',len(self.raw)+1,'PASSAGE_RANGE_INVALID'),('context_start',1,'PASSAGE_RANGE_INVALID')]:
            with self.subTest(key=key):
                self.selection = deepcopy(original)
                self.selection['candidates'][0]['passages'][0][key] = value
                with self.assertRaisesRegex(ModelError,error): self.export()
        self.selection = original
        p = self.selection['candidates'][0]['passages'][0]
        p['start'] = self.raw.index('í'.encode())+1
        p['passage_sha256'] = sha256_bytes(self.raw[p['start']:])
        with self.assertRaisesRegex(ModelError,'PASSAGE_ENCODING_INVALID'): self.export()

    def test_same_conversation_cannot_change_split(self):
        self.export(commit=True)
        self.grant(self.ref,'training')
        with self.assertRaisesRegex(ModelError,'SPLIT_LEAKAGE'): self.export('training',commit=True)

    def test_versions_and_cross_account_duplicate_bridge(self):
        self.export(commit=True)
        duplicate = self.source(self.raw, account='account-b', attempt='b1')
        changed = self.source(b'new version', account='account-b', attempt='b2')
        self.grant(changed, 'training')
        # Exclude the duplicate version from selection and from permissions.
        self.selection = self.select(changed,b'new version')
        with self.assertRaisesRegex(ModelError,'SPLIT_LEAKAGE'): self.export('training')
        self.assertNotEqual(duplicate, changed)

    def test_client_and_project_splits(self):
        for field in ('client','project'):
            with self.subTest(field=field):
                self.setUp()  # isolated synthetic ledger for each dimension
                second = self.source(b'Second', meeting='second', attempt='b1')
                self.grant(second,'training')
                self.selection = self.select(self.ref,self.raw)
                for identity in self.selection['identities'].values(): identity[field]='same-id'
                self.export(commit=True)
                selected = self.select(second,b'Second')
                selected['identities']=deepcopy(self.selection['identities'])
                self.selection=selected
                with self.assertRaisesRegex(ModelError,'SPLIT_LEAKAGE'):
                    self.export('training')

    def test_independent_conversations_can_have_separate_splits(self):
        second = self.source(b'Second', meeting='second', attempt='b1')
        self.selection = self.select(self.ref,self.raw)
        self.export(commit=True)
        self.grant(second,'training')
        self.selection = self.select(second,b'Second')
        self.assertEqual(len(self.export('training',commit=True)['evidence']['manifest']['candidates']),1)

    def test_excluded_candidate_annotations_are_not_exported(self):
        self.selection['candidates'][0]['task']='PRIVATE-ANNOTATION'
        output=self.export('training',commit=True)
        self.assertNotIn('PRIVATE-ANNOTATION',(self.bank/output['outputs'][0]['path']).read_text(encoding='utf-8'))

    def test_identity_cannot_be_changed_to_evade_previous_split(self):
        self.export(commit=True)
        self.selection['identities'][self.ref[0]]['client']='new-client'
        with self.assertRaisesRegex(ModelError,'GROUP_IDENTITY_CHANGED'): self.export()

    def test_late_duplicate_bridge_invalidates_prior_separation(self):
        second=self.source(b'Second',meeting='second',attempt='b1')
        self.selection=self.select(self.ref,self.raw)
        self.export(commit=True)
        self.grant(second,'training')
        self.selection=self.select(second,b'Second')
        self.export('training',commit=True)
        self.source(self.raw,meeting='second',attempt='b2')
        self.selection=self.select(self.ref,self.raw)
        with self.assertRaisesRegex(ModelError,'SPLIT_LEAKAGE'): self.export()

    def test_original_tampering_rejected(self):
        original=load_json(self.bank/f'versiones/{self.ref[1]}.json')
        (self.bank/original['blob_path']).write_bytes(b'tampered')
        with self.assertRaisesRegex(ModelError,'HASH_MISMATCH'): self.export()

    def test_atomic_link_failure_cleans_temporary_payload(self):
        publish = ('windows_fs._K.MoveFileExW' if sys.platform == 'win32'
                   else 'transcripciones_modelo.os.link')
        with patch(publish,side_effect=OSError('synthetic disk failure')):
            with self.assertRaises(OSError): self.export(commit=True)
        self.assertEqual(list((self.bank/'datasets-control').iterdir()),[])
        self.assertFalse((self.bank/'datasets').exists())
        self.assertTrue(self.export(commit=True)['evidence']['committed'])

    def test_denied_and_unselected_identity_metadata_never_in_payload(self):
        denied=self.source(b'Denied',meeting='denied',attempt='d1')
        unselected=self.source(b'Unselected',meeting='unselected',attempt='u1')
        self.selection=self.select(self.ref,self.raw)
        second=self.select(denied,b'Denied')['candidates'][0]
        second['candidate_id']='c2'
        self.selection['candidates'].append(second)
        markers=[]
        for ref,label in ((denied,'DENIED'),(unselected,'UNSELECTED')):
            for key in ('client','project','evidence'):
                marker=f'PRIVATE-{label}-{key}'
                self.selection['identities'][ref[0]][key]=marker
                markers.append(marker)
        for commit in (False,True):
            output=self.export(commit=commit)
            payload=json_bytes(output)
            for value in [*markers,denied[0],denied[1],unselected[0],unselected[1]]:
                self.assertNotIn(value.encode(),payload)
            self.assertNotIn('identities',output['evidence']['manifest']['selection'])
            if commit:
                manifest_path=self.bank/output['outputs'][0]['path']
                self.assertEqual(manifest_path.read_bytes(),json_bytes(output['evidence']['manifest']))
                control=load_json(self.bank/'datasets-control'/manifest_path.name)
                self.assertNotIn(control['nonce'].encode(),payload)
                self.assertEqual(control['identities'],self.selection['identities'])

    def test_control_tampering_and_missing_control_fail_closed(self):
        output=self.export(commit=True)
        path=self.bank/'datasets-control'/Path(output['outputs'][0]['path']).name
        original=path.read_bytes()
        control=load_json(path)
        control['identities'][self.ref[0]]['client']='tampered'
        path.write_bytes(json_bytes(control))
        with self.assertRaisesRegex(ModelError,'DATASET_CONTROL_MISMATCH'): self.export()
        path.write_bytes(original)
        path.unlink()
        with self.assertRaises(ModelError): self.export()

    def test_orphan_control_never_visible_or_returned(self):
        original=datasets.atomic_write
        def fail_manifest(bank,path,data):
            if path.startswith('datasets/'):
                raise OSError('synthetic failure after private control')
            return original(bank,path,data)
        with patch.object(datasets,'atomic_write',side_effect=fail_manifest):
            with self.assertRaises(OSError): self.export(commit=True)
        self.assertEqual(inspect_exports(bank=self.bank),[])
        self.assertFalse((self.bank/'datasets').exists())
        self.assertEqual(len(list((self.bank/'datasets-control').glob('*.json'))),1)
        self.assertTrue(self.export(commit=True)['evidence']['committed'])
        self.assertEqual(len(inspect_exports(bank=self.bank)),1)

    def test_unknown_or_missing_group_rejected(self):
        self.selection['identities'][self.ref[0]]['client']='unknown'
        with self.assertRaisesRegex(ModelError,'GROUP_IDENTITY_UNKNOWN'): self.export()
        self.selection['identities']={}
        with self.assertRaisesRegex(ModelError,'GROUP_COVERAGE_REQUIRED'): self.export()

    def test_historical_requires_explicit_flag_and_exact_permission(self):
        new = self.source(b'Later',attempt='later')
        self.assertNotEqual(new,self.ref)
        with self.assertRaisesRegex(ModelError,'HISTORICAL_FLAG_REQUIRED'): self.export()
        self.selection['allow_historical']=True
        self.assertEqual(len(self.export()['evidence']['manifest']['candidates']),1)

    def test_revoke_between_preparation_and_commit(self):
        original = datasets._prepare
        calls = []
        def racing(*args,**kwargs):
            value=original(*args,**kwargs)
            calls.append(1)
            if len(calls)==1: self.grant(self.ref,action='revoke')
            return value
        # Simulate a concurrent writer arriving between preparations, avoiding a
        # nested acquisition of the process-level bank lock in this test only.
        with patch.object(datasets,'_prepare',side_effect=racing):
            with self.assertRaisesRegex(ModelError,'PERMISSION_SNAPSHOT_CHANGED'):
                with patch.object(datasets,'bank_lock',lambda _: datasets.live_reads()):
                    self.export(commit=True)
        self.assertFalse((self.bank/'datasets').exists())

    def test_interruption_and_collision_do_not_publish_partial(self):
        with patch.object(datasets,'atomic_write',side_effect=OSError('synthetic interruption')):
            with self.assertRaises(OSError): self.export(commit=True)
        self.assertFalse((self.bank/'datasets').exists())
        preview=self.export()
        path=self.bank/preview['outputs'][0]['path']
        path.parent.mkdir();path.write_text('{}', encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ModelError,'SCHEMA_INVALID'): self.export(commit=True)
        self.assertEqual(path.read_text(encoding='utf-8'),'{}')

    def test_reject_derived_payloads_duplicate_ids_and_product_destination(self):
        self.selection['candidates'][0]['run_id']='untrusted-old-analysis'
        with self.assertRaisesRegex(ModelError,'SCHEMA_INVALID'): self.export()
        del self.selection['candidates'][0]['run_id']
        self.selection['candidates'].append(deepcopy(self.selection['candidates'][0]))
        with self.assertRaisesRegex(ModelError,'CANDIDATE_IDS_INVALID'): self.export()
        product = self.root / 'synthetic-product'
        (product / '.git').mkdir(parents=True)
        with self.assertRaisesRegex(ModelError,'BANK_INSIDE_GIT'):
            prepare_export(self.selection,'evaluation','0'*64,bank=product,company='fixture',audience='internal')


if __name__ == '__main__': unittest.main()
