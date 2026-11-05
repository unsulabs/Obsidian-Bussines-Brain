import datetime as dt
import multiprocessing
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import transcripciones_trabajos as jobs
from transcripciones_modelo import ModelError, sha256_bytes


def competing_claim(bank, owner, barrier, output):
    barrier.wait()
    try:
        jobs.Queue(bank).claim("job-a", owner)
        output.put("claimed")
    except ModelError as exc:
        output.put(exc.code)


class QueueTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.bank = Path(tmp.name).resolve() / "bank"
        self.now = dt.datetime(2026, 11, 4, tzinfo=dt.timezone.utc)
        self.queue = jobs.Queue(self.bank, clock=lambda: self.now)
        self.queue.enqueue("job-a")

    def staged(self, row, data=b"synthetic result"):
        path = row["staging_path"] + "/result.txt"
        dest = self.bank / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return {"outputs": [{"path": path, "sha256": sha256_bytes(data)}]}

    def test_fencing_late_owner_rejected(self):
        old = self.queue.claim("job-a", "worker-a", lease_seconds=1)
        old_manifest = self.staged(old)
        self.now += dt.timedelta(seconds=2)
        new = self.queue.claim("job-a", "worker-b")
        self.assertGreater(new["fencing_token"], old["fencing_token"])
        with self.assertRaisesRegex(ModelError, "STALE_FENCING_TOKEN"):
            self.queue.submit("job-a", old["fencing_token"], old_manifest)
        with self.assertRaisesRegex(ModelError, "STALE_FENCING_TOKEN"):
            self.queue.commit("job-a", old["fencing_token"])

    def test_expired_current_token_rejected(self):
        row = self.queue.claim("job-a", "worker-a", lease_seconds=1)
        manifest = self.staged(row)
        self.now += dt.timedelta(seconds=1)
        with self.assertRaisesRegex(ModelError, "LEASE_EXPIRED"):
            self.queue.submit("job-a", row["fencing_token"], manifest)

    def test_commit_idempotent_and_strict_transition(self):
        row = self.queue.claim("job-a", "worker-a")
        token = row["fencing_token"]
        with self.assertRaisesRegex(ModelError, "JOB_STATE_INVALID"):
            self.queue.commit("job-a", token)
        self.queue.submit("job-a", token, self.staged(row))
        result = self.queue.commit("job-a", token)
        self.assertEqual((self.bank / result["outputs"][0]["path"]).read_bytes(), b"synthetic result")
        before = list((self.bank / "jobs/job-a").glob("*.json"))
        self.now += dt.timedelta(days=1)
        self.assertTrue(self.queue.commit("job-a", token)["evidence"]["idempotent"])
        self.assertEqual(before, list((self.bank / "jobs/job-a").glob("*.json")))

    def test_tamper_between_submit_commit_rejected(self):
        row = self.queue.claim("job-a", "worker-a")
        manifest = self.staged(row)
        self.queue.submit("job-a", row["fencing_token"], manifest)
        (self.bank / manifest["outputs"][0]["path"]).write_bytes(b"changed")
        with self.assertRaisesRegex(ModelError, "HASH_MISMATCH"):
            self.queue.commit("job-a", row["fencing_token"])
        self.assertEqual(self.queue.get("job-a")["state"], "entregado")

    def test_staging_scope_and_schema_enforced(self):
        row = self.queue.claim("job-a", "worker-a")
        manifest = self.staged(row)
        manifest["outputs"][0]["path"] = "staging/job-b/1/result.txt"
        with self.assertRaisesRegex(ModelError, "STAGING_SCOPE_MISMATCH"):
            self.queue.submit("job-a", row["fencing_token"], manifest)
        manifest = self.staged(row)
        manifest["outputs"][0]["extra"] = True
        with self.assertRaisesRegex(ModelError, "SCHEMA_INVALID"):
            self.queue.submit("job-a", row["fencing_token"], manifest)

    def test_input_change_rejected(self):
        source = self.bank / "source.txt"
        source.write_bytes(b"input")
        self.queue.enqueue("job-b", input_refs=["source.txt"], input_hashes=[sha256_bytes(b"input")])
        row = self.queue.claim("job-b", "worker-a")
        manifest = self.staged(row)
        self.queue.submit("job-b", row["fencing_token"], manifest)
        source.write_bytes(b"changed")
        with self.assertRaisesRegex(ModelError, "INPUT_VERSION_CHANGED"):
            self.queue.commit("job-b", row["fencing_token"])

    def test_dependency_and_enqueue_collision(self):
        self.queue.enqueue("job-b", depends_on=["job-a"])
        with self.assertRaisesRegex(ModelError, "DEPENDENCY_PENDING"):
            self.queue.claim("job-b", "worker-a")
        with self.assertRaisesRegex(ModelError, "IDEMPOTENCY_CONFLICT"):
            self.queue.enqueue("job-a", job_type="changed")

    def test_result_recovery_after_promotion_before_transition(self):
        row = self.queue.claim("job-a", "worker-a")
        self.queue.submit("job-a", row["fencing_token"], self.staged(row))
        with patch.object(self.queue, "_save", side_effect=RuntimeError("crash")), self.assertRaises(RuntimeError):
            self.queue.commit("job-a", row["fencing_token"])
        self.assertEqual(self.queue.get("job-a")["state"], "entregado")
        self.queue.commit("job-a", row["fencing_token"])
        self.assertEqual(self.queue.get("job-a")["state"], "consolidado")
        self.assertEqual(len(list((self.bank / "results").rglob("result.txt"))), 1)

    def test_two_processes_only_one_claim(self):
        ctx = multiprocessing.get_context("spawn" if sys.platform == "win32" else "fork")
        barrier = ctx.Barrier(2)
        output = ctx.Queue()
        processes = [ctx.Process(target=competing_claim, args=(str(self.bank), owner, barrier, output)) for owner in ("worker-a", "worker-b")]
        for process in processes:
            process.start()
        for process in processes:
            process.join(10)
            self.assertEqual(process.exitcode, 0)
        self.assertEqual(sorted([output.get(timeout=2), output.get(timeout=2)]), ["LEASE_BUSY", "claimed"])

    def test_symlink_worker_output_rejected(self):
        row = self.queue.claim("job-a", "worker-a")
        manifest = self.staged(row)
        path = self.bank / manifest["outputs"][0]["path"]
        path.unlink()
        outside = self.bank / "outside"
        outside.write_bytes(b"synthetic result")
        path.symlink_to(outside)
        with self.assertRaisesRegex(ModelError, "UNSAFE_PATH"):
            self.queue.submit("job-a", row["fencing_token"], manifest)

    def test_git_boundary_cannot_be_bypassed_by_queue(self):
        repo = self.bank.parent / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        with self.assertRaisesRegex(ModelError, "BANK_INSIDE_GIT"):
            jobs.Queue(repo / "bank")
        # A repository created after Queue construction also stops mutation.
        subprocess.run(["git", "init", "-q", str(self.bank)], check=True)
        with self.assertRaisesRegex(ModelError, "BANK_INSIDE_GIT"):
            self.queue.claim("job-a", "worker-a")


if __name__ == "__main__":
    unittest.main()
