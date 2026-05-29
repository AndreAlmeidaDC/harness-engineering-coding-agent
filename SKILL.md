---
name: harness-engineering-coding-agent
description: Portable operational workflow for AI coding agents. Use for software development tasks involving product discovery, PRD/specification, architecture, semantic specifications, coding, bugfixes, refactors, integrations, tests, auth, data, security, CI/CD, release, observability, replayability, rollback, evaluation and handoff. Também use para agentes de coding, desenvolvimento com IA, critérios de aceite, plano de testes, revisão, deploy seguro e medição pós-lançamento.
---

# Harness Engineering Coding Agent

Use this skill to guide an AI coding agent from **product intent** to **production impact** with disciplined harness engineering.

This skill is not a prompt for generating code faster. It is a portable operating workflow for building software with AI agents while preserving product clarity, engineering quality, verification, release safety, observability and learning.

It can be used by any coding agent that can read files, edit code, run commands and keep notes, including Claude Code, Codex, Cursor, Windsurf, Gemini CLI, OpenCode, local agents or internal company agents.

## Core principle

**Code is not software.**

Software includes requirements, architecture, data, user flows, security, tests, deployment, observability, maintenance and the process that keeps all of it coherent over time.

The agent must never treat a working local demo as production-ready software.

## Activation decision

If the user asks to build, modify, debug, refactor, test, release or evaluate software, first classify the request and choose the smallest workflow that protects quality without creating unnecessary process.

Use the full workflow only when the task has product ambiguity, user impact, production impact, user data, auth, integrations, release risk, security risk or multi-session complexity.

## When to use

Use this skill when the task involves any of the following:

- product discovery for a new feature or application;
- PRD, specification, acceptance criteria or architecture definition;
- implementation of feature, bugfix, refactor, migration or integration;
- frontend plus backend plus data or auth;
- security, permissions, RLS, payments, credentials or personal data;
- CI/CD, release planning, feature flags, rollback or monitoring;
- evaluating whether an AI-generated change is good enough;
- designing semantic behavior contracts, agentic workflows, automations or AI-native systems;
- long-running tasks where another agent or human may need to resume later.

## When not to use the full workflow

Do not run the full workflow for one-off explanations, throwaway prototypes, small snippets, isolated edits that do not affect behavior or quick learning experiments.

Even then, keep Git safety, scope control and explicit done criteria.

## Execution modes

| Mode | Use when | Rule |
|---|---|---|
| `solo` | The task is small or medium, clear and low risk. | One agent performs the full loop with discipline. |
| `review-pair` | The task has medium risk, auth, data, security, business logic or release sensitivity. | One agent implements and another agent or separate session validates. |
| `squad` | The task is high-risk, long-running, product-critical or cross-functional. | Multiple roles are activated. Read `references/squad-mode.md`. |

The default is `solo`. Do not use `squad` just because it sounds impressive. Use it when the cost of coordination is lower than the cost of error.

## Non-negotiable rules

1. **No blind coding.** The agent must understand product intent or the existing spec before implementation.
2. **No giant context dump.** Load minimum sufficient context. Use documentation as a map, not as a landfill.
3. **No one-shot hero behavior.** Break work into small tasks and implement one task at a time.
4. **No premature victory.** Do not mark done because code compiles or a request returns `200`. Done requires acceptance criteria and relevant sensors.
5. **No test weakening.** Never delete, weaken or bypass tests to make the change pass. If a test is wrong, explain why and request or record approval.
6. **No silent scope creep.** Record extra work as follow-up. Do not implement outside the current task unless approved.
7. **No unsafe production action.** Production, credentials, payments, destructive database operations and user data require explicit approval.
8. **No untracked handoff.** Every meaningful run must leave enough state for another agent or human to continue.

## Project files

Create lightweight versions only when the task requires them. Do not create process files for tiny edits that do not need them.

```text
AGENTS.md
.harness/STATE.md
.harness/CONTRACT.md
.harness/ACCEPTANCE_CRITERIA.md
.harness/TEST_PLAN.md
.harness/EVALUATION_REPORT.md
.harness/HANDOFF.md
.harness/OPEN_QUESTIONS.md
docs/product/PRODUCT_INTENT.md
docs/product/PRD.md
docs/product/METRICS_PLAN.md
docs/product/POST_LAUNCH_REVIEW.md
.harness/SEMANTIC_SPEC.md
docs/architecture/ARCHITECTURE.md
docs/decisions/DECISION_LOG.md
docs/release/RELEASE_PLAN.md
```

