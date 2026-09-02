# Observability and learning

Harness engineering measures the run and the harness, not only the final code.

## Three observability layers

1. **Component:** commands, tool calls, latency, failures, file changes and resource use.
2. **Experience:** whether the user flow, operator workflow or system guarantee actually holds.
3. **Decision:** why the agent chose a task, permission, architecture or recovery path.

Logs without requirement and decision context are insufficient for agentic work.

## Trajectory evidence

Record compact trajectories:

- initial hypothesis;
- context loaded;
- task/state transitions;
- sensors and outcomes;
- failed hypotheses;
- escalation or rollback;
- final blind spots.

Do not store hidden chain-of-thought. Store inspectable decisions and evidence.

## Harness improvement loop

When a run exposes a recurring failure:

1. describe the failure class;
2. identify the missing/incorrect guardrail;
3. predict the measurable improvement;
4. add a regression fixture or eval;
5. change the smallest harness component;
6. compare against the baseline;
7. keep, revise or revert;
8. record new trade-offs.

A rule is accepted because it improves observed performance, not because it sounds strict.

## Eval portfolio

Maintain representative cases: clean success, ambiguous requirement, stale context, failing tests, security boundary, tool outage, partial progress, merge conflict, rollback and long-running resume.

Track completion quality, false blocks, retries without evidence, scope violations, verification coverage, recovery success and human intervention.
