---
name: harness-update_docs
description: Reconcile work-item docs after implementation drift by updating PRD, FDD, and plan artifacts under docs/exec-plans/current/ and re-validating them.
examples:
  - "$harness-update_docs docs/exec-plans/current/docs-import"
  - "$harness-update_docs docs/exec-plans/current/course-authoring/docs-import"
when_to_use:
  - "Implementation has drifted from the documented plan or design."
  - "Validation is failing and the task is to repair work-item artifacts."
when_not_to_use:
  - "Net-new feature definition before coding."
---

## Required Resources
Always load before updating docs:

- `references/decision_log.md`
- `references/drift_mapping.md`
- `references/input_resolution.md`
- `references/definition_of_done.md`
- `references/validation.md`
- `assets/templates/decision_entry_template.md`
