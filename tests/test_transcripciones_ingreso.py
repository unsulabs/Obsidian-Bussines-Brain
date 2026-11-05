import json
from pathlib import Path
import sys
import tempfile
import subprocess
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from transcripciones_ingreso import ingest, read_parts_manifest
from transcripciones_custodia import load_catalog, verify_bank
from transcripciones_modelo import ModelError, sha256_bytes
import transcripciones_ingreso as ingreso


class IngresoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.bank = self.root / "bank"
        self.kw = dict(job_id="job-1", account_id="local-user", source_id="source-1", attempt_id="a1")

    def tearDown(self):
        self.temp.cleanup()

    def receive(self, **kwargs):
        return ingest(self.bank, **dict(self.kw, **kwargs))

    def test_preview_does_not_write(self):
        self.receive(parts=[(1, b"unmodified\r\n")])
        self.assertFalse(self.bank.exists())

    def test_order_exact_bytes_and_unknown_metadata(self):
        self.receive(parts=[(2, b"second\n"), (1, b"first\r\n")], expected_parts=2, closed=True, commit=True)
        original = b"first\r\nsecond\n"
        self.assertEqual((self.bank / "originales" / (sha256_bytes(original) + ".bin")).read_bytes(), original)
        row = load_catalog(self.bank)[0]
        self.assertEqual(row["states"]["completeness"], "completa_comprobada")
        self.assertIsNone(row["event_time"])
        self.assertEqual(row["speaker_labels"], [])
        self.assertEqual(row["title_reported"], "")
        assembly = json.loads(next(self.bank.rglob("assembly-manifest.v1.json")).read_bytes())
        self.assertEqual([x["number"] for x in assembly["parts"]], [1, 2])
        self.assertEqual(verify_bank(self.bank)["evidence"]["versions"], 1)

    def test_missing_part_never_complete_even_closed(self):
        out = self.receive(parts=[(1, b"a"), (3, b"c")], expected_parts=3, closed=True, commit=True)
        self.assertEqual(out["evidence"]["missing_parts"], [2])
        self.assertEqual(load_catalog(self.bank)[0]["states"]["completeness"], "parcial")

    def test_open_or_unknown_total_never_complete(self):
        for closed, expected in ((False, 1), (True, None)):
            out = self.receive(parts=[(1, b"a")], closed=closed, expected_parts=expected)
            self.assertEqual(out["evidence"]["completeness"], "partial")

    def test_replay_and_immutable_conflict(self):
        args = dict(parts=[(1, b"a")], commit=True)
        self.receive(**args)
        self.assertTrue(self.receive(**args)["evidence"]["idempotent"])
        with self.assertRaises(ModelError):
            self.receive(parts=[(1, b"changed")], commit=True)
        self.assertEqual(len(load_catalog(self.bank)[0]["version_ids"]), 1)

    def test_invalid_parts_no_write(self):
        for parts in ([], [(1, b"")], [(1, b"a"), (1, b"b")], [(0, b"a")]):
            with self.assertRaises(ModelError):
                self.receive(parts=parts, commit=True)
        self.assertFalse(self.bank.exists())

    def test_escape_and_symlink_rejected(self):
        outside = self.root / "outside.txt"
        outside.write_bytes(b"synthetic")
        folder = self.root / "input"
        folder.mkdir()
        (folder / "link.txt").symlink_to(outside)
        for path in ("../outside.txt", "link.txt"):
            descriptor = folder / "parts.json"
            descriptor.write_text(json.dumps({"parts": [{"number": 1, "path": path}], "expected_parts": 1, "closed": True}), encoding='utf-8', newline='\n')
            with self.assertRaises(ModelError):
                read_parts_manifest(descriptor)

    def test_public_api_rejects_git_and_vault_even_preview(self):
        repo = self.root / "repo"
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        vault = self.root / "vault"
        (vault / ".obsidian").mkdir(parents=True)
        for bank in (repo / "bank", vault, vault / "bank"):
            with self.subTest(bank=bank), self.assertRaises(ModelError):
                ingest(bank, **self.kw, parts=[(1, b"synthetic")])
        # The project root containing a product checkout is not itself a repo.
        out = self.receive(parts=[(1, b"synthetic")])
        self.assertFalse(out["evidence"]["committed"])
        self.assertFalse(self.bank.exists())

    def test_retry_after_interrupted_delivery_does_not_expose_catalog(self):
        write = ingreso.atomic_write
        count = 0
        def interrupted(*args, **kwargs):
            nonlocal count
            count += 1
            if count == 2:
                raise OSError("Synthetic interruption")
            return write(*args, **kwargs)
        kwargs = dict(parts=[(1, b"first"), (2, b"second")], closed=True, expected_parts=2, commit=True)
        with patch.object(ingreso, "atomic_write", side_effect=interrupted), self.assertRaises(OSError):
            self.receive(**kwargs)
        self.assertEqual(load_catalog(self.bank), [])
        self.assertFalse(list(self.bank.rglob("capture-manifest.v1.json")))
        self.assertTrue(self.receive(**kwargs)["evidence"]["committed"])
        self.assertEqual(len(load_catalog(self.bank)), 1)


if __name__ == "__main__":
    unittest.main()
