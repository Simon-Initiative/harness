---
name: harness-architect
description: Transform a PRD into a practical FDD in a work item directory under docs/exec-plans/current/ with concrete boundaries, interfaces, data impacts, and verification strategy.
examples:
  - "$harness-architect docs/exec-plans/current/gradebook-overrides"
  - "$harness-architect docs/exec-plans/current/platform-modernization/gradebook-overrides"
when_to_use:
  - "PRD exists and technical design decisions are needed."
  - "The team needs concrete boundaries and contracts before planning or coding."
when_not_to_use:
  - "PRD is missing (use $harness-analyze)."
  - "Task is direct implementation (use $harness-develop)."
---

## Required Resources
Always load before writing:

- `references/persona.md`
- `references/philosophy.md`
- `references/approach.md`
- `references/focus_areas.md`
- `references/output_requirements.md`
- `references/fdd_checklist.md`
- `references/definition_of_done.md`
- `references/validation.md`
- `assets/templates/fdd_template.md`
- repository context: `ARCHITECTURE.md`, `harness.yml`, `docs/STACK.md`, `docs/TOOLING.md`, `docs/TESTING.md`, `docs/PRODUCT_SENSE.md`, `docs/FRONTEND.md`, `docs/BACKEND.md`, `docs/DESIGN.md`, `docs/OPERATIONS.md`, and relevant files under `docs/design-docs/`

## Workflow
1. Resolve the work item directory under `docs/exec-plans/current/...`.
2. Read `<work_item_dir>/prd.md`.
3. Open or create `<work_item_dir>/fdd.md`.
4. Use `assets/templates/fdd_template.md` as the section structure.
5. Apply the reference files as hard guidance for boundaries, interfaces, risks, and verification.
6. Use `harness.yml` to determine whether feature flags, telemetry, performance requirements, code review, and issue tracking should appear by default.
7. Run:
   - `python3 ../requirements/scripts/requirements_trace.py <work_item_dir> --action verify_fdd`
   - `python3 ../requirements/scripts/requirements_trace.py <work_item_dir> --action master_validate --stage fdd_only`
   - `python3 ../validate/scripts/validate_work_item.py <work_item_dir> --check fdd`

## Output Contract
- Update `<work_item_dir>/fdd.md`.
- Final response: updated path, key decisions, unresolved questions.
