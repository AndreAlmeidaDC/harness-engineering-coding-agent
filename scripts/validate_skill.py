from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required_files = [
    "SKILL.md",
    "README.md",
    "references/product-engineering-discovery.md",
    "references/prd-specification-builder.md",
    "references/semantic-system-design.md",
    "references/version-check.md",
    "references/release-measurement-loop.md",
    "references/squad-mode.md",
    "docs/academic-foundations.md",
    "templates/AGENTS.md",
    "templates/CONTRACT.md",
    "templates/SEMANTIC_SPEC.md",
    "templates/DECISION_GRILL.md",
    "templates/ACCEPTANCE_CRITERIA.md",
    "templates/TEST_PLAN.md",
    "templates/EVALUATION_REPORT.md",
    "templates/HANDOFF.md",
    "templates/STATE.md",
]

errors = []
skill = ROOT / "SKILL.md"
if not skill.exists():
    errors.append("Missing SKILL.md")
else:
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    if "name: harness-engineering-coding-agent" not in text:
        errors.append("SKILL.md frontmatter must include the expected name")
    if "description:" not in text:
        errors.append("SKILL.md frontmatter must include description")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md should stay under 500 lines")

for rel in required_files:
    if not (ROOT / rel).exists():
        errors.append(f"Missing required file: {rel}")

if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed.")
