import copy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from transcripciones_antecedentes import plan_review, merge_review, invalidate_dependencies, stage_review
from transcripciones_modelo import ModelError, read_bytes, sha256_bytes


def event(kind="taxonomia"):
    return {"schema_version": "evento.v1", "created_at": "2026-11-04T00:00:00Z",
            "producer_version": "test", "event_id": "EV-1", "event_type": kind,
            "old_refs": [], "new_refs": [], "reason": "new conceptual category",
            "actor": "synthetic-owner", "affected_ids": [], "sweep_snapshot": "SN-1", "jobs": []}


def snapshot():
    return {"snapshot_id": "SN-1", "entries": [
        {"tr_id": tr, "version_ids": ["V-1", "V-2"], "title": title,
         "eligibility": {"allowed": True, "company": "demo", "audience": "internal",
                         "purpose": "internal_query", "permission_snapshot": "a" * 64,
                         "evidence": "synthetic-ledger"}}
        for tr, title in [("TR-OLD", "colores para pedidos"), ("TR-NEW", "semaforo")]]}


def delivery(job, state="reviewed"):
    return {**{k: job[k] for k in ("job_id", "input_hash", "attempt", "tr_id")},
            "state": state, "reason": "agent examined all versions",
            "reviewed_version_ids": job["version_ids"], "relations": [], "proposals": []}


