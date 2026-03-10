---
name: harness-develop
description: Implement one phase from a work item plan under docs/exec-plans/current/ using the repository contract as the source of truth.
examples:
  - "$harness-develop docs/exec-plans/current/gradebook-overrides phase=2"
  - "$harness-develop docs/exec-plans/current/platform-modernization/gradebook-overrides phase=2"
when_to_use:
  - "PRD, FDD, and plan exist and implementation is requested for a specific phase."
  - "Work requires tests and validation closure."
when_not_to_use:
  - "Required planning inputs are missing."
  - "Task is low-ceremony prototype work (use $harness-prototype)."
---

## Required Resources
Always load before coding:

- `references/persona.md`
- `references/approach.md`
- `references/coding_guidelines.md`
- `references/stack_practices.md`
- `references/ui_boundaries.md`
- `references/development_checklist.md`
- `references/output_requirements.md`
- `references/definition_of_done.md`
- `references/validation.md`
- `assets/templates/phase_execution_record_template.md`
- repository context: `ARCHITECTURE.md`, `harness.yml`, `docs/PRODUCT_SENSE.md`, 
- Read `docs/FRONTEND.md`, `docs/BACKEND.md`, `docs/CODEREVIEW.md` when enabled, and the work item docs

## Workflow
1. Resolve the work item directory.
2. Read `prd.md`, `fdd.md`, `plan.md`, and relevant `design/*.md` files.
3. If a phase selector is provided, implement only that phase.
4. Resolve `<skills_root>` as the directory that contains the installed harness skills (`develop/`, `validate/`, etc.). Do not resolve script paths relative to the repository or current working directory.
5. Run `python3 <skills_root>/validate/scripts/validate_work_item.py <work_item_dir> --check all` before coding.
6. Implement only the approved scope and keep a running execution record using the template.
7. Run repository-local verification and test commands from `docs/TOOLING.md` and `docs/TESTING.md`.
8. If code review is enabled in `harness.yml`, run at least one `$harness-review` round after tests pass.
9. Sync work-item docs when implementation diverges.
10. Run `python3 <skills_root>/validate/scripts/validate_work_item.py <work_item_dir> --check all` after implementation.
11. Final-phase only, run the requirements verification commands.
