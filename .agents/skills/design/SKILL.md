---
name: harness-design
description: Produce a slice-level detailed design doc at <work_item_dir>/design/<slice_slug>.md by mapping slice responsibilities, interfaces, edge cases, and tests to the work item requirements.
examples:
  - "$harness-design docs/exec-plans/current/gradebook-overrides slice=late-penalty-ui"
  - "$harness-design docs/exec-plans/current/platform-modernization/gradebook-overrides slice=late-penalty-ui"
when_to_use:
  - "PRD/FDD exist and one implementation slice needs deeper design."
  - "A planned phase needs concrete signatures and edge-case handling before coding."
when_not_to_use:
  - "Task is feature-level architecture (use $harness-architect)."
  - "Task is immediate implementation (use $harness-develop)."
---

## Required Resources
Always load before writing:

- `references/design_checklist.md`
- `references/definition_of_done.md`
- `references/validation.md`
- `assets/templates/design_slice_template.md`
- `<work_item_dir>/prd.md`
- `<work_item_dir>/fdd.md`
- `<work_item_dir>/plan.md` when present

## Workflow
1. Resolve the work item directory.
2. Create or update `<work_item_dir>/design/<slice_slug>.md`.
3. Use `assets/templates/design_slice_template.md` as the structure.
4. Map the slice back to the work item requirements and implementation plan.
5. Use repository-local testing and operations docs plus `harness.yml` to decide which cross-cutting concerns need to be called out.
6. Run `python3 .agents/skills/validate/scripts/validate_work_item.py <work_item_dir> --check design --file <work_item_dir>/design/<slice_slug>.md`.
