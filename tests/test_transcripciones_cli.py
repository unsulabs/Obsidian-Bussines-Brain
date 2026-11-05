import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CLI = Path(__file__).resolve().parents[1] / "scripts" / "transcripciones.py"


class CLITests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.bank = self.root / "bank"
        self.profile = self.root / "profile.json"
        self.profile.write_text(json.dumps({"company_id": "synthetic", "allowed_purposes": ["custody"], "bank": str(self.bank)}))

    def tearDown(self):
        self.temp.cleanup()

    def run_cli(self, command, *options, data=None, purpose="custody"):
        run = subprocess.run([sys.executable, str(CLI), command, "--bank", str(self.bank), "--profile", str(self.profile),
                              "--purpose", purpose, "--request-id", "request-1", *options], input=data, capture_output=True)
        self.assertEqual(run.stderr, b"", run.stderr)
        return run.returncode, json.loads(run.stdout)

    def test_stdin_to_bank_and_readonly_status(self):
        flags = ["--stdin", "--account-id", "local", "--source-id", "s1", "--attempt-id", "a1", "--closed", "--expected-parts", "1"]
        code, out = self.run_cli("ingresar", *flags, data=b"exact\r\nbytes\n")
        self.assertEqual(code, 0)
        self.assertFalse(self.bank.exists())
        code, out = self.run_cli("ingresar", *flags, "--commit", data=b"exact\r\nbytes\n")
        self.assertEqual(code, 0, out)
        self.assertTrue(out["evidence"]["committed"])
        self.assertNotIn("exact", json.dumps(out))
        before = {p.relative_to(self.bank): p.read_bytes() for p in self.bank.rglob("*") if p.is_file()}
        self.assertEqual(self.run_cli("estado")[1]["evidence"]["transcriptions"], 1)
        self.assertEqual(self.run_cli("verificar")[1]["evidence"]["versions"], 1)
        self.assertEqual(before, {p.relative_to(self.bank): p.read_bytes() for p in self.bank.rglob("*") if p.is_file()})

    def test_file_and_manifest_registration(self):
        source = self.root / "source.txt"
        source.write_bytes(b"synthetic file")
        code, out = self.run_cli("ingresar", "--archivo", str(source), "--account-id", "local", "--source-id", "s1", "--attempt-id", "a1", "--commit")
        self.assertEqual(code, 0, out)
        receipt = next(self.bank.rglob("capture-manifest.v1.json"))
        code, out = self.run_cli("registrar", "--capture-manifest", str(receipt), "--commit")
        self.assertEqual(code, 0, out)
        self.assertTrue(out["evidence"]["idempotent"])

    def test_denied_purpose_and_report_collision(self):
        code, out = self.run_cli("estado", purpose="training")
        self.assertEqual(code, 2)
        self.assertEqual(out["errors"][0]["code"], "PURPOSE_DENIED")
        report = self.root / "report.json"
        report.write_text("keep")
        code, out = self.run_cli("estado", "--output", str(report))
        self.assertEqual(code, 2)
        self.assertEqual(report.read_text(), "keep")
        self.assertFalse(self.bank.exists())

    def test_no_future_commands_advertised(self):
        run = subprocess.run([sys.executable, str(CLI), "--help"], capture_output=True)
        self.assertEqual(run.returncode, 0)
        self.assertNotIn(b"preparar-ficha", run.stdout)
        self.assertIn(b"segmentar", run.stdout)
        self.assertIn(b"conciliar", run.stdout)

    def test_inventory_reconcile_and_multipart_cli(self):
        from test_transcripciones_inventario import inventory
        snapshot = inventory()
        snapshot["account"]["id"] = "local"
        snapshot["meetings"][0]["id"] = "s1"
        path = self.root / "inventory.json"
        path.write_text(json.dumps(snapshot))
        self.assertTrue(self.run_cli("inventario-validar", "--snapshot", str(path))[1]["evidence"]["valid"])
        self.assertFalse(self.run_cli("conciliar", "--snapshot", str(path))[1]["evidence"]["download_complete"])
        (self.root / "first.txt").write_bytes(b"first\n")
        (self.root / "second.txt").write_bytes(b"second\n")
        parts = self.root / "parts.json"
        parts.write_text(json.dumps({"parts": [{"number": 2, "path": "second.txt"}, {"number": 1, "path": "first.txt"}], "expected_parts": 2, "closed": True}))
        code, out = self.run_cli("ingresar", "--parts-manifest", str(parts), "--account-id", "local", "--source-id", "s1", "--attempt-id", "a1", "--commit")
        self.assertEqual(code, 0, out)
        report = self.root / "result.json"
        code, out = self.run_cli("conciliar", "--snapshot", str(path), "--output", str(report))
        self.assertEqual(code, 0, out)
        self.assertTrue(out["evidence"]["download_complete"])
        self.assertEqual(json.loads(report.read_text()), out)

    def test_analysis_cli_and_private_context_output(self):
        from test_transcripciones_pipeline import PipelineTests
        fixture = PipelineTests()
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        self.bank = fixture.bank
        self.profile.write_text(json.dumps({"company_id": "synthetic", "allowed_purposes": ["custody", "local_analysis", "internal_query"], "bank": str(self.bank)}))
        submission = fixture.submission()
        path = self.root / "submission.json"
        path.write_text(json.dumps(submission))
        code, out = self.run_cli("analizar", "--input", str(path), "--audience", "internal", "--commit", purpose="local_analysis")
        self.assertEqual(code, 0, out)
        code, out = self.run_cli("cobertura", "--tr-id", fixture.tr, "--run", "RUN-fixture", "--audience", "internal", purpose="local_analysis")
        self.assertEqual(code, 0, out)
        self.assertFalse(out["evidence"]["ratified"])
        query = self.root / "query.json"
        query.write_text(json.dumps({"query": "descuentos", "company": "synthetic", "audience": "internal", "purpose": "internal_query"}))
        code, out = self.run_cli("buscar", "--request", str(query), purpose="internal_query")
        self.assertEqual(out["errors"][0]["code"], "PRIVATE_OUTPUT_REQUIRED")
        destination = self.root / "context.json"
        code, out = self.run_cli("buscar", "--request", str(query), "--output", str(destination), purpose="internal_query")
        self.assertEqual(code, 0, out)
        self.assertNotIn("descuentos", json.dumps(out))
        self.assertGreater(out["evidence"]["candidate_count"], 0)
        package = json.loads(destination.read_text())["evidence"]["context"]
        self.assertIn("descuentos", json.dumps(package))
        self.assertTrue(package["abstention"])
        code, out = self.run_cli("indexar", "--snapshot", "current", "--audience", "internal", purpose="local_analysis")
        self.assertEqual(code, 0, out)
        self.assertFalse(out["evidence"]["committed"])

    def test_search_report_cannot_enter_git(self):
        repo = self.root / "product"
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        self.profile.write_text(json.dumps({"company_id": "synthetic", "allowed_purposes": ["internal_query"], "bank": str(self.bank)}))
        query = self.root / "query.json"
        query.write_text(json.dumps({"query": "secret", "company": "synthetic", "audience": "internal", "purpose": "internal_query"}))
        output = repo / "context.json"
        code, out = self.run_cli("buscar", "--request", str(query), "--output", str(output), purpose="internal_query")
        self.assertEqual(code, 2)
        self.assertEqual(out["errors"][0]["code"], "BANK_INSIDE_GIT")
        self.assertFalse(output.exists())

    def test_search_request_fields_roundtrip_filters_and_history(self):
        from test_transcripciones_pipeline import PipelineTests
        from transcripciones_pipeline import consolidate_analysis, review_snapshot, review_history
        fixture = PipelineTests(); fixture.setUp()
        self.addCleanup(fixture.tearDown)
        self.bank = fixture.bank
        self.profile.write_text(json.dumps({"company_id": "synthetic", "allowed_purposes": ["internal_query"], "bank": str(self.bank)}))
        first = fixture.submission()
        first["global_reconciliation"]["open_conflicts"] = ["OLD-PRIVATE-CONFLICT"]
        for claim in first["claims"]:
            claim["validity_state"] = "vigente"
        consolidate_analysis(self.bank, first, **fixture.scope, commit=True)
        mapping = {"RUN-fixture": "RUN-second", **{c["claim_id"]: "NEW-" + c["claim_id"] for c in first["claims"]}}
        def remap(value):
            if isinstance(value, str): return mapping.get(value, value)
            if isinstance(value, dict): return {k: remap(v) for k, v in value.items()}
            if isinstance(value, list): return [remap(v) for v in value]
            return value
        newer = remap(first)
        newer["supersedes_run_id"] = "RUN-fixture"
        newer["global_reconciliation"]["open_conflicts"] = []
        consolidate_analysis(self.bank, newer, **fixture.scope, commit=True)
        base = {"query": "descuentos", "company": "synthetic", "audience": "internal", "purpose": "internal_query",
                "task": "PRIVATE TASK: inspect approved scope", "entities": [], "period": None, "mode": "actual"}
        counter = 0
        def search(**changes):
            nonlocal counter
            counter += 1
            request = dict(base, **changes)
            path = self.root / f"request-{counter}.json"
            output = self.root / f"context-{counter}.json"
            path.write_text(json.dumps(request))
            code, stdout = self.run_cli("buscar", "--request", str(path), "--output", str(output), purpose="internal_query")
            self.assertNotIn("PRIVATE TASK", json.dumps(stdout))
            self.assertNotIn("descuentos", json.dumps(stdout))
            self.assertNotIn("OLD-PRIVATE-CONFLICT", json.dumps(stdout))
            return code, stdout, json.loads(output.read_text())
        code, _, report = search()
        self.assertEqual(code, 0, report)
        current = report["evidence"]["context"]
        self.assertEqual(current["task"], base["task"])
        self.assertEqual(current["mode"], "actual")
        self.assertIn("engine_mode", current)
        self.assertNotIn("RUN-fixture", [r["run_id"] for r in current["analyses"]])
        self.assertIn("RUN-second", [r["run_id"] for r in current["analyses"]])
        code, _, report = search(entities=["PERSON-nonexistent"])
        self.assertEqual(code, 0, report)
        self.assertEqual(report["evidence"]["context"]["entities"], ["PERSON-nonexistent"])
        self.assertEqual(report["evidence"]["context"]["candidates"], [])
        self.assertEqual(report["evidence"]["context"]["analyses"], [])
        period = {"from": "1900-01-01", "to": "1900-12-31"}
        code, _, report = search(period=period)
        self.assertEqual(code, 0, report)
        self.assertEqual(report["evidence"]["context"]["period"], period)
        self.assertEqual(report["evidence"]["context"]["candidates"], [])
        self.assertEqual(report["evidence"]["context"]["analyses"], [])
        code, _, report = search(mode="historico")
        self.assertEqual(code, 0, report)
        self.assertIn("RUN-fixture", [r["run_id"] for r in report["evidence"]["context"]["analyses"]])
        snapshot = review_snapshot(self.bank, **fixture.scope)
        review_history(self.bank, fixture.event(snapshot["snapshot_id"]), snapshot["snapshot_id"], **fixture.scope, commit=True)
        code, _, report = search(mode="historico")
        self.assertEqual(code, 0, report)
        self.assertNotIn("RUN-fixture", [r["run_id"] for r in report["evidence"]["context"]["analyses"]])
        self.assertNotIn("OLD-PRIVATE-CONFLICT", json.dumps(report))
        for changes in ({"unknown": "must reject"}, {"mode": "invented"}, {"entities": "not-list"},
                        {"period": {"from": "1901-01-01", "to": "1900-01-01"}}):
            code, stdout, _ = search(**changes)
            self.assertEqual(code, 2, stdout)
            self.assertTrue(stdout["errors"])

    def test_profile_bank_mismatch(self):
        self.profile.write_text(json.dumps({"company_id": "synthetic", "allowed_purposes": ["custody"], "bank": str(self.root / "other")}))
        code, out = self.run_cli("estado")
        self.assertEqual(code, 2)
        self.assertEqual(out["errors"][0]["code"], "BANK_PROFILE_MISMATCH")
        self.assertFalse(self.bank.exists())

    def test_equivalent_relative_bank_and_symlink_rejection(self):
        actual = self.bank
        # cwd is the product checkout; the bank is outside, reached through .. .
        self.bank = Path(os.path.relpath(actual, Path.cwd()))
        code, out = self.run_cli("estado")
        self.assertEqual(code, 0, out)
        link = self.root / "linked-bank"
        actual.mkdir()
        link.symlink_to(actual, target_is_directory=True)
        self.bank = link
        code, out = self.run_cli("estado")
        self.assertEqual(code, 2, out)
        self.assertEqual(out["errors"][0]["code"], "UNSAFE_PATH")
        self.bank = actual
        self.profile.write_text(json.dumps({"company_id": "synthetic", "allowed_purposes": ["custody"], "bank": str(link)}))
        code, out = self.run_cli("estado")
        self.assertEqual(code, 2, out)
        self.assertEqual(out["errors"][0]["code"], "UNSAFE_PATH")

    def test_blocked_report_is_written_without_overwriting_existing(self):
        report = self.root / "blocked.json"
        code, out = self.run_cli("estado", "--output", str(report), purpose="denied")
        self.assertEqual(code, 2)
        self.assertEqual(out["status"], "BLOCKED")
        self.assertEqual(json.loads(report.read_text()), out)
        prior = report.read_bytes()
        self.run_cli("estado", "--output", str(report), purpose="other")
        self.assertEqual(report.read_bytes(), prior)

    def test_git_and_vault_boundaries(self):
        repo = self.root / "repo"
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        vault = self.root / "vault"
        (vault / ".obsidian").mkdir(parents=True)
        explicit = self.root / "unopened-vault"
        for bank, declared_vault in ((repo / "bank", None), (vault, None), (vault / "bank", None),
                                     (explicit, explicit), (explicit / "bank", explicit)):
            self.bank = bank
            profile = {"company_id": "synthetic", "allowed_purposes": ["custody"], "bank": str(bank)}
            if declared_vault:
                profile["vault"] = str(declared_vault)
            self.profile.write_text(json.dumps(profile))
            code, out = self.run_cli("estado")
            self.assertEqual(code, 2, out)
            self.assertIn(out["errors"][0]["code"], ("BANK_INSIDE_GIT", "BANK_INSIDE_VAULT"))


if __name__ == "__main__":
    unittest.main()
