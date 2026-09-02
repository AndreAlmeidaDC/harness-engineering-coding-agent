# Contributing

## Required workflow

1. Add or update a failing regression test for the behavior being changed.
2. Modify the smallest validator, template or reference surface.
3. Run:

```bash
python3 scripts/validate_skill.py
python3 scripts/test_validator.py
python3 -m py_compile scripts/*.py
```

4. Update `metadata.json`, `SKILL.md` and `CHANGELOG.md` together.
5. Open a PR explaining the predicted improvement, measured result, false-block risk and rollback.

## Design rules

- Machine-enforce safety-critical invariants when practical.
- Keep LLM judgment for semantics that cannot be reduced honestly.
- Do not add mandatory artifacts without a demonstrated failure class.
- New permissions are deny-by-default and approval-gated.
- State transitions require evidence.
- A handoff requirement needs a real continuity boundary.
- Changes to task states, DAG validation, permission policy or release gates require regression tests.
