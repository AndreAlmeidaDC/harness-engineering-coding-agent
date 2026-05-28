# Release Measurement Loop

Use this reference when a change will reach users, production, customer data, integrations or operational workflows.

The goal is to make release and learning part of the harness, not an afterthought.

## When to load this reference

Load this file for production deployment, staged rollout, feature flags, database migrations, user-facing behavior, customer data, third-party integrations, operational workflow changes, incident follow-up or any change where rollback and observability matter.

## Outputs

| File | Purpose |
|---|---|
| `docs/release/RELEASE_PLAN.md` | Defines rollout, ownership, rollback, observability and communication. |
| `docs/product/POST_LAUNCH_REVIEW.md` | Captures adoption, impact, incidents and learning after launch. |
| `.harness/EVALUATION_REPORT.md` | Records verification evidence before release. |

## Release questions

- How will this reach users?
- Is the rollout staged?
- Is there a feature flag?
- Is there a rollback strategy?
- Who owns the release?
- What is the blast radius?
- What logs and metrics are required?
- What alerts are required?
- What is the post-launch review date?

## Measurement questions

- What behavior should change?
- What adoption signal proves value?
- What leading indicator should move first?
- What lagging indicator matters later?
- What should we learn even if the feature fails?

## Rollback standard

A release plan is weak if rollback is described only as “revert if needed”. A useful rollback plan states who can trigger rollback, what condition triggers rollback, what command or process executes rollback, what data migration risk exists and how users or customers will be informed if needed.

## Observability standard

Do not launch unobservable behavior. For user-facing or operational changes, define logs, metrics, dashboards or alerts before treating deployment as success.

## Rules

Do not launch critical changes without rollback. Do not launch unobservable behavior. Do not treat deployment as success. Success means safe release plus measured learning.

## Change history

| Date | Time | Reason |
|---|---|---|
| 2026-05-28 | 13:12 GMT-3 | Converted from subskill to portable reference and expanded rollback and observability standards. |
