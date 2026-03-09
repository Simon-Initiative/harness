---
name: harness-validate
description: Validate a work item directory under docs/exec-plans/current/ by checking required files, headings, unresolved TODO markers, and markdown structure.
examples:
  - "$harness-validate docs/exec-plans/current/docs-import"
  - "$harness-validate docs/exec-plans/current/course-authoring/docs-import"
when_to_use:
  - "Before handing work-item artifacts to implementation."
  - "After editing PRD, FDD, plan, or design docs."
when_not_to_use:
  - "The task is writing docs from scratch and no validation is needed yet."
---

## Required Resources
Always load before validating:

- `references/validation_rules.md`
- `references/link_validation_notes.md`
- `references/definition_of_done.md`
- `assets/templates/validation_report_template.md`
- `scripts/validate_work_item.py`
