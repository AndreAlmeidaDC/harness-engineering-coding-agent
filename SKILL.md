---
name: harness-engineering-coding-agent
description: >
  Portable control-plane workflow for AI coding agents. Use for non-trivial software work that needs bounded scope, task dependencies, workspace isolation, least-privilege tools, deterministic verification, independent review, rollback, release safety, resumable state or multi-agent coordination. Scale down for small edits instead of generating process documents by default.
license: MIT
---

# Harness Engineering Coding Agent

A coding agent is only as reliable as the environment, state machine, permissions, tests and recovery paths around it. This skill supplies that control plane without turning every task into bureaucracy.

## Origin version check

Canonical source:

```text
https://github.com/AndreAlmeidaDC/harness-engineering-coding-agent
```

At meaningful use, follow `references/version-check.md`. Never execute remote update code or self-update silently.

## Activation

Use the smallest profile that protects the work:

| Profile | Use when | Minimum control |
|---|---|---|
| `micro` | harmless, isolated change | scope, Git safety, one sensor, final evidence |
| `run` | feature, bugfix, refactor or investigation with dependencies | validated run contract and bounded task loop |
| `review-pair` | auth, data, business rules, release or rubric judgment | implementer and independent verifier |
| `orchestrated` | parallel, long-running or cross-system work | task DAG, leases/worktrees, checkpoints and integration owner |

Do not activate orchestration because it sounds sophisticated. Activate it when coordination cost is lower than error cost.

## Load only what applies

- `references/execution-control.md` — run contract, DAG, leases and convergence;
- `references/context-and-state.md` — repository context, checkpoints and re-anchoring;
- `references/verification-release.md` — sensors, independent review and release;
- `references/observability-learning.md` — trajectories, evals and harness improvement.

## Operating loop

1. **Inspect before asking.** Read repository instructions, current Git state, relevant code, tests, schemas and recent history before requesting information already available.
2. **State the contract.** Define goal, included/excluded scope, risk, permissions, done criteria, sensors and rollback. For non-trivial work, instantiate `templates/RUN_CONTRACT.json` and validate it.
3. **Build the DAG.** Break work into bounded tasks with dependencies, owner/workspace lease, linked requirements, files, sensors and terminal states.
4. **Execute one ready task.** Make the smallest change. Prefer a failing test first when behavior is clear enough to specify.
5. **Attach evidence.** A task moves to review/done only after its declared sensors run. Report exact result and blind spots.
6. **Verify independently when required.** The verifier inspects contract, diff and raw evidence rather than accepting the author's summary.
7. **Checkpoint and converge.** Commit stable slices, stop retries without new evidence, re-anchor on drift and escalate when scope or permission must expand.
8. **Release separately.** Production, credentials, data migrations, payments, public actions and destructive operations require an explicit release task and human approval.
9. **Handoff only at a boundary.** Create a handoff when work crosses session, owner, review or release boundaries—not after every completed typo.
10. **Improve the harness with evidence.** Turn recurring failures into a regression case, make the smallest guardrail change and compare with the baseline.

## Non-negotiable rules

- Do not overwrite unidentified user changes.
- Do not weaken tests to manufacture success.
- Do not let an LLM message alone transition task state.
- Do not give two agents an overlapping mutable lease without an integration plan.
- Do not retry the same hypothesis without new evidence.
- Do not hide blind spots or call partial verification complete.
- Do not grant production, financial, public or credentialed authority by default.
- Do not store hidden chain-of-thought; record inspectable decisions, evidence and state transitions.

## Commands

```bash
python3 scripts/validate_run_contract.py path/to/RUN_CONTRACT.json
python3 scripts/validate_skill.py
python3 scripts/test_validator.py
```

## Completion format

```text
Summary
- bounded outcome and scope

Evidence
- sensors, exact results and environment
- requirement/task coverage
- blind spots

Safety
- permissions exercised
- unexpected changes
- rollback

State
- branch/checkpoint/task states
- boundary handoff only when required
```

## Change history

| Date | Version | Change |
|---|---|---|
| 2026-09-02 | 2026.09.02 | Rebuilt as an executable control plane: validated run contract, task DAG, leases, convergence, permission policy, independent verification, boundary handoffs, observability and regression-driven harness evolution. |
