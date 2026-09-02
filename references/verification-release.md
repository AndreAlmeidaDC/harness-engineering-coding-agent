# Verification and release

## Sensor hierarchy

Use deterministic sensors first: unit/integration/e2e tests, typecheck, lint, build, schema validation, migration dry-run, security scanners, accessibility checks, replay and invariant checks.

Use inferential review second: architecture critique, UX review, visual review and security reasoning. These add judgment but do not replace executable evidence.

## Independent verification

For high-risk work, authorization, data, payments, production or rubric-based judgment, the authoring context must not be the only verifier. Use a separate agent/session/human or a deterministic test oracle.

The verifier receives the contract, diff and evidence, not only the implementer's narrative.

## Evidence record

For each task capture:

- command or procedure;
- environment and relevant version;
- exit/result;
- artifact/log path;
- requirement covered;
- blind spots;
- timestamp when freshness matters.

## Release boundary

A release is a separate task. Before it reaches users, require:

- approved scope and version;
- fresh sensors;
- data migration/backup where relevant;
- secrets and environment review;
- feature flag or rollout strategy when useful;
- owner and blast radius;
- observability;
- rollback tested or operationally credible;
- post-release smoke and review date;
- explicit approval for production-impacting action.

A successful local build is not a release decision.
