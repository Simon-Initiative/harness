---
name: harness-validate
description: Optionally check selected artifact presence and structured requirements.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Run `python3 <this-skill>/scripts/validate_work_item.py <work-item> --workflow feature` for a nonempty plan plus required structured requirements. `--workflow work`, `bug`, or `prototype` requires only the work directory; `epic` requires a nonempty plan. Existing requirements are validated in every workflow. Use `--check prd|fdd|plan|design --file <relative-path>` to check a selected artifact (file override only for design), or `--check requirements` for required requirements alone.

This utility checks nonempty selected files and the canonical requirements schema/evidence paths. It does not check heading order, prose quality, Markdown links/anchors, forbidden words, execution success or semantic coverage. Open questions and deferred work are allowed. Diagnose failures without reading script source or producing a report file.

Resolve `<this-skill>` from the invoked skill's actual location, not the working repository. Installed links are named `harness-validate`, not `validate`. Python helpers resolve their own real path before importing sibling implementation. PyYAML is required.
