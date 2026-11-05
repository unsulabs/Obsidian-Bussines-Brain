import copy
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from transcripciones_taxonomia import seed_taxonomy,validate_taxonomy,resolve_identity,propose_change
from transcripciones_modelo import ModelError


class TaxonomyTests(unittest.TestCase):
    def test_generic_multiaxis_and_no_business_assertions(self):
        seed=seed_taxonomy();self.assertEqual(len({c["axis"] for c in seed["categories"]}),5)
        self.assertEqual(seed["entities"],[])

    def test_homonyms_and_brand_company_distinct(self):
        seed=seed_taxonomy()
        seed["entities"]=[dict(entity_id=str(i),name="Nube",kind=kind,scope=scope,aliases=[],identity_evidence=["synthetic authority record"]) for i,(kind,scope) in enumerate([("company","A"),("brand","A"),("company","B")])]
        self.assertEqual(resolve_identity(seed,"Nube",scope="A",kind="brand")["entity_id"],"1")
        seed["entities"].append(dict(seed["entities"][0],entity_id="4"))
        with self.assertRaises(ModelError):resolve_identity(seed,"Nube",scope="A",kind="company")

    def test_diff_full_sweep_and_merge_provenance(self):
        old=seed_taxonomy();new=copy.deepcopy(old);new.update(taxonomy_version="generic-2",previous_version="generic-1")
        new["categories"][0]["aliases"]=["regla de decisión"]
        diff=propose_change(old,new,expected_version="generic-1",catalog_ids=["TR2","TR1"])
        self.assertEqual(diff["changed"],["CAT-criterio"]);self.assertTrue(diff["full_sweep"])
        self.assertEqual(len(diff["jobs"]),2)
        with self.assertRaises(ModelError):propose_change(old,new,expected_version="stale",catalog_ids=[])
        new["equivalences"]=[dict(kind="fusiona",from_ids=["CAT-proceso","CAT-recurso"],to_ids=["CAT-criterio"],rationale="Synthetic comparison",scope="fixture")]
        self.assertEqual(propose_change(old,new,expected_version="generic-1",catalog_ids=[])["equivalences"],new["equivalences"])
