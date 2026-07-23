# Epic Lane Plan Guidance

An epic lane plan is a parent planning artifact for a body of work composed of many related features. It should group all epic features into a small number of lanes, explain why those groupings are coherent, and make lane dependencies clear enough that the team knows where to start.

A lane is a group of related features, tickets, or child work items. It is usually the work boundary for one engineer or tightly coordinated owner. Features inside a lane are typically worked serially, so lane ordering should be deliberate.

## Plan Shape

Use this structure unless the repository has a stronger local convention:

- Context references
- Why We Are Organizing By Lanes
- Lane Summary
- Clarifications and Assumptions
- One section per lane, using `## Lane N: <Lane Name>`
- Suggested Global Execution Shape
- Lane Dependency Flow (Mermaid)
- Open Questions
- Decision Log, when updating or when sequencing decisions need durable rationale
- Recommended Next Work, when a handoff is useful

## Lane Entry

For each lane, include:

- `Scope`: feature tickets, child work items, and relevant local docs assigned to the lane
- `Proposed Serial Order`: numbered feature order inside the lane
- `Dependency Notes`: why the lane's internal ordering is appropriate
- `Cross-Lane Dependencies`: inbound and outbound dependencies, including immediate-start status when there is no inbound lane dependency

## Good Lanes

Good lanes group features that share a coherent product area, implementation surface, or dependency boundary. Examples:

- data infrastructure and contracts that unblock all feature surfaces
- shell/navigation/layout work that establishes user workflow foundations
- core UI tiles or panels that share data contracts and interaction patterns
- AI recommendation features that share prompt, context, feedback, or regeneration infrastructure
- export/release hardening work that depends on stable scoped data behavior
- correctness stabilization work that should land before broad structural model changes

Avoid lanes that are only team names, vague phases, arbitrary time boxes, or unrelated grab bags. Also avoid turning every feature into its own lane; the point is to make the epic easier to understand by grouping related features.

## Lane Dependencies

Lane dependencies should be lane-level by default:

- no inbound lane dependency means the lane can start immediately
- hard dependency means the dependent lane should wait for the upstream lane to complete
- soft dependency means the dependent lane can begin, but should align with the upstream lane's outputs or conventions
- ticket-level constraints should be called out only when they materially affect sequencing

The global execution shape should summarize which lanes start first, which lanes can run in parallel, and where final integration or hardening belongs.

## Lane Plan Versus Implementation Plan

An epic lane plan says:

- what lanes exist
- which features belong in each lane
- why those groupings and lane orders matter
- which lanes can start immediately
- how lanes depend on each other, summarized in a concise Mermaid graph when useful
- what assumptions or unresolved questions affect lane sequencing

An implementation plan says:

- exact phases
- engineering tasks
- test commands
- gates for one feature
- definitions of done

If the requested artifact is for a single feature with PRD/FDD, use `harness-plan` instead.