Keep `AGENTS.md` short. It should point to the right docs, commands and constraints, not contain the whole company brain.

## Artifact matrix

| Task type | Minimum artifacts | Optional artifacts |
|---|---|---|
| `quick-fix` | final summary with verification; `.harness/HANDOFF.md` if state matters | `.harness/EVALUATION_REPORT.md` |
| `feature` | `.harness/CONTRACT.md`, `.harness/ACCEPTANCE_CRITERIA.md`, `.harness/TEST_PLAN.md`, `.harness/HANDOFF.md` | `docs/product/PRD.md` |
| `product-feature` | `docs/product/PRODUCT_INTENT.md`, `docs/product/PRD.md`, `.harness/CONTRACT.md`, `.harness/HANDOFF.md` | `.harness/SEMANTIC_SPEC.md`, `docs/product/METRICS_PLAN.md` |
| `architecture` | `.harness/CONTRACT.md`, `.harness/SEMANTIC_SPEC.md`, `docs/architecture/ARCHITECTURE.md`, `docs/decisions/DECISION_LOG.md`, `.harness/HANDOFF.md` | `.harness/EVALUATION_REPORT.md` |
| `security-data` | `.harness/CONTRACT.md`, `.harness/ACCEPTANCE_CRITERIA.md`, `.harness/TEST_PLAN.md`, `.harness/EVALUATION_REPORT.md`, `.harness/HANDOFF.md` | `docs/decisions/DECISION_LOG.md` |
| `release` | `docs/release/RELEASE_PLAN.md`, `.harness/EVALUATION_REPORT.md`, `.harness/HANDOFF.md` | `.harness/SEMANTIC_SPEC.md` when replay/auditability matters, `docs/product/POST_LAUNCH_REVIEW.md` |
| `investigation` | `.harness/STATE.md`, `.harness/EVALUATION_REPORT.md` or investigation notes, `.harness/HANDOFF.md` | `.harness/OPEN_QUESTIONS.md` |

## Workflow

### Phase 0: classify the task

Classify the request before acting. Use one or more of these labels:

- `quick-fix`: simple correction, low risk;
- `feature`: new behavior or UI;
- `product-feature`: feature with product ambiguity;
- `architecture`: structural decision or cross-cutting change;
- `semantic-system`: behaviors, guarantees, constraints, agentic workflows, automations, replayability, auditability or AI-native runtime concerns;
- `security-data`: auth, permissions, secrets, RLS, payments or personal data;
- `release`: deployment, flags, rollback, observability;
- `investigation`: bug diagnosis, research, logs or incident.

Then choose execution mode: low risk uses `solo`, medium risk uses `review-pair`, and high-risk or long-running work uses `squad`.

### Phase 1: product intent gate

Before spec or code, answer:

- What problem are we solving?
- Who has this problem?
- Why now?
- What happens if we do not build it?
- What is the smallest valuable version?
- What should not be built now?
- How will we know if it worked?

If answers are missing for product-relevant work, read `references/product-engineering-discovery.md` and create or update the needed product intent artifacts.

### Phase 2: specification gate

For any feature with more than trivial scope, create or update the contract, acceptance criteria and test plan. Use `references/prd-specification-builder.md` when the product, role, flow, architecture or acceptance criteria are not clear.

The spec must distinguish confirmed facts, decisions, assumptions, open questions and out-of-scope items. Every meaningful requirement must have an ID, for example `BUS-001`, `USER-001`, `AUTH-001`, `DATA-001`, `UI-001`, `SEC-001`, `NFR-001`, `REL-001` or `MET-001`.


### Phase 2.5: semantic specification gate

Use this gate for `architecture`, `semantic-system`, agentic workflows, automations, distributed behavior or AI-native systems. Read `references/semantic-system-design.md` and create or update `.harness/SEMANTIC_SPEC.md` when behavior, guarantees, constraints, events, state, replay, auditability or observability are central to the task.

The agent should describe behaviors before files and functions. Prefer plain language, but use lightweight behavior blocks when that makes the contract clearer. The goal is not to impose a DSL or advanced stack; the goal is to prevent duplicated logic, architectural drift and hidden assumptions.

