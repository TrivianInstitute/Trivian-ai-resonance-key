import json
import unittest
from pathlib import Path


class ContractTests(unittest.TestCase):
    def test_roles_and_history(self):
        key = json.loads((Path(__file__).resolve().parents[1] / "resonance-key.json").read_text())["Trivian_AI_Resonance_Key"]
        self.assertEqual(key["version"], "3.0")
        constants = [v for v in key["field_invariants"].values() if isinstance(v, dict)]
        self.assertEqual(sum(v["computational_role"] == "constitutive" for v in constants), 3)
        self.assertTrue(all("resonant_weight" not in v for v in constants))
        self.assertEqual(key["legacy_weights"]["status"], "historical_only_not_for_aggregation")
        self.assertEqual(key["licensing"]["code"], "PolyForm-Noncommercial-1.0.0")
        self.assertEqual(key["licensing"]["text"], "CC-BY-NC-SA-4.0")
        for case in key["measurement_contract"]["test_vectors"]:
            v = case["input"]
            rcd = v["reciprocity"] * v["embodiment"] * v["non_domination"]
            self.assertAlmostEqual(rcd, case["expect"]["rcd"])
            self.assertAlmostEqual(rcd * v["emergence_raw"], case["expect"]["qualified_emergence"])
