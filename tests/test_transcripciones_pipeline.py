"""Synthetic custody → explicit rights → portable analysis → live context."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from transcripciones_modelo import ModelError, load_json, safe_path, utc_now
from transcripciones_ingreso import ingest
from transcripciones_permisos import record_decision, permission_snapshot
from transcripciones_pipeline import (segment_capture, consolidate_analysis, coverage_report,
    store_taxonomy, review_snapshot, review_history)
from transcripciones_taxonomia import seed_taxonomy
from transcripciones_contexto import build_context
from test_transcripciones_analisis import fixture


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.bank = Path(self.temp.name).resolve() / "bank"
        self.scope = dict(company="synthetic", audience="internal", purpose="local_analysis")
        self.authored = fixture()
        receipt = ingest(self.bank, job_id="J1", account_id="local", source_id="S1", attempt_id="A1",
                         parts=[(1, self.authored["data"])], expected_parts=1, closed=True, commit=True)
        self.tr = receipt["evidence"]["tr_id"]
        self.vid = receipt["evidence"]["version_id"]
        self.grant("local_analysis")
        self.grant("internal_query")
        store_taxonomy(self.bank, seed_taxonomy(), commit=True)

    def tearDown(self):
        self.temp.cleanup()

    def grant(self, purpose, action="grant"):
        return record_decision(self.bank, dict(tr_id=self.tr, version_id=self.vid, company="synthetic", audience="internal",
            purpose=purpose, action=action, authority="Synthetic fixture owner", evidence=["Synthetic test authorization"], decided_at=utc_now()), commit=True)

    def snapshot_bytes(self):
        return {str(p.relative_to(self.bank)): p.read_bytes() for p in self.bank.rglob("*") if p.is_file()}

    def submission(self):
        result = segment_capture(self.bank, self.tr, self.vid, **self.scope, max_core_bytes=128, commit=True)
        bundle_id = result["evidence"]["bundle_id"]
        segments = load_json(safe_path(self.bank, result["outputs"][0]["path"]))["segments"]
        mapping = {"TR-synthetic": self.tr, "V-1": self.vid}
        mapping.update({old["segment_id"]: new["segment_id"] for old, new in zip(self.authored["segments"], segments)})
        def replace(item):
            if isinstance(item, str): return mapping.get(item, item)
            if isinstance(item, list): return [replace(x) for x in item]
            if isinstance(item, dict): return {k: replace(v) for k,v in item.items()}
            return item
        args = replace(self.authored)
        keys = ("agent_results", "claims", "relations", "subject_matrix", "global_reconciliation", "analyzer_version", "taxonomy_version", "run_id")
        return {**{k: args[k] for k in keys}, "tr_id": self.tr, "version_id": self.vid,
                "segment_bundle": bundle_id, "permission_snapshot": permission_snapshot(self.bank, source_refs=[(self.tr, self.vid)], **self.scope),
                "canonical_context_refs": [], "supersedes_run_id": None, "dependency_ids": []}

    def event(self, snapshot, **overrides):
        return dict(schema_version="evento.v1", created_at="2026-11-04T00:00:00Z", producer_version="test",
                    event_id="EV-1", event_type="correccion", old_refs=["RUN-fixture"], new_refs=[],
                    reason="Synthetic correction requires review", actor="synthetic", affected_ids=[],
                    sweep_snapshot=snapshot, jobs=[], **overrides)

    def test_end_to_end_agent_bundle_and_no_semantic_ratification(self):
        submission = self.submission()
        before = self.snapshot_bytes()
        preview = consolidate_analysis(self.bank, submission, **self.scope)
        self.assertFalse(preview["evidence"]["committed"])
        self.assertEqual(before, self.snapshot_bytes())
        committed = consolidate_analysis(self.bank, submission, **self.scope, commit=True)
        self.assertTrue(committed["evidence"]["committed"])
        self.assertTrue(consolidate_analysis(self.bank, submission, **self.scope, commit=True)["evidence"]["idempotent"])
        report = coverage_report(self.bank, self.tr, "RUN-fixture", **self.scope)
        self.assertTrue(report["evidence"]["current"])
        self.assertFalse(report["evidence"]["ratified"])
        context = build_context(self.bank, "descuentos", company="synthetic", audience="internal")
        self.assertTrue(context["candidates"])
        self.assertTrue(context["abstention"])
        self.assertFalse(context["semantic_answer_generated"])

    def test_no_permissions_even_cached_and_corrupt_original(self):
        submission = self.submission()
        consolidate_analysis(self.bank, submission, **self.scope, commit=True)
        self.grant("local_analysis", "revoke")
        with self.assertRaises(ModelError):
            consolidate_analysis(self.bank, submission, **self.scope, commit=True)
        with self.assertRaises(ModelError):
            segment_capture(self.bank, self.tr, self.vid, **self.scope, commit=True)
        with self.assertRaises(ModelError):
            coverage_report(self.bank, self.tr, "RUN-fixture", **self.scope)
        self.grant("internal_query", "revoke")
        self.assertEqual(build_context(self.bank, "descuentos", company="synthetic", audience="internal")["candidates"], [])
        self.grant("local_analysis")
        blob = next((self.bank / "originales").glob("*.bin"))
        blob.write_bytes(b"tampered")
        with self.assertRaises(ModelError):
            segment_capture(self.bank, self.tr, self.vid, **self.scope)

    def test_no_writes_on_incomplete_semantics_and_stale_permission(self):
        submission = self.submission()
        before = self.snapshot_bytes()
        bad = deepcopy(submission); bad["agent_results"].pop()
        with self.assertRaises(ModelError):
            consolidate_analysis(self.bank, bad, **self.scope, commit=True)
        self.assertEqual(before, self.snapshot_bytes())
        bad = deepcopy(submission); bad["claims"][0]["editorial_state"] = "ratificado"
        with self.assertRaises(ModelError):
            consolidate_analysis(self.bank, bad, **self.scope, commit=True)
        self.grant("local_analysis", "revoke"); self.grant("local_analysis")
        with self.assertRaisesRegex(ModelError, "PERMISSION_SNAPSHOT_STALE|SEGMENT_SCOPE_STALE"):
            consolidate_analysis(self.bank, submission, **self.scope)

    def test_snapshot_permissions_resume_and_invalidation(self):
        submission = self.submission()
        consolidate_analysis(self.bank, submission, **self.scope, commit=True)
        snapshot = review_snapshot(self.bank, **self.scope)
        event = self.event(snapshot["snapshot_id"])
        before = self.snapshot_bytes()
        preview = review_history(self.bank, event, snapshot["snapshot_id"], **self.scope)
        self.assertEqual(before, self.snapshot_bytes())
        self.assertFalse(preview["evidence"]["complete"])
        report = review_history(self.bank, event, snapshot["snapshot_id"], **self.scope, commit=True)
        self.assertFalse(coverage_report(self.bank, self.tr, "RUN-fixture", **self.scope)["evidence"]["current"])
        bundle = load_json(safe_path(self.bank, report["outputs"][0]["path"]))
        job = bundle["plan"]["jobs"][0]
        delivered = {k: job[k] for k in ("job_id", "input_hash", "attempt", "tr_id")}
        delivered.update(state="reviewed", reason="Synthetic agent inspected all versions; correction stays proposed",
                         reviewed_version_ids=job["version_ids"], relations=[], proposals=[])
        complete = review_history(self.bank, event, snapshot["snapshot_id"], **self.scope,
                                  results=[delivered], previous_path=report["outputs"][0]["path"], commit=True)
        self.assertTrue(complete["evidence"]["complete"])
        self.grant("local_analysis", "revoke")
        with self.assertRaisesRegex(ModelError, "SNAPSHOT_CHANGED"):
            review_history(self.bank, event, snapshot["snapshot_id"], **self.scope, results=[delivered], commit=True)

    def test_segment_cache_is_idempotent_and_wrong_scope_denied(self):
        first = segment_capture(self.bank, self.tr, self.vid, **self.scope, commit=True)
        again = segment_capture(self.bank, self.tr, self.vid, **self.scope, commit=True)
        self.assertEqual(first["outputs"], again["outputs"])
        self.assertTrue(again["evidence"]["idempotent"])
        with self.assertRaisesRegex(ModelError, "SOURCE_PERMISSION_DENIED"):
            segment_capture(self.bank, self.tr, self.vid, company="other", audience="internal")

    def test_historical_claim_reference_requires_verified_prior_run(self):
        first = self.submission()
        first["global_reconciliation"]["open_conflicts"] = ["OLD-ONLY-CONFLICT"]
        consolidate_analysis(self.bank, first, **self.scope, commit=True)
        mapping = {"RUN-fixture": "RUN-second", **{c["claim_id"]: "NEW-" + c["claim_id"] for c in first["claims"]}}
        def replace(value):
            if isinstance(value, str): return mapping.get(value, value)
            if isinstance(value, list): return [replace(v) for v in value]
            if isinstance(value, dict): return {k: replace(v) for k,v in value.items()}
            return value
        updated = replace(first)
        updated["global_reconciliation"]["open_conflicts"] = []
        updated["supersedes_run_id"] = "RUN-fixture"
        updated["claims"][0]["supersedes_claim_id"] = first["claims"][0]["claim_id"]
        consolidated = consolidate_analysis(self.bank, updated, **self.scope, commit=True)
        self.assertTrue(consolidated["evidence"]["committed"])
        self.assertTrue(coverage_report(self.bank, self.tr, "RUN-second", **self.scope)["evidence"]["current"])
        prior = coverage_report(self.bank, self.tr, "RUN-fixture", **self.scope)
        self.assertFalse(prior["evidence"]["current"])
        self.assertTrue(prior["evidence"]["dependency_current"])
        self.assertEqual(prior["evidence"]["stale_reasons"], ["superseded"])
        self.assertEqual(prior["evidence"]["superseded_by"], ["RUN-second"])
        self.assertTrue((self.bank / "analisis/RUN-fixture.json").exists())
        context = build_context(self.bank, "descuentos", company="synthetic", audience="internal")
        self.assertNotIn("RUN-fixture", [r["run_id"] for r in context.get("analyses", [])])
        self.assertIn("RUN-second", [r["run_id"] for r in context["analyses"]])
        self.assertNotIn("OLD-ONLY-CONFLICT", json.dumps(context))
        forged = deepcopy(updated)
        forged["run_id"] = "RUN-third"
        forged["supersedes_run_id"] = "RUN-missing"
        with self.assertRaises(ModelError):
            consolidate_analysis(self.bank, forged, **self.scope, commit=True)
        snapshot = review_snapshot(self.bank, **self.scope)
        review_history(self.bank, self.event(snapshot["snapshot_id"]), snapshot["snapshot_id"], **self.scope, commit=True)
        prior = coverage_report(self.bank, self.tr, "RUN-fixture", **self.scope)["evidence"]
        self.assertFalse(prior["dependency_current"])
        self.assertEqual(prior["stale_reasons"], ["dependency_invalidated", "superseded"])
        self.assertTrue(coverage_report(self.bank, self.tr, "RUN-second", **self.scope)["evidence"]["current"])

    def test_taxonomy_change_invalidates_old_run_and_rejects_fork(self):
        submission = self.submission()
        consolidate_analysis(self.bank, submission, **self.scope, commit=True)
        current = load_json(safe_path(self.bank, "taxonomia/generic-1.json"))
        newer = deepcopy(current)
        newer.update(taxonomy_version="generic-2", previous_version="generic-1")
        newer["categories"][0]["definition"] += " Synthetic revised scope."
        snapshot = review_snapshot(self.bank, **self.scope)
        event = self.event(snapshot["snapshot_id"])
        event.update(event_type="taxonomia", old_refs=["generic-1"], new_refs=["generic-2"])
        with self.assertRaisesRegex(ModelError, "TAXONOMY_EVENT_REQUIRED"):
            store_taxonomy(self.bank, newer, commit=True)
        store_taxonomy(self.bank, newer, event=event, commit=True)
        self.assertFalse(coverage_report(self.bank, self.tr, "RUN-fixture", **self.scope)["evidence"]["current"])
        with self.assertRaisesRegex(ModelError, "DEPENDENCY_INVALIDATED"):
            consolidate_analysis(self.bank, submission, **self.scope, commit=True)
        fork = deepcopy(newer); fork["taxonomy_version"] = "generic-fork"
        with self.assertRaisesRegex(ModelError, "BASE_VERSION_STALE"):
            store_taxonomy(self.bank, fork, event=event, commit=True)

    def test_unrelated_permission_does_not_stale_analysis_cache(self):
        submission = self.submission()
        consolidate_analysis(self.bank, submission, **self.scope, commit=True)
        other = ingest(self.bank, job_id="J2", account_id="other-account", source_id="S2", attempt_id="A1",
                       parts=[(1, b"Unrelated synthetic source")], closed=True, expected_parts=1, commit=True)
        record_decision(self.bank, dict(tr_id=other["evidence"]["tr_id"], version_id=other["evidence"]["version_id"],
            company="other", audience="external", purpose="local_analysis", action="grant", authority="Synthetic owner",
            evidence=["Synthetic authorization"], decided_at=utc_now()), commit=True)
        self.assertTrue(coverage_report(self.bank, self.tr, "RUN-fixture", **self.scope)["evidence"]["current"])
        self.assertTrue(consolidate_analysis(self.bank, submission, **self.scope, commit=True)["evidence"]["idempotent"])


if __name__ == "__main__":
    unittest.main()