For structural decisions, perform a proportionate state-of-the-art review. Compare the simplest conventional approach with any advanced option such as state machines, workflow engines, event sourcing, actor models, policy engines, graph storage, vector retrieval, CQRS or transactional outbox. Choose the smallest design that preserves the required guarantees.

### Phase 3: context loading

Load only context relevant to the task. Recommended order:

1. `AGENTS.md`
2. `.harness/STATE.md`
3. `.harness/CONTRACT.md`
4. relevant PRD, spec and test plan
5. relevant architecture docs
6. files directly involved in the task
7. recent Git history if needed

Do not load every document just because it exists.

### Phase 4: Git safety gate

Before modifying files, check repository state with the equivalent of:

```bash
git status
git branch --show-current
git log --oneline -5
```

If the working tree is dirty, identify whether changes belong to the user. Do not overwrite them. Prefer a branch or worktree for non-trivial work.

### Phase 5: task breakdown

Break the work into small tasks. Each task must include task ID, linked requirement IDs, files likely affected, expected behavior, verification method, rollback risk and done criteria.

If there are more than five steps or unclear dependencies, create `.harness/TASKS.md`.

### Phase 6: implementation loop

For each task:

1. restate the task;
2. make minimal changes;
3. run relevant sensors;
4. inspect failures;
5. correct;
6. update progress;
7. stop after the task is done.

Do not mix unrelated tasks in the same loop.

### Phase 7: feedback sensors

Use computational sensors first: unit tests, integration tests, e2e tests, lint, typecheck, build, static analysis, schema validation, migration dry-run, replay/audit checks, accessibility checks and security scans when applicable.

Use inferential sensors second: AI review, architecture critique, UX critique, security reasoning and requirement coverage review.

Inferential sensors are useful, but they are not a substitute for deterministic checks.

If no automated test exists, create the smallest relevant verification path or document why verification is currently manual.

Never report verification as complete with generic wording. Always include exact commands, exact outcomes and remaining blind spots.

### Phase 8: evaluation report

Create or update `.harness/EVALUATION_REPORT.md` for meaningful work. Include what changed, which requirements were covered, commands run, pass/fail result, unresolved risks, assumptions made, files changed and follow-up tasks.

### Phase 9: release gate

If the change will reach users, production, customer data, integrations or operational workflows, read `references/release-measurement-loop.md`.

Answer these release questions:

- How will this reach users?
- Is there a feature flag?
- Is there rollback?
- Who owns the release?
- What logs, metrics, traces, audit events and replay evidence are needed?
- What is the blast radius?
- What is the post-launch review date?

### Phase 10: handoff

End every meaningful run with `.harness/HANDOFF.md`. Include current state, completed work, pending work, blocked items, commands already run, files changed, risks and recommended next action.

## Review-pair handoff

When using `review-pair`, the implementation agent must provide requirement IDs addressed, files changed, commands run, known risks, verification gaps and suggested review focus.

The evaluation agent must not assume correctness from the implementation summary. It must verify against the contract and inspect changed files.

## Definition of done

A task is done only when product intent is clear enough for the current scope, spec or contract exists when needed, all acceptance criteria for the task were addressed, relevant sensors were executed, failures were fixed or explicitly recorded, no user changes were overwritten, no test was weakened without approval, state and handoff were updated, and release and measurement plan exist when users are affected.

## Anti-patterns

Stop and correct course if you detect vibe coding by prompt accumulation, implementation before product intent, PRD with no acceptance criteria, acceptance criteria with no test plan, giant `AGENTS.md` as memory landfill, agent judging its own work without sensors, code compiling but behavior not validated, tests deleted to pass, feature launched without rollback, no owner for post-launch behavior, or logs, metrics, traces or audit events added only after an incident, or architecture chosen before behavior and guarantees are explicit.

## Output format for agent responses

At the end of an execution, respond with:

```text
Summary
- What changed

Verification
- Commands/sensors run
- Results
- Remaining blind spots

Risks
- Known risks or assumptions

Files changed
- List

Next action
- Recommended next step
```

## Change history

| Date | Time | Reason |
|---|---|---|
| 2026-05-28 | 13:00 GMT-3 | Reworked as a portable skill for any AI coding agent, added YAML frontmatter, activation heuristics, artifact matrix, review-pair handoff and stronger verification rules. |
| 2026-05-29 | 05:50 GMT-3 | Added semantic specification gate, state-of-the-art review guidance, replay/auditability checks and semantic-system classification inspired by VibeCoding state-of-the-art-driven development. |
