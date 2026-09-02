#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_run_contract.py"
BASE = json.loads((ROOT / "templates" / "RUN_CONTRACT.json").read_text(encoding="utf-8"))


def run_contract(payload: dict) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "run.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return subprocess.run([sys.executable, str(VALIDATOR), str(path)], capture_output=True, text=True)


class ContractTests(unittest.TestCase):
    def test_reference_contract_passes(self):
        proc = run_contract(copy.deepcopy(BASE))
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_cycle_fails(self):
        data = copy.deepcopy(BASE)
        data["tasks"][0]["depends_on"] = ["TASK-002"]
        proc = run_contract(data)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("cycle", proc.stdout)

    def test_unknown_dependency_fails(self):
        data = copy.deepcopy(BASE)
        data["tasks"][1]["depends_on"] = ["TASK-X"]
        proc = run_contract(data)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("unknown dependency", proc.stdout)

    def test_task_without_sensor_fails(self):
        data = copy.deepcopy(BASE)
        data["tasks"][0]["sensors"] = []
        proc = run_contract(data)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("sensors", proc.stdout)

    def test_financial_autonomy_fails(self):
        data = copy.deepcopy(BASE)
        data["permissions"]["financial_actions"] = True
        proc = run_contract(data)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("financial_actions", proc.stdout)

    def test_high_risk_requires_independent_verifier(self):
        data = copy.deepcopy(BASE)
        data["risk"] = "high"
        data["verification"]["independent_context_required"] = False
        proc = run_contract(data)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("independent verification", proc.stdout)

    def test_user_release_requires_rollback(self):
        data = copy.deepcopy(BASE)
        data["release"]["reaches_users"] = True
        data["release"]["rollback"] = ""
        proc = run_contract(data)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("rollback", proc.stdout)

    def test_boundary_handoff_requires_conditions(self):
        data = copy.deepcopy(BASE)
        data["handoff"]["required_when"] = []
        proc = run_contract(data)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("required_when", proc.stdout)


if __name__ == "__main__":
    unittest.main()
