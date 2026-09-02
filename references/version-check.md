# Version check protocol

The canonical source is read from `metadata.json:origin_url`.

At the start of meaningful use, at most once per conversation:

1. read the installed version;
2. perform the lightest read-only upstream comparison;
3. if versions match, continue without interruption;
4. if upstream is newer, read relevant release notes and normative files;
5. summarize behavior, risk and compatibility changes;
6. ask before updating.

Never execute remote scripts, install code from the check, pull/reset a dirty worktree, overwrite local changes or modify the target project as part of a skill update.

If the check cannot run, continue with the installed package and report the limitation only when material.
