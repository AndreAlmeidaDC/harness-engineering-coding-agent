# Context and durable state

## Repository as source of truth

Agent-readable context belongs in versioned files close to the work. Chat is coordination, not durable state.

Keep `AGENTS.md` short. It should point to commands, architecture, constraints and current contracts rather than duplicate every document.

## Progressive disclosure

Load in this order:

1. root instructions and current run contract;
2. task and directly linked requirements;
3. affected code/tests/configuration;
4. architecture or decision records only when needed;
5. recent Git history or logs when they answer the current question.

Do not preload the entire repository brain.

## Checkpoints and snapshots

Checkpoint after a task reaches a stable sensor result, before risky migration and before context reset. Record commit/ref, task states, evidence paths and known blind spots.

A snapshot is recoverable only when another agent can reconstruct state from it.

## Re-anchoring

Re-anchor when the agent forgets scope, contradicts a decision, recreates excluded work, loses the data model or cannot explain the current task.

Reload the run contract, task, linked requirements and current diff. Restate what remains. Do not continue piling prompts onto a drifted model.

## Documentation garbage collection

Old plans, duplicate truths and stale instructions increase error. Periodically:

- identify canonical files;
- archive or delete superseded state;
- update links;
- remove completed temporary contracts;
- test that documented commands still work;
- keep historical records clearly non-normative.
