#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ALLOWED_TASK_TYPES = {
    "quick-fix", "feature", "product-feature", "architecture", "semantic-system",
    "security-data", "release", "investigation", "documentation", "prototype"
}
ALLOWED_RISKS = {"low", "medium", "high", "critical"}
ALLOWED_TASK_STATES = {"proposed", "ready", "in_progress", "blocked", "review", "done", "cancelled"}
ALLOWED_HANDOFF = {"none", "boundary", "always"}
TERMINAL_REQUIRED = {"done", "blocked", "cancelled"}


def fail(errors: list[str]) -> int:
    for error in errors:
        print(f"FAIL: {error}")
    return 1


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("root must be an object")
    return value


def has_cycle(tasks: list[dict[str, Any]]) -> bool:
    deps = {str(task.get("id")): [str(x) for x in task.get("depends_on", [])] for task in tasks}
    state: dict[str, int] = {}

    def visit(node: str) -> bool:
        marker = state.get(node, 0)
        if marker == 1:
            return True
        if marker == 2:
            return False
        state[node] = 1
        for dep in deps.get(node, []):
            if visit(dep):
                return True
        state[node] = 2
        return False

    return any(visit(node) for node in deps)


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ["schema_version", "run_id", "goal", "task_type", "risk", "scope", "workspace", "permissions", "requirements", "tasks", "terminal_states", "stop_conditions", "escalation_conditions", "verification", "release", "handoff"]:
        if key not in data:
            errors.append(f"missing key: {key}")

    if data.get("task_type") not in ALLOWED_TASK_TYPES:
        errors.append(f"unsupported task_type: {data.get('task_type')}")
    if data.get("risk") not in ALLOWED_RISKS:
        errors.append(f"unsupported risk: {data.get('risk')}")

    scope = data.get("scope") if isinstance(data.get("scope"), dict) else {}
    if not scope.get("include"):
        errors.append("scope.include must not be empty")
    if "exclude" not in scope:
        errors.append("scope.exclude must be explicit")

    permissions = data.get("permissions") if isinstance(data.get("permissions"), dict) else {}
    for key in ["filesystem", "network", "credentials", "production", "financial_actions", "public_communications"]:
        if key not in permissions:
            errors.append(f"permissions missing: {key}")
    if permissions.get("production") is True and not data.get("release", {}).get("approval_required"):
        errors.append("production permission requires release.approval_required=true")
    if permissions.get("financial_actions") is True:
        errors.append("financial_actions must remain false in an autonomous run contract")

    requirements = data.get("requirements") if isinstance(data.get("requirements"), list) else []
    req_ids = [str(req.get("id")) for req in requirements if isinstance(req, dict)]
    if len(req_ids) != len(set(req_ids)):
        errors.append("requirement IDs must be unique")
    if any(not req_id or req_id == "None" for req_id in req_ids):
        errors.append("every requirement needs an id")

    tasks = data.get("tasks") if isinstance(data.get("tasks"), list) else []
    if not tasks:
        errors.append("tasks must not be empty")
    task_ids = [str(task.get("id")) for task in tasks if isinstance(task, dict)]
    if len(task_ids) != len(set(task_ids)):
        errors.append("task IDs must be unique")
    known = set(task_ids)
    requirement_set = set(req_ids)
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            errors.append(f"tasks[{index}] must be an object")
            continue
        task_id = str(task.get("id"))
        if task.get("status") not in ALLOWED_TASK_STATES:
            errors.append(f"{task_id}: invalid status")
        if not task.get("done_when"):
            errors.append(f"{task_id}: done_when must not be empty")
        if not task.get("sensors"):
            errors.append(f"{task_id}: sensors must not be empty")
        if not task.get("rollback"):
            errors.append(f"{task_id}: rollback is required")
        for dep in task.get("depends_on", []):
            if dep not in known:
                errors.append(f"{task_id}: unknown dependency {dep}")
            if dep == task_id:
                errors.append(f"{task_id}: cannot depend on itself")
        for req_id in task.get("requirement_ids", []):
            if req_id not in requirement_set:
                errors.append(f"{task_id}: unknown requirement {req_id}")
    if tasks and has_cycle(tasks):
        errors.append("task dependency graph contains a cycle")

    terminal = set(data.get("terminal_states", []))
    if not TERMINAL_REQUIRED.issubset(terminal):
        errors.append("terminal_states must include done, blocked and cancelled")
    if not data.get("stop_conditions"):
        errors.append("stop_conditions must not be empty")
    if not data.get("escalation_conditions"):
        errors.append("escalation_conditions must not be empty")

    verification = data.get("verification") if isinstance(data.get("verification"), dict) else {}
    if not verification.get("required_sensors"):
        errors.append("verification.required_sensors must not be empty")
    if verification.get("blind_spots_must_be_reported") is not True:
        errors.append("verification.blind_spots_must_be_reported must be true")
    if data.get("risk") in {"high", "critical"} and verification.get("independent_context_required") is not True:
        errors.append("high/critical risk requires independent verification context")

    release = data.get("release") if isinstance(data.get("release"), dict) else {}
    if release.get("reaches_users") and not release.get("rollback"):
        errors.append("user-facing release requires rollback")
    if release.get("reaches_users") and release.get("approval_required") is not True:
        errors.append("user-facing release requires explicit approval")

    handoff = data.get("handoff") if isinstance(data.get("handoff"), dict) else {}
    if handoff.get("mode") not in ALLOWED_HANDOFF:
        errors.append("handoff.mode must be none, boundary or always")
    if handoff.get("mode") == "boundary" and not handoff.get("required_when"):
        errors.append("boundary handoff requires required_when conditions")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Harness run contract")
    parser.add_argument("path", nargs="?", default="templates/RUN_CONTRACT.json")
    args = parser.parse_args()
    try:
        data = load(Path(args.path))
    except ValueError as exc:
        return fail([str(exc)])
    errors = validate(data)
    if errors:
        return fail(errors)
    print(f"Run contract valid: {data['run_id']} tasks={len(data['tasks'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
