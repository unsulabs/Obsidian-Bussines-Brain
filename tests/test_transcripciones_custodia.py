"""Synthetic custody negatives: exact bytes, separate identities, crash recovery."""
import copy
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import transcripciones_custodia as custody
from transcripciones_modelo import ModelError, json_bytes, load_json, sha256_bytes, validate_record, validate_bank_location


def capture(root, data=b"synthetic\r\n\x00\xff", *, account="account-a", meeting="meeting-a", attempt="attempt-a", completeness="unverified"):
    folder = root / "input" / account / meeting / attempt
    folder.mkdir(parents=True, exist_ok=True)
    manifest = {"schema_version": "capture-manifest.v1", "job_id": "run-a", "attempt_id": attempt,
        "account": {"id": account, "observed_identity": "Synthetic account"},
        "meeting": {"id": meeting, "url": "https://example.test/meeting", "title": "Synthetic"},
        "captured_at": "2026-11-04T12:00:00Z", "method": "ui-copy-transcript",
        "file": {"path": "original.txt", "size_bytes": len(data), "sha256": sha256_bytes(data)},
        "completeness": completeness, "evidence": {"beginning": "observed", "ending": "observed", "continuity": "observed", "gaps": [], "uncertainties": []}}
    (folder / "original.txt").write_bytes(data)
    path = folder / "capture-manifest.v1.json"
    path.write_bytes(json_bytes(manifest))
    return path


class CustodyTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        self.bank = self.root / "bank"

    def change(self, path, callback):
        data = load_json(path)
        callback(data)
        path.write_bytes(json_bytes(data))

    def test_dry_run_has_no_writes(self):
        path = capture(self.root)
        result = custody.register_capture(self.bank, path)
        self.assertFalse(result["evidence"]["committed"])
        self.assertFalse(self.bank.exists())

    def test_exact_binary_and_idempotence(self):
        data = b"\xef\xbb\xbfuno\r\n\x00\xfffin"
        path = capture(self.root, data)
        custody.register_capture(self.bank, path, commit=True)
        before = {p.relative_to(self.bank): p.read_bytes() for p in self.bank.rglob("*") if p.is_file()}
        result = custody.register_capture(self.bank, path, commit=True)
        self.assertTrue(result["evidence"]["idempotent"])
        self.assertEqual(next((self.bank / "originales").glob("*.bin")).read_bytes(), data)
        after = {p.relative_to(self.bank): p.read_bytes() for p in self.bank.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_same_bytes_do_not_merge_accounts_or_meetings(self):
        for account, meeting in [("account-a", "meeting-a"), ("account-b", "meeting-a"), ("account-a", "meeting-b")]:
            custody.register_capture(self.bank, capture(self.root, account=account, meeting=meeting), commit=True)
        rows = custody.load_catalog(self.bank)
        self.assertEqual(len(rows), 3)
        self.assertEqual(len({r["tr_id"] for r in rows}), 3)
        self.assertEqual(len(list((self.bank / "originales").glob("*.bin"))), 1)

    def test_versions_append_without_preferring_latest(self):
        first = custody.register_capture(self.bank, capture(self.root, b"old"), commit=True)
        original = next((self.bank / "versiones").glob("*.json"))
        before = original.read_bytes()
        custody.register_capture(self.bank, capture(self.root, b"new", attempt="attempt-b"), commit=True)
        row = custody.load_catalog(self.bank)[0]
        self.assertEqual(len(row["version_ids"]), 2)
        self.assertEqual(row["preferred_version_id"], first["evidence"]["version_id"])
        self.assertEqual(original.read_bytes(), before)

    def test_sealed_manifest_cannot_change(self):
        path = capture(self.root)
        custody.register_capture(self.bank, path, commit=True)
        self.change(path, lambda m: m["meeting"].update(title="changed"))
        with self.assertRaisesRegex(ModelError, "SEALED_CAPTURE_CHANGED"):
            custody.register_capture(self.bank, path, commit=True)

    def test_mismatch_does_not_write(self):
        path = capture(self.root)
        (path.parent / "original.txt").write_bytes(b"changed")
        with self.assertRaisesRegex(ModelError, "HASH_MISMATCH"):
            custody.register_capture(self.bank, path, commit=True)
        self.assertFalse(self.bank.exists())

    def test_partial_evidence_never_means_complete(self):
        path = capture(self.root, completeness="complete")
        self.change(path, lambda m: m["evidence"].update(continuity=""))
        with self.assertRaisesRegex(ModelError, "COMPLETENESS_UNPROVEN"):
            custody.register_capture(self.bank, path, commit=True)

    def test_empty_rejected(self):
        with self.assertRaises(ModelError):
            custody.register_capture(self.bank, capture(self.root, b""), commit=True)

    def test_inaccessible_preserved_not_downloaded(self):
        path = capture(self.root)
        self.change(path, lambda m: m.update(file=None, completeness="inaccessible", evidence={"beginning": "", "ending": "", "continuity": "", "gaps": ["provider unavailable"], "uncertainties": []}))
        custody.register_capture(self.bank, path, commit=True)
        row = custody.load_catalog(self.bank)[0]
        self.assertEqual(row["version_ids"], [])
        self.assertEqual(row["states"]["completeness"], "inaccesible")
        self.assertFalse((self.bank / "originales").exists())

    def test_traversal_and_symlink_rejected(self):
        path = capture(self.root)
        for unsafe in ("../original.txt", "/tmp/a", "a/../../x", "a//x"):
            self.change(path, lambda m: m["file"].update(path=unsafe))
            with self.assertRaisesRegex(ModelError, "UNSAFE_PATH"):
                custody.register_capture(self.bank, path, commit=True)
        self.change(path, lambda m: m["file"].update(path="link.txt"))
        (path.parent / "link.txt").symlink_to(path.parent / "original.txt")
        with self.assertRaisesRegex(ModelError, "UNSAFE_PATH"):
            custody.register_capture(self.bank, path, commit=True)

    def test_destination_symlink_rejected(self):
        path = capture(self.root)
        self.bank.mkdir()
        outside = self.root / "outside"
        outside.mkdir()
        (self.bank / "originales").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ModelError, "UNSAFE_PATH"):
            custody.register_capture(self.bank, path, commit=True)
        self.assertEqual(list(outside.iterdir()), [])

    def test_strict_schema_and_timestamp(self):
        path = capture(self.root)
        m = load_json(path)
        for bad in (dict(m, unexpected=True), dict(m, captured_at="not-a-date"), dict(m, captured_at="2026-11-04T12:00:00+01:00")):
            with self.assertRaisesRegex(ModelError, "SCHEMA_INVALID"):
                validate_record("capture-manifest", bad)
        m["account"]["extra"] = "no"
        with self.assertRaises(ModelError):
            validate_record("capture-manifest", m)

    def test_duplicate_json_keys_rejected(self):
        path = capture(self.root)
        path.write_text('{"schema_version":"capture-manifest.v1","schema_version":"x"}', encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ModelError, "INVALID_JSON"):
            custody.register_capture(self.bank, path)

    def test_recovery_after_blob_before_receipt(self):
        path = capture(self.root)
        real_write = custody.atomic_write
        def crash(bank, dest, data, **kwargs):
            if dest.startswith("versiones/"):
                raise RuntimeError("simulated power loss")
            return real_write(bank, dest, data, **kwargs)
        with patch.object(custody, "atomic_write", crash), self.assertRaises(RuntimeError):
            custody.register_capture(self.bank, path, commit=True)
        self.assertEqual(custody.load_catalog(self.bank), [])
        self.assertEqual(custody.recover_bank(self.bank)["evidence"]["recovered_transactions"], 1)
        self.assertEqual(len(custody.load_catalog(self.bank)), 1)
        self.assertTrue(custody.register_capture(self.bank, path, commit=True)["evidence"]["idempotent"])

    def test_corrupt_blob_not_repaired_or_acknowledged(self):
        path = capture(self.root)
        custody.register_capture(self.bank, path, commit=True)
        blob = next((self.bank / "originales").glob("*.bin"))
        blob.write_bytes(b"tamper")
        with self.assertRaisesRegex(ModelError, "HASH_MISMATCH"):
            custody.register_capture(self.bank, path, commit=True)
        self.assertEqual(blob.read_bytes(), b"tamper")

    def test_generic_monologue_preserves_unknown_completeness(self):
        path = capture(self.root, "monólogo literal\n".encode())
        self.change(path, lambda m: m.update(method="pasted-text", meeting={"id": "local-monologue-1", "url": None, "title": ""}))
        custody.register_capture(self.bank, path, commit=True)
        row = custody.load_catalog(self.bank)[0]
        self.assertEqual(row["occurrences"][0]["provider"], "local")
        self.assertEqual(row["states"]["completeness"], "desconocida")
        self.assertEqual(set(row["permission_record"].values()), {"desconocido"})

    def test_version_lineage_survives_clock_regression(self):
        with patch.object(custody, "utc_now", return_value="2026-11-04T12:00:00Z"):
            first = custody.register_capture(self.bank, capture(self.root, b"first"), commit=True)
        with patch.object(custody, "utc_now", return_value="2026-11-03T12:00:00Z"):
            second = custody.register_capture(self.bank, capture(self.root, b"second", attempt="attempt-b"), commit=True)
        row = custody.load_catalog(self.bank)[0]
        self.assertEqual(row["version_ids"], [first["evidence"]["version_id"], second["evidence"]["version_id"]])
        self.assertEqual(row["preferred_version_id"], first["evidence"]["version_id"])

    def test_original_metadata_tampering_detected_against_journal(self):
        path = capture(self.root)
        custody.register_capture(self.bank, path, commit=True)
        original = next((self.bank / "versiones").glob("*.json"))
        self.change(original, lambda m: m.update(captured_at="2026-11-01T12:00:00Z"))
        with self.assertRaisesRegex(ModelError, "HASH_MISMATCH"):
            custody.verify_bank(self.bank)

    def test_completed_journal_corruption_rejected_by_verify_and_recover(self):
        custody.register_capture(self.bank, capture(self.root), commit=True)
        journal = next((self.bank / "journal").glob("*.json"))
        self.change(journal, lambda tx: tx["entries"][0].update(bytes_b64="!!invalid!!"))
        for operation in (custody.verify_bank, custody.recover_bank):
            with self.assertRaisesRegex(ModelError, "JOURNAL_INVALID"):
                operation(self.bank)

    def test_recovery_rejects_corrupt_committed_blob(self):
        custody.register_capture(self.bank, capture(self.root), commit=True)
        next((self.bank / "originales").glob("*.bin")).write_bytes(b"corrupt")
        with self.assertRaisesRegex(ModelError, "HASH_MISMATCH"):
            custody.recover_bank(self.bank)

    def test_utc_offset_zero_is_valid(self):
        path = capture(self.root)
        self.change(path, lambda m: m.update(captured_at="2026-11-04T06:35:22.821295+00:00"))
        custody.register_capture(self.bank, path, commit=True)
        self.assertEqual(len(custody.load_catalog(self.bank)), 1)

    def test_git_location_rejected_by_api_even_in_preview(self):
        repo = self.root / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        bank = repo / "new/nested/bank"
        path = capture(self.root)
        for commit in (False, True):
            with self.assertRaisesRegex(ModelError, "BANK_INSIDE_GIT"):
                custody.register_capture(bank, path, commit=commit)
        with self.assertRaisesRegex(ModelError, "BANK_INSIDE_GIT"):
            custody.recover_bank(bank)
        self.assertFalse(bank.exists())
        # A sibling repository does not make its entire parent private area Git.
        self.assertEqual(validate_bank_location(self.bank), self.bank)

    def test_vault_marker_and_explicit_uninitialized_vault_rejected(self):
        vault = self.root / "vault"
        with self.assertRaisesRegex(ModelError, "BANK_INSIDE_VAULT"):
            validate_bank_location(vault / "bank", vault=vault)
        (vault / ".obsidian").mkdir(parents=True)
        with self.assertRaisesRegex(ModelError, "BANK_INSIDE_VAULT"):
            custody.register_capture(vault / "nested/bank", capture(self.root))
        self.assertFalse((vault / "nested").exists())


if __name__ == "__main__":
    unittest.main()
