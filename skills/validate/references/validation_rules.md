# Validation Rules

Core checks implemented by `scripts/validate_work_item.py`:

- required headings exist for each artifact type
- no unresolved `TODO`, `TBD`, or `FIXME` markers remain
- PRD requirements traceability points to `requirements.yml`
- plan phases are numbered and include a `Definition of Done` block
- markdown links are validated for local paths and anchors
