---
name: harness-requirements
description: Manage deterministic FR and AC traceability in <work_item_dir>/requirements.yml across PRD, FDD, plan, and implementation proof artifacts.
examples:
  - "$harness-requirements docs/exec-plans/current/gradebook-overrides --action capture"
  - "$harness-requirements docs/exec-plans/current/platform-modernization/gradebook-overrides --action verify_plan"
when_to_use:
  - "requirements.yml must be initialized, validated, or promoted through traceability stages."
  - "A deterministic machine-enforced requirements gate is needed."
when_not_to_use:
  - "The task is drafting PRD, FDD, or plan content itself."
---

## Required Resources
Always load before running:

- `references/schema.md`
- `references/stages.md`
- `assets/templates/requirements_template.yml`
- `scripts/requirements_trace.py`
