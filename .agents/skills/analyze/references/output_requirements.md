# Output Requirements (PRD)

Produce only the PRD body in markdown with these headings in this exact order:

1. Overview
2. Background & Problem Statement
3. Goals & Non-Goals
4. Users & Use Cases
5. UX / UI Requirements
6. Functional Requirements
7. Acceptance Criteria (Testable)
8. Non-Functional Requirements
9. Data, Interfaces & Dependencies
10. Repository & Platform Considerations
11. Feature Flagging, Rollout & Migration
12. Telemetry & Success Metrics
13. Risks & Mitigations
14. Open Questions & Assumptions
15. QA Plan
16. Definition of Done

For any section where there are no requiements (for instance, if feature flagging is NOT enabled in the target repo, simply include "N/A" as the body for the content of that section)

## Section Rules

- `Functional Requirements` must contain exactly: `Requirements are found in requirements.yml`
- `Acceptance Criteria (Testable)` must contain exactly: `Requirements are found in requirements.yml`
- Do not duplicate FR or AC entries in `prd.md`
- When feature flags are not in scope, include exactly: `No feature flags present in this work item`
- Keep QA focused on realistic automated and manual verification expected by the repository
