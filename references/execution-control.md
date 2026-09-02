# Execution control

The language model proposes and executes bounded work; deterministic state controls whether work may advance.

## Run contract

For non-trivial work, create or update `RUN_CONTRACT.json`. It records goal, scope, risk, permissions, requirements, task DAG, sensors, stop/escalation conditions, rollback and handoff policy.

Do not create a run contract for a one-line explanation or harmless typo. Use it when continuity, risk, parallelism or release matters.

## Task DAG

Each task has a unique ID, dependencies, owner, status, requirement links, file scope, sensors, done criteria and rollback.

Allowed lifecycle:

```text
proposed -> ready -> in_progress -> review -> done
                         |            |
                         v            v
                      blocked      blocked
                         |
                         v
                      cancelled
```

A task can enter `ready` only when dependencies are terminal-successful. A model message does not change state by itself; evidence and the control loop do.

## Ownership and leases

Parallel agents must not silently edit the same mutable surface. A coordinator assigns an owner or workspace lease for each task. If overlap is unavoidable, serialize or define an explicit integration owner.

A lease includes task ID, workspace/worktree, paths, start time and expiry/heartbeat. Abandoned leases are reclaimed only after checking repository state.

## Convergence and stop conditions

Retries are governed by evidence, not a magic number. Stop when:

- consecutive attempts produce no new diagnostic evidence;
- the same failing state repeats;
- the proposed fix contradicts the contract;
- scope, permission, cost or production access must expand;
- the agent cannot identify a falsifiable next hypothesis.

Escalate with the evidence collected, not with “it still does not work”.

## Deterministic control loop

```text
load contract -> select ready task -> acquire lease -> execute bounded slice
-> run declared sensors -> attach evidence -> independent review when required
-> transition state -> checkpoint -> select next task or stop
```

The controller must be able to resume from files and Git without relying on hidden conversation state.
