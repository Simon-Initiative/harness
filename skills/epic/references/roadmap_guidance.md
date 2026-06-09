# Epic Roadmap Guidance

An epic roadmap is a parent planning artifact for a body of work composed of multiple feature slices. It should explain what order the slices should be tackled in and why. It should not be a tactical implementation plan for the entire epic.

## Roadmap Shape

Use this structure unless the repository has a stronger local convention:

- Purpose
- Core Direction
- Current Foundation
- Sequencing Principles
- Feature Sequence
- Cross-Cutting Concerns
- Suggested Child Artifacts
- Open Questions

## Feature Slice Entry

For each feature slice, include:

- slice name and likely directory slug
- what the slice delivers
- what it intentionally excludes
- dependencies
- why it comes at this point in the sequence
- likely follow-up artifacts, usually `informal.md`, `prd.md`, `fdd.md`, `requirements.yml`, and `plan.md`

## Good Slices

Good feature slices are bounded by stable interfaces or dependency layers. Examples:

- shared contract before runtime behavior
- runtime behavior before authoring UI
- persistence and migration before cutover
- outcome/reward plumbing before adaptive algorithms
- analytics after assignment/exposure data exists

Avoid slices that are only team names, vague phases, or arbitrary time boxes.

## Roadmap Versus Implementation Plan

An epic roadmap says:

- what feature slices exist
- why their order matters
- what each slice should produce
- what risks and unknowns affect the sequence

An implementation plan says:

- exact phases
- engineering tasks
- test commands
- gates for one feature
- definitions of done

If the requested artifact is for a single feature with PRD/FDD, use `harness-plan` instead.
