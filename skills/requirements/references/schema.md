# Canonical requirements

`version: 1` and a nonempty `requirements` list are required. Each requirement has
`id` (FR- followed by at least three digits), nonempty `title`, and nonempty nested
`acceptance_criteria`. Each criterion has `id` (AC- followed by at least three digits),
nonempty `title`, and optional `evidence` list. IDs are globally unique within their type.
Unknown fields, duplicate YAML keys, and unsupported versions are errors.

Evidence entries have `path` and `supports` (a nonempty explanation). Paths are
`work:relative/file` or `repo:relative/file`; the latter requires explicit `--repo-root`.
Files must exist and resolve inside their chosen root, including through symlinks.
URLs, anchors and line suffixes are unsupported; describe precise locations in `supports`.
Optional `command` and `result` must occur together and record actual execution,
including failures or unavailable checks honestly. Manual evidence can point to an
existing plan section describing the observation. Evidence can be absent while planning.

Validation establishes structure and file existence. It does not run checks, verify
recorded results, or prove semantic coverage. The implementing agent and final reviewer
assess coverage. Never insert IDs into production code to satisfy a scanner.

Capture requires explicit IDs and replaces supplied requirements in full (including
nested criteria); omitted requirements remain. Review intentional criterion removals.
An identical payload is safe to rerun. Invalid input leaves the existing file unchanged.

## Migration

Older nested files: retain IDs, titles and criteria; remove `feature`, `generated_from`,
`status` and `verification_method`. Convert each meaningful `proofs` entry manually to
an explicit evidence entry; do not discard evidence. Remove empty `proofs` lists.
Older top-level `acceptance_criteria`: explicitly assign each to its owning requirement
before capture. Remove `work_item`. No automatic ownership inference is safe.
Replace promotion/verify/master_validate commands with `--action validate` (or the
work-item validator when checking artifacts too). Their previous output was not proof
of execution or behavior. There is no status promotion lifecycle.
