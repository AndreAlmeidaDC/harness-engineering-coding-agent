#!/usr/bin/env python3
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md", "README.md", "CHANGELOG.md", "CONTRIBUTING.md", "GOVERNANCE.md",
    "metadata.json", "references/version-check.md", "references/execution-control.md",
    "references/context-and-state.md", "references/verification-release.md",
    "references/observability-learning.md", "templates/RUN_CONTRACT.json",
    "templates/TASK.md", "templates/EVALUATION_REPORT.md", "templates/HANDOFF.md",
    "scripts/validate_run_contract.py", "scripts/test_validator.py"
]


def fail(message: str) -> None:
    print("FAIL:", message)
    raise SystemExit(1)


def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail("missing: " + ", ".join(missing))
    metadata = json.loads((ROOT / "metadata.json").read_text(encoding="utf-8"))
    version = str(metadata.get("version", ""))
    if not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}", version):
        fail("version must use YYYY.MM.DD")
    if metadata.get("origin_url") != "https://github.com/AndreAlmeidaDC/harness-engineering-coding-agent":
        fail("wrong origin")
    corpus = "\n".join((ROOT / p).read_text(encoding="utf-8") for p in REQUIRED if p.endswith(".md"))
    for concept in [version, "run contract", "DAG", "stop conditions", "independent", "rollback", "observability", "boundary"]:
        if concept.lower() not in corpus.lower():
            fail("missing concept: " + concept)
    stale = [
        "End every meaningful run with `.harness/HANDOFF.md`",
        "Every meaningful requirement must have an ID",
        "If there are more than five steps",
        "harness-engineering-coding-agent/main/metadata.json"
    ]
    for phrase in stale:
        if phrase.lower() in corpus.lower():
            fail("stale mandatory process: " + phrase)
    proc = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_run_contract.py"), str(ROOT / "templates" / "RUN_CONTRACT.json")], capture_output=True, text=True)
    if proc.returncode:
        fail(proc.stdout + proc.stderr)
    print(f"Validation passed. version={version}")


if __name__ == "__main__":
    main()