class Reviews(unittest.TestCase):
    def plan(self):
        return plan_review(event(), snapshot())["evidence"]["plan"]

    def test_all_entries_without_lexical_overlap_and_versions(self):
        plan = self.plan()
        self.assertEqual({j["tr_id"] for j in plan["jobs"]}, {"TR-OLD", "TR-NEW"})
        self.assertEqual(plan["mode"], "full_snapshot")
        self.assertEqual(plan["jobs"][0]["version_ids"], ["V-1", "V-2"])

    def test_resume_does_not_skip_earlier_tr_id(self):
        plan = self.plan()
        later = delivery(plan["jobs"][-1])
        first = merge_review({"plan": plan, "results": [later]})
        self.assertFalse(first["evidence"]["complete"])
        self.assertEqual(first["evidence"]["cursor"]["next_tr_id"], plan["jobs"][0]["tr_id"])
        done = merge_review({"plan": plan, "previous": first["evidence"],
                             "results": [delivery(plan["jobs"][0])]})
        self.assertTrue(done["evidence"]["complete"])
        self.assertEqual(len(done["evidence"]["accepted_results"]), 2)

    def test_empty_and_inaccessible_are_never_complete(self):
        plan = self.plan()
        for results in ([], [delivery(j, "inaccessible") for j in plan["jobs"]]):
            merged = merge_review({"plan": plan, "results": results})
            self.assertFalse(merged["evidence"]["complete"])
            self.assertIn("SWEEP_INCOMPLETE", merged["warnings"])

    def test_new_snapshot_does_not_accept_old_cursor(self):
        plan = self.plan()
        old = merge_review({"plan": plan, "results": []})["evidence"]
        new_snapshot = snapshot()
        new_snapshot["entries"][0]["version_ids"].append("V-3")
        new_plan = plan_review(event(), new_snapshot)["evidence"]["plan"]
        with self.assertRaises(ModelError):
            merge_review({"plan": new_plan, "previous": old, "results": []})

    def test_late_delivery_tampering_and_missing_prior_version(self):
        for key, value in [("attempt", 0), ("input_hash", "b" * 64),
                           ("reviewed_version_ids", ["V-2"])]:
            plan = self.plan()
            record = delivery(plan["jobs"][0])
            record[key] = value
            with self.assertRaises(ModelError):
                merge_review({"plan": plan, "results": [record]})
        plan["jobs"].pop()
        with self.assertRaises(ModelError):
            merge_review({"plan": plan, "results": []})

    def test_permissions_fail_closed_and_excluded_accounted(self):
        snap = snapshot()
        del snap["entries"][0]["eligibility"]
        with self.assertRaises(ModelError):
            plan_review(event(), snap)
        snap = snapshot()
        snap["entries"][0]["eligibility"]["allowed"] = False
        plan = plan_review(event(), snap)["evidence"]["plan"]
        done = merge_review({"plan": plan, "results": [delivery(plan["jobs"][0])]})
        self.assertTrue(done["evidence"]["complete"])
        self.assertEqual(done["evidence"]["decisions"]["TR-OLD"]["state"], "excluded")

    def test_all_event_types_and_rejected_cycle_propagate(self):
        records = [{"id": "claim", "depends_on": [], "editorial_state": "rechazado"},
                   {"id": "summary", "depends_on": ["claim", "web"]},
                   {"id": "web", "depends_on": ["summary"]},
                   {"id": "bot", "depends_on": ["web"]},
                   {"id": "clean", "depends_on": []}]
        original = copy.deepcopy(records)
        for kind in ("nueva_fuente", "correccion", "taxonomia", "permisos", "analizador", "fallo"):
            audit = invalidate_dependencies(event(kind), records)["evidence"]
            self.assertEqual(set(audit["invalidated_ids"]), {"claim", "summary", "web", "bot"})
            self.assertFalse(audit["repaired"])
        self.assertEqual(original, records)

    def test_unknown_lineage_is_not_clean(self):
        audit = invalidate_dependencies(event(), [{"id": "bot", "depends_on": ["missing"]}])
        self.assertEqual(audit["evidence"]["invalidated_ids"], ["bot"])
        self.assertEqual(audit["status"], "DONE_WITH_CONCERNS")

    def test_proposals_cannot_ratify(self):
        plan = self.plan()
        record = delivery(plan["jobs"][0])
        record["proposals"] = [{"editorial_state": "ratificado", "reason": "recent"}]
        with self.assertRaises(ModelError):
            merge_review({"plan": plan, "results": [record]})

    def test_bilateral_evidence_and_retoma_preserved(self):
        plan = self.plan()
        data = b"synthetic passage"
        digest = sha256_bytes(data)
        def span(tr):
            return {"tr_id": tr, "version_id": "V-1", "text_sha256": digest,
                    "start": 0, "end": len(data), "excerpt_sha256": digest}
        relation = {"schema_version": "relacion.v1", "created_at": "2026-11-04T00:00:00Z",
                    "producer_version": "test", "relation_id": "R-1", "predicate": "retoma",
                    "vocabulary_version": "relaciones-banco.v1",
                    "source_ref": {"kind": "source", "id": "TR-NEW", "version_id": "V-1"},
                    "target_ref": {"kind": "source", "id": "TR-OLD", "version_id": "V-1"},
                    "source_evidence": [span("TR-NEW")], "target_evidence": [span("TR-OLD")],
                    "rationale": "agent relates ideas across terminology", "scope": "demo orders",
                    "valid_time": None, "editorial_state": "propuesta", "reviewer": None,
                    "supersedes_relation_id": None}
        record = delivery(plan["jobs"][0])
        record["relations"] = [relation]
        args = {"plan": plan, "results": [record],
                "sources": {("TR-NEW", "V-1"): data, ("TR-OLD", "V-1"): data},
                "known_refs": {("source", tr, "V-1") for tr in ("TR-NEW", "TR-OLD")}}
        output = merge_review(args)["evidence"]["relations"][0]
        self.assertEqual(output["predicate"], "retoma")
        self.assertEqual(output["editorial_state"], "propuesta")
        for key, value in [("target_evidence", []), ("scope", ""), ("editorial_state", "ratificado")]:
            broken = copy.deepcopy(args)
            broken["results"][0]["relations"][0][key] = value
            with self.assertRaises(ModelError):
                merge_review(broken)

        # Registry endpoints with a resolved speaker require the exact explicit
        # taxonomy; neither the relation label nor a known ID grants identity.
        from test_transcripciones_analisis import fixture
        from transcripciones_taxonomia import seed_taxonomy
        claim = fixture()["claims"][0]
        claim.update(claim_id="C-resolved", evidence_spans=[span("TR-OLD")],
                     attribution_state="resuelta", resolved_entity_id="PERSON-luz", resolved_entity_kind="person")
        relation["target_ref"] = {"kind": "claim", "id": "C-resolved", "version_id": "V-1"}
        args["known_refs"].add(("claim", "C-resolved", "V-1"))
        args["ref_registry"] = {("claim", "C-resolved", "V-1"): claim}
        with self.assertRaises(ModelError):
            merge_review(args)
        taxonomy = seed_taxonomy()
        taxonomy["entities"] = [{"entity_id": "PERSON-luz", "name": "Luz", "kind": "person",
                                  "scope": claim["scope"], "aliases": [], "identity_evidence": ["Synthetic identity attestation"]}]
        args["taxonomy"] = taxonomy
        self.assertEqual(merge_review(args)["evidence"]["relations"][0]["target_ref"]["id"], "C-resolved")
        args["taxonomy"]["entities"][0]["scope"] = "wrong-scope"
        with self.assertRaises(ModelError):
            merge_review(args)

    def test_staging_immutable_and_no_original_mutation(self):
        with tempfile.TemporaryDirectory() as temp:
            bank = Path(temp).resolve()
            output = stage_review(bank, "J-1", 1, {"synthetic": True})
            before = read_bytes(bank, output["path"])
            with self.assertRaises(ModelError):
                stage_review(bank, "J-1", 1, {"synthetic": False})
            self.assertEqual(read_bytes(bank, output["path"]), before)
            self.assertFalse((bank / "originales").exists())


if __name__ == "__main__":
    unittest.main()
