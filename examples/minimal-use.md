# Minimal use

For a low-risk bugfix, do not generate the full documentation set.

1. Inspect Git state and reproduce the bug.
2. State the target behavior, included files and excluded refactors.
3. Create a two-task run contract: fix, then verify.
4. Write a failing test when behavior is specifiable.
5. Implement the smallest fix.
6. Run the original reproduction plus project sensors.
7. Review the diff and report blind spots.
8. Create a handoff only if the run stops before completion or moves to another owner/reviewer.
