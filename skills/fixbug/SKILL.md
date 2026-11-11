---
name: harness-fixbug
description: Investigate and fix a defect with regression protection and final review.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Establish expected versus actual behavior and investigate the root cause. Prefer demonstrating a failing regression test before the minimal fix. If reproduction or automation is impractical, record alternative evidence and environmental limits; never invent a failed test or treat unavailable checks as passing.

Implement the smallest safe fix, add practical regression protection, and run affected verification. Avoid unrelated refactors; update docs only for changed behavior contracts.

After the complete deliverable passes relevant verification, run `$harness-review` once unless automatic review is explicitly disabled in repository policy. A user-requested review still runs. Resolve substantive findings and rerun affected checks; broader re-review is needed only if the fixes justify it.

Report root cause, fix, regression evidence, check results and limits.
