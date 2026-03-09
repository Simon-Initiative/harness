# Input Resolution

Accept any of:

- explicit work item directory path(s), for example `docs/exec-plans/current/<feature_slug>` or `docs/exec-plans/current/<epic_slug>/<feature_slug>`
- changed file list
- branch or diff context

Resolve work item directories in this order:

1. use explicit work item input when provided
2. extract from changed paths under `docs/exec-plans/current/`
3. if still unknown, infer from nearest touched work-item docs or ask the user
