# Representative workflow dry runs

These are static instruction walkthroughs using the revised skills, supplemented by
executable artifact/path tests in `test_harness.py`. They are not claims that a real
agent ran each workflow or that natural-language policy is deterministically enforced.

| Scenario/input | Walkthrough and expected boundary |
| --- | --- |
| Bug: parser accepts empty file | `fixbug` records expected rejection and actual acceptance, adds failing regression when practical, makes minimal fix, runs affected checks, then one final review. Unavailable reproduction is recorded as a limit. |
| Bounded enhancement: add optional flag | `work` states short chat approach and implements authorized change without a spec pack or approval pause; verifies and reviews complete change. Empty work-directory validator fixture passes. |
| Feature: two ordered phases, parser then caller | `develop` without selector completes parser and caller with affected checks, tracks both in plan, then reviews both against the pre-feature base once. Compact plan plus nested requirements fixture passes. |
| Selected phase 1 of 2 | `develop phase=1` completes only phase 1 and its checks, reports final review pending, and does not trigger automatic formal review. |
| Prototype: measure parser feasibility | `prototype` runs smallest useful smoke experiment, reports observed evidence and unknowns; skips broad regression/hardening. No spec pack needed. Delivered code gets final review unless disabled. |
| Epic: parser and UI owners | `epic` records ownership, dependency on parser interface, independent work that can proceed; diagram only if helpful. No child documents manufactured. Plan-only fixture passes. |
| Legacy repository | Seed preserves existing instructions and architecture; existing valid version 1 policy remains accepted; extra docs are not removed. Unit fixture covers preservation and disabled review configuration. |
| Explicit review with automatic review disabled | `review` honors explicit request, inspects full requested diff and authoritative requirements independently; disabled automatic gate does not suppress requested review. |
| Application-defined reviewers (Torus policy) | `harness.yml` points to `docs/CODEREVIEW.md`. For a deliverable changing Elixir and TypeScript/React UI, select security and performance plus Elixir, UI and TypeScript; add Gleam or requirements only when their documented triggers apply. Delegate each selected guide to a separate reviewer within one final stage, using the complete deliverable base. Wait, merge and deduplicate. A selected non-final phase does not start this stage. |
| Review policy at a custom path or without harness.yml | Follow the configured `details_file` when supplied; otherwise consult existing `docs/CODEREVIEW.md` and applicable repository instructions. Missing configured policy is reported. Unavailable independent execution is disclosed per selected lens, not reported as completed specialist review. |

Review scheduling above is assessed from instructions, not from an execution engine.
A later small comparison on representative real tasks could test agent adherence without
adding a benchmark framework. Final review of this change is recorded in the completion report.
