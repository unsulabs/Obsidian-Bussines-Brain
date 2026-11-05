"""Request memo scale and byte-exact invalidation; entirely synthetic banks."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import test_transcripciones_recuperacion as retrieval_fixtures
from test_transcripciones_custodia import capture
from transcripciones_custodia import register_capture
from transcripciones_contexto import build_context
from transcripciones_indice import search
from transcripciones_lectura import _active
from transcripciones_modelo import ModelError


class RequestReadTests(unittest.TestCase):
    def setUp(self):
        self.fixture = retrieval_fixtures.RetrievalTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.decision()
        self.bank, self.access = self.fixture.bank, self.fixture.access

    def query(self):
        return build_context(self.bank, 'criterio', **self.access)

    def test_scale_validates_catalog_and_ledger_once_per_request(self):
        import transcripciones_custodia as custody
        import transcripciones_permisos as rights
        for index in range(20):
            added = register_capture(self.bank, capture(self.fixture.root,
                (f'criterio sintetico {index} ' * 600).encode(), meeting=f'scale-{index}'), commit=True)['evidence']
            self.fixture.decision(tr_id=added['tr_id'], version_id=added['version_id'])
        original = rights.validate_record
        validations = []
        def counted(kind, *args, **kwargs):
            validations.append(kind)
            return original(kind, *args, **kwargs)
        with patch.object(custody, '_load_catalog', wraps=custody._load_catalog) as catalog, \
                patch.object(rights, 'validate_record', counted):
            first = self.query()
            self.assertEqual(catalog.call_count, 1)
            self.assertEqual(validations.count('permiso'), 21)
            second = self.query()
            self.assertEqual(catalog.call_count, 2)
            self.assertEqual(validations.count('permiso'), 42)
        self.assertEqual(first, second)
        self.assertEqual(len(first['candidates']), 10)
        self.assertIsNone(_active.get())

    def test_revocation_during_search_never_returns_cached_grant(self):
        changed = False
        def revoke(candidate):
            nonlocal changed
            if not changed:
                changed = True
                self.fixture.decision('revoke')
            return [candidate]
        with self.assertRaisesRegex(ModelError, 'SNAPSHOT_CHANGED'):
            search(self.bank, 'criterio', **self.access, candidate_filter=revoke)
        self.assertIsNone(_active.get())
        self.assertEqual(self.query()['candidates'], [])

    def test_multiple_writes_inside_request_use_live_ledger(self):
        changed = False
        def mutate(candidate):
            nonlocal changed
            if not changed:
                changed = True
                self.fixture.decision('revoke')
                self.fixture.decision('grant')
            return [candidate]
        with self.assertRaisesRegex(ModelError, 'SNAPSHOT_CHANGED'):
            search(self.bank, 'criterio', **self.access, candidate_filter=mutate)
        self.assertTrue(self.query()['candidates'])
        self.assertEqual(len(list((self.bank/'permissions').glob('*.json'))), 3)

    def test_same_length_original_mutation_rejected(self):
        blob = next((self.bank/'originales').glob('*.bin'))
        before = blob.read_bytes()
        def mutate(candidate):
            blob.write_bytes(b'X' * len(before))
            return [candidate]
        with self.assertRaisesRegex(ModelError, 'SNAPSHOT_CHANGED'):
            search(self.bank, 'criterio', **self.access, candidate_filter=mutate)
        self.assertIsNone(_active.get())
        with self.assertRaisesRegex(ModelError, 'HASH_MISMATCH'):
            self.query()

    def test_added_analysis_rejected_even_if_no_original_changed(self):
        def mutate(candidate):
            (self.bank/'analisis').mkdir(exist_ok=True)
            (self.bank/'analisis'/'new.json').write_text('{}')
            return [candidate]
        with self.assertRaisesRegex(ModelError, 'SNAPSHOT_CHANGED'):
            search(self.bank, 'criterio', **self.access, candidate_filter=mutate)

    def test_failed_query_discards_cache_and_next_request_checks_corruption(self):
        with self.assertRaises(ModelError):
            build_context(self.bank, 'criterio', **self.access, mode='invalid')
        self.assertIsNone(_active.get())
        self.assertTrue(self.query()['candidates'])
        ledger = next((self.bank/'permissions').glob('*.json'))
        ledger.write_text('{}')
        with self.assertRaises(ModelError):
            self.query()

    def test_utf8_cache_uses_exact_bytes_and_still_checks_hashes_and_offsets(self):
        import transcripciones_analisis as analysis
        from transcripciones_lectura import guarded_read
        from transcripciones_modelo import sha256_bytes
        @guarded_read
        def exercise(bank):
            for data in ('aé'.encode(), 'aé'.encode(), b'abc'):
                span = dict(tr_id='TR-test', version_id='V-test', text_sha256=sha256_bytes(data),
                            start=0, end=len(data), excerpt_sha256=sha256_bytes(data))
                self.assertTrue(analysis.validate_span(span, {('TR-test', 'V-test'): data}))
            span['text_sha256'] = sha256_bytes(b'wrong')
            with self.assertRaisesRegex(ModelError, 'SOURCE_CHANGED'):
                analysis.validate_span(span, {('TR-test', 'V-test'): b'abc'})
            data = 'aé'.encode()
            span.update(text_sha256=sha256_bytes(data), start=2, end=3)
            with self.assertRaisesRegex(ModelError, 'OFFSET_INVALID'):
                analysis.validate_span(span, {('TR-test', 'V-test'): data})
        with patch.object(analysis, 'boundaries', wraps=analysis.boundaries) as bounds:
            exercise(self.bank)
            self.assertEqual(bounds.call_count, 2)
            exercise(self.bank)
            self.assertEqual(bounds.call_count, 4)


if __name__ == '__main__':
    unittest.main()
