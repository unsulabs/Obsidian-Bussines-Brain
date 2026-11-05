from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from transcripciones_inventario import reconcile, validate_inventory
from transcripciones_custodia import load_catalog, register_capture
from transcripciones_modelo import ModelError
from test_transcripciones_custodia import capture


def inventory():
    return {"schema_version": "inventario.v1", "created_at": "2026-11-04T12:00:00Z", "producer_version": "test-1",
        "snapshot_id": "inventory-a", "account": {"id": "account-a", "observed_identity": "Synthetic"},
        "captured_at": "2026-11-04T12:00:00Z", "sections": [{"name": "owned", "end_observed": True, "end_evidence": "last page observed", "limit": None}],
        "meetings": [{"id": "meeting-a", "url": "https://example.test/meeting", "title": "Synthetic", "state": "pending", "attempts": []}]}


class InventoryTests(unittest.TestCase):
    def test_claimed_download_without_receipt_remains_pending(self):
        snapshot = inventory()
        snapshot["meetings"][0]["state"] = "complete"
        report = reconcile(snapshot, [])
        self.assertFalse(report["evidence"]["download_complete"])
        self.assertEqual(report["evidence"]["counts"]["pending"], 1)

    def test_inaccessible_is_accounted_but_not_downloaded(self):
        snapshot = inventory()
        snapshot["meetings"][0]["state"] = "inaccessible"
        report = reconcile(snapshot, [])
        self.assertTrue(report["evidence"]["all_discovered_accounted"])
        self.assertFalse(report["evidence"]["download_complete"])
        self.assertEqual(report["evidence"]["downloaded_complete"], 0)

    def test_inventory_not_closed_without_end(self):
        snapshot = inventory()
        snapshot["sections"][0].update(end_observed=False, end_evidence=None, limit="session ended")
        self.assertFalse(validate_inventory(snapshot)["inventory_closed"])
        self.assertFalse(reconcile(snapshot, [])["evidence"]["inventory_closed"])

    def test_end_requires_evidence_and_no_limit(self):
        snapshot = inventory()
        snapshot["sections"][0]["end_evidence"] = None
        with self.assertRaisesRegex(ModelError, "END_NOT_OBSERVED"):
            validate_inventory(snapshot)

    def test_duplicate_ids_and_extra_fields_rejected(self):
        snapshot = inventory()
        snapshot["meetings"] *= 2
        with self.assertRaisesRegex(ModelError, "DUPLICATE_MEETING"):
            validate_inventory(snapshot)
        snapshot = inventory()
        snapshot["extra"] = True
        with self.assertRaisesRegex(ModelError, "SCHEMA_INVALID"):
            validate_inventory(snapshot)

    def test_complete_receipt_and_account_isolation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            bank = root / "bank"
            register_capture(bank, capture(root, completeness="complete"), commit=True)
            rows = load_catalog(bank)
            self.assertTrue(reconcile(inventory(), rows)["evidence"]["download_complete"])
            snapshot = inventory()
            snapshot["account"]["id"] = "account-b"
            self.assertEqual(reconcile(snapshot, rows)["evidence"]["counts"]["pending"], 1)


if __name__ == "__main__":
    unittest.main()
