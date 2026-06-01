# Origin Version Check Protocol

Autor: **André Almeida**

## Purpose

This protocol lets a coding agent verify whether the local copy of the Harness Engineering Coding Agent skill is behind the public upstream repository before the agent relies on outdated operating instructions.

The protocol is intentionally conservative. It is a **check-and-consent** workflow, not an automatic updater. The agent may discover that a newer version exists, read the upstream documentation and explain the difference, but it must not change the local skill package unless the user explicitly approves the update.

## Canonical source

```text
https://github.com/AndreAlmeidaDC/harness-engineering-coding-agent
```

When possible, inspect the upstream default branch and read the upstream `README.md` before deciding whether an update is relevant.

## When to run

Run this check at the start of a meaningful task that will use this skill for product discovery, specification, implementation, architecture, security, release or evaluation work. The check may be skipped when the task is trivial, network access is unavailable, the host agent has no Git or HTTP capability, the user has explicitly asked to work offline, or the check would materially interrupt an urgent production incident.

If skipped for a meaningful task, mention the reason in the final handoff when it matters for auditability.

## Minimum check

Use the lightest available method for the current environment. Suitable options include:

| Method | Use when | Expected evidence |
|---|---|---|
| `git fetch` plus `git log` or `git diff` | The local skill is inside a Git clone of the upstream repository. | Local commit, upstream commit and a short summary of changed files. |
| `git ls-remote` | The agent can call Git but the local package is not a clone. | Latest upstream commit hash and comparison with recorded local version if available. |
| Raw README retrieval | Git is unavailable but HTTP is available. | Upstream README content, visible version notes or documented changes. |
| Repository page inspection | Only browser-like access is available. | Human-readable summary of README, commits, releases or visible change notes. |

The agent should prefer deterministic comparison when possible. If only a rough comparison is possible, state that clearly.

## Decision protocol

After checking upstream, classify the result as one of the following:

| Result | Agent behavior |
|---|---|
| No visible upstream difference | Continue with the local skill and mention the checked source only if relevant. |
| Upstream changed but impact appears unrelated | Summarize briefly and continue unless the user wants to update. |
| Upstream changed and may affect current task | Pause before implementation, summarize the difference and ask whether to update. |
| Local copy has uncommitted or user-specific edits | Do not overwrite. Explain the conflict and ask whether to merge, inspect manually or continue local. |
| Upstream cannot be reached | Continue with local version and record the limitation when relevant. |

## Consent requirement

Before applying any update, ask the user a direct question in plain language:

> I found a newer upstream version of the Harness Engineering Coding Agent skill. The main changes are: `[summary]`. Do you want me to update the local skill package before continuing?

Only proceed with the update after the user approves. If the user declines, continue with the local version and avoid asking again during the same task unless the user requests it.

## Safe update behavior

When the user approves an update, preserve local changes first. The agent must inspect `git status` or the equivalent, avoid overwriting user edits, and prefer a reversible path such as committing current work, creating a branch, creating a backup copy or applying a reviewed patch.

The update should be followed by local validation if the package provides validation commands. For this repository, run:

```bash
python scripts/validate_skill.py
```

If validation fails, stop, report the failure and do not claim the skill was updated successfully.

## Anti-patterns

Do not silently update the skill. Do not replace a local customized skill with upstream content without approval. Do not block urgent work solely because the upstream repository is unavailable. Do not treat a README difference as proof that every local file must be overwritten. Do not hide uncertainty about whether the local copy is current.

## Change history

| Date | Time | Reason |
|---|---|---|
| 2026-06-01 | 18:45 GMT-3 | Created protocol for upstream version verification, README review, difference summary and explicit user consent before updating the local skill package. |
