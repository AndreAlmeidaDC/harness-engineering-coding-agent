# Governance

## Normative surfaces

Current behavior is defined by:

- `SKILL.md`;
- files linked under `references/`;
- `templates/RUN_CONTRACT.json`;
- validators and tests under `scripts/`.

Pre-v2 guides and PDFs remain available in Git history and are not normative after version `2026.09.02`.

## Change authority

The maintainer approves changes to the default branch. Safety-critical changes require regression evidence and PR review.

## Autonomy boundary

The harness coordinates work but does not grant production, financial, public, destructive or credentialed authority. Those actions require explicit user approval in the active run.

## Self-update

The skill may perform a read-only upstream comparison. It never executes remote code, silently updates itself or overwrites local changes.

## Review cadence

Revalidate external claims and examples when tooling or agent runtimes change. Review the eval portfolio after meaningful failures rather than expanding process pre-emptively.
