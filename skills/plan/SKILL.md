---
name: harness-plan
description: Convert PRD and FDD into a dependency-ordered implementation plan in a work item directory under docs/exec-plans/current/ with explicit gates and verification notes.
examples:
  - "$harness-plan docs/exec-plans/current/gradebook-overrides"
  - "$harness-plan docs/exec-plans/current/platform-modernization/gradebook-overrides"
when_to_use:
  - "PRD/FDD are present and implementation planning is required."
  - "A phased execution plan is needed before coding."
when_not_to_use:
  - "PRD/FDD are missing (use $harness-analyze and $harness-architect first)."
  - "Task is direct coding (use $harness-develop)."
---

## Required Resources
Always load before planning:

- `references/persona.md`
- `references/approach.md`
- `references/planning_considerations.md`
- `references/output_requirements.md`
- `references/plan_checklist.md`
- `references/definition_of_done.md`
- `references/validation.md`
- `assets/templates/plan_template.md`
- `<work_item_dir>/prd.md`
- `<work_item_dir>/fdd.md`
- `ARCHITECTURE.md`
- `harness.yml`
- `docs/STACK.md`
- `docs/TOOLING.md`
- `docs/TESTING.md`
- `docs/PRODUCT_SENSE.md`
- `docs/FRONTEND.md`
- `docs/BACKEND.md`

## Workflow
1. Resolve the work item directory.
2. Read `prd.md` and `fdd.md`.
3. Create or update `plan.md` from the plan template.
4. Build numbered phases with tasks, testing tasks, gates, and dependencies.
5. Use `harness.yml` and repository docs to decide which cross-cutting concerns must be planned explicitly.
6. Run:
   - `python3 ../requirements/scripts/requirements_trace.py <work_item_dir> --action verify_plan`
   - `python3 ../requirements/scripts/requirements_trace.py <work_item_dir> --action master_validate --stage plan_present`
   - `python3 ../validate/scripts/validate_work_item.py <work_item_dir> --check plan`
