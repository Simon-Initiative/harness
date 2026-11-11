---
name: harness-bootstrap
description: Add a compact repository routing entry point while preserving existing documentation.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Inspect the target repository and existing instructions, architecture and command documentation. Run `python3 <this-skill>/seed_harness_contract.py <target-repo>` using the invoked skill's actual location. The script creates only a missing `AGENTS.md` and preserves every existing file.

Adapt the new routing entry point to substantive existing architecture, commands/testing, and applicable policy; add domain documents only when the repository needs them. Do not overwrite substantive instructions, seed placeholder integrations, or infer operational readiness from path existence. Existing legacy contracts remain usable and are not deleted.

Preserve application-defined review orchestration. Point to an existing `docs/CODEREVIEW.md` or the review entry point configured in `capabilities.code_review.details_file`, including its reviewer/checklist selection rules. These reviewers run within the single final review stage. Do not create an empty review document or replace specialist reviewers with the harness's general reviewer.

Optional `harness.yml` retains version 1 capability policy: disabled adoption disables automatic use; enabled/include means default consideration when relevant; enabled/exclude means opt-in. Absent code-review policy defaults to one final review. Explicit review requests always run. Other absent capabilities imply no integration. Details paths are optional and read when relevant.

Run `python3 <this-skill>/validate_harness_contract.py <target-repo>`. Report created/reused paths, substantive routing updates, validation results and missing knowledge. Validation checks structure, not readiness.
