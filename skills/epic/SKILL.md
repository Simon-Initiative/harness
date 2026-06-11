---
name: harness-epic
description: Create or update an epic-level roadmap under docs/exec-plans/current/ from informal source material. Use when an epic is composed of multiple feature slices and needs a parent plan.md that sequences child work items, rather than a phase-by-phase implementation plan for a single feature.
examples:
  - "$harness-epic docs/exec-plans/current/epics/ab_testing"
  - "$harness-epic docs/exec-plans/current/epics/math"
when_to_use:
  - "An informal epic description exists and the user wants an epic roadmap."
  - "The work spans multiple features or child work items."
  - "The output should guide later PRD/FDD/requirements/implementation plans per feature slice."
when_not_to_use:
  - "A single feature already has PRD/FDD and needs an implementation plan; use $harness-plan."
  - "The user wants implementation or coding."
---

# Harness Epic

Create an epic-level roadmap, usually `<epic_dir>/plan.md`, from `informal.md`, existing parent docs, and relevant child feature docs.

## Required Inputs

Load these when present:

- `<epic_dir>/informal.md`
- `<epic_dir>/requirements.md`
- `<epic_dir>/approach.md`
- `<epic_dir>/plan.md` if updating
- Child feature `informal.md`, `prd.md`, `fdd.md`, `plan.md`, and `requirements.yml` only as needed to understand current decomposition
- `references/roadmap_guidance.md`
- `assets/templates/epic_plan_template.md`

If repo-level guidance exists, skim only the relevant files needed for documentation conventions, such as `AGENTS.md`, `harness.yml`, or nearby epic examples.

## Workflow

1. Resolve the epic directory under `docs/exec-plans/current/`.
2. Read the informal source and nearby parent docs.
3. Inspect sibling or child feature directories enough to infer established documentation style and decomposition.
4. Decide whether the output is a new roadmap or an update to an existing roadmap.
5. Write or update `<epic_dir>/plan.md` as a parent roadmap, not an implementation plan.
6. Sequence feature slices by dependency and risk.
7. For each feature slice, describe scope, exclusions, ordering rationale, and expected child artifacts.
8. Include a slice dependency graph when there is more than one non-linear dependency or when the graph would clarify parallelizable versus serial work.
9. Call out cross-cutting concerns, migration/cutover, observability, testing posture, and open questions.
10. Do not create child PRDs/FDDs/requirements/plans unless the user explicitly asks.

## Output Rules

- Use repository-relative paths in roadmap text.
- Keep implementation tasks high-level. Do not write detailed phase tasks, test commands, or line-item coding checklists for the whole epic.
- Preserve clear slice boundaries so follow-up skills can operate on one child feature at a time.
- Make dependencies explicit: "this comes before X because..."
- Add a Mermaid dependency graph for multi-slice epics when it improves readability; keep node labels concise and aligned with the feature slice names.
- Include likely child directories when helpful, but avoid creating empty directories unless requested.
- If updating an existing roadmap, preserve useful existing structure and revise only what the new source requires.

## Hand-Off Pattern

End with the recommended next child slice to document and which Harness skill should be used next:

- `harness-analyze` for a child `prd.md`
- `harness-architect` for a child `fdd.md`
- `harness-requirements` for child `requirements.yml`
- `harness-plan` for a child implementation `plan.md`
