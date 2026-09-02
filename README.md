# Harness Engineering Coding Agent

Portable control plane for AI coding work.

The original skill had strong principles—product intent, Git safety, scope control, independent review, tests, rollback and release discipline—but expressed them through a growing list of documents and mandatory gates. Version `2026.09.02` keeps those principles and moves the critical controls into a machine-validatable run contract.

## Core idea

```text
LLM proposes and executes bounded work.
Deterministic state decides what may advance.
Evidence—not confidence—moves a task to done.
```

## What v2 adds

- JSON run contract with scope, permissions and release boundaries;
- task DAG with dependencies, owners and terminal states;
- worktree/workspace leases for parallel agents;
- stop and escalation conditions based on new evidence;
- independent verification for risky or rubric-based work;
- compact, durable repository state and re-anchoring;
- component, experience and decision observability;
- trajectory summaries without hidden chain-of-thought;
- regression-driven harness improvement;
- handoffs only at real continuity boundaries.

## What v2 removes

- a mandatory artifact matrix for every feature;
- requirement IDs for harmless micro-edits;
- handoff after every meaningful completed task;
- arbitrary task-count thresholds;
- the assumption that more process automatically means more safety.

## Quick start

Copy `templates/RUN_CONTRACT.json`, adapt it and validate:

```bash
python3 scripts/validate_run_contract.py .harness/RUN_CONTRACT.json
```

Run repository checks:

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validator.py
```

## Runtime profiles

- `micro` — low-risk isolated change;
- `run` — normal feature, bugfix, refactor or investigation;
- `review-pair` — independent author/verifier separation;
- `orchestrated` — parallel agents with task DAG and leases.

## Repository structure

```text
SKILL.md
references/
  execution-control.md
  context-and-state.md
  verification-release.md
  observability-learning.md
templates/
  RUN_CONTRACT.json
  TASK.md
  EVALUATION_REPORT.md
  HANDOFF.md
scripts/
  validate_run_contract.py
  validate_skill.py
  test_validator.py
checklists/
  RUN_CHECKLIST.md
```

Pre-v2 guides remain available in Git history but are no longer shipped as normative runtime material. The current `SKILL.md`, references and machine validator define behavior.

## Limits

This harness cannot prove product correctness, remove the need for domain judgment or make privileged actions safe by declaration. A validated contract means the control fields are coherent; it does not mean the implementation is correct.
