---
name: harness-epic
description: Create or update an epic-level lane plan under docs/exec-plans/current/ from informal source material. Use when an epic spans many related features and needs a parent plan.md that groups those features into a small number of feature lanes, documents lane ownership boundaries, and determines lane dependencies rather than creating a phase-by-phase implementation plan for one feature.
---

# Harness Epic

Create an epic-level lane plan, usually `<epic_dir>/plan.md`, from `informal.md`, existing parent docs, and relevant child feature docs.

A feature lane is a group of related features within an epic. Lanes should make the full epic easier to reason about, provide practical work boundaries for a single engineer or tightly coordinated owner, and clarify which groups of work are serial versus parallel. Features within a lane are usually worked serially by one engineer unless the plan explicitly says otherwise.

## Required Inputs

Load these when present:

- `<epic_dir>/informal.md`
- `<epic_dir>/requirements.md`
- `<epic_dir>/approach.md`
- `<epic_dir>/plan.md` if updating
- Child feature `informal.md`, `prd.md`, `fdd.md`, `plan.md`, and `requirements.yml` only as needed to understand current decomposition
- `references/lane_plan_guidance.md`
- `assets/templates/epic_plan_template.md`

If repo-level guidance exists, skim only the relevant files needed for documentation conventions, such as `AGENTS.md`, `harness.yml`, or nearby epic examples.

## Workflow

1. Resolve the epic directory under `docs/exec-plans/current/`.
2. Read the informal source and nearby parent docs. Treat `informal.md` as the primary input for suggested lane boundaries and feature allocation.
3. Inspect sibling or child feature directories enough to understand existing feature docs, tickets, and local documentation style.
4. Decide whether the output is a new lane plan or an update to an existing lane plan.
5. Organize all epic features into a small number of named lanes. Prefer the user-suggested lanes from `informal.md` unless dependencies, ownership boundaries, or coupling make a different grouping clearly better.
6. For each lane, document scope, proposed serial order, dependency notes, and cross-lane dependencies.
7. Determine lane dependencies so the team can see which lanes can start immediately, which lanes are blocked, and which lanes can run in parallel.
8. Write or update `<epic_dir>/plan.md` as a high-level parent plan, not a tactical implementation plan.
9. Include a lane dependency graph when there is more than one lane or when the graph clarifies immediate-start versus blocked work.
10. Include a suggested global execution shape that summarizes lane ordering and parallelization.
11. Call out clarifications, assumptions, cross-cutting hardening, and decision-log entries when useful.
12. Do not create child PRDs/FDDs/requirements/plans unless the user explicitly asks.

## Output Rules

- Use repository-relative paths in plan text.
- Keep implementation tasks high-level. Do not write detailed phase tasks, test commands, or line-item coding checklists for the whole epic.
- Preserve clear lane boundaries. Each lane should represent a coherent grouping of related features, not a vague phase, sprint, team label, or arbitrary time box.
- Treat features, tickets, and child work items as lane scope entries. Do not organize the parent plan around "feature slices."
- Keep each lane's proposed serial order dependency-first, then risk reduction, then workflow completion.
- Make dependencies explicit: "Lane X depends on Lane Y because..." and call out material ticket-level constraints inside the lane when needed.
- Add a Mermaid lane dependency graph for multi-lane epics; keep node labels concise and aligned with lane names.
- Mark lanes with no inbound dependencies as immediate-start lanes in the Mermaid graph when helpful.
- Include likely child directories when helpful, but avoid creating empty directories unless requested.
- If updating an existing plan, preserve useful existing content and revise only what the new source requires.

## Hand-Off Pattern

End with the recommended next lane or feature to document and which Harness skill should be used next:

- `harness-analyze` for a child `prd.md`
- `harness-architect` for a child `fdd.md`
- `harness-requirements` for child `requirements.yml`
- `harness-plan` for a child implementation `plan.md`
