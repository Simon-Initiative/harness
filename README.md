# Harness Engineering Skills

Reusable engineering skills for capable agents in Codex and Claude Code. Start with the
request, applicable repository instructions, the invoked skill and the artifact at hand.
Read code and domain guidance progressively as decisions require it. Reuse unchanged
context. Repository-specific rules and explicit user scope remain authoritative.

## Default workflows

| Work | Path |
| --- | --- |
| Bounded enhancement/refactor | `work` → implement and verify → final review |
| Bug | `fixbug` → reproduce/protect → fix and verify → final review |
| Substantial feature | `analyze` → `architect` when needed → `plan` → `develop` all remaining phases → final review |
| Difficult slice | Optional `design` to resolve a specific uncertainty |
| Multi-feature initiative | Optional `epic` for ownership, dependencies and concurrency |
| Experiment | `prototype` → smallest useful experiment/smoke check → report evidence and unknowns |

Public skill names remain `$harness-analyze`, `$harness-architect`, `$harness-plan`,
`$harness-develop`, `$harness-work`, `$harness-fixbug`, `$harness-review`,
`$harness-prototype`, `$harness-design`, `$harness-epic`, `$harness-requirements`,
`$harness-update_docs`, `$harness-validate`, and `$harness-bootstrap`.

An analysis/design/planning-only request stops at that scope. Implementation authorization
permits completing the plan without renewed approval at routine phase boundaries.
`develop phase=2` honors that selection; a non-final selected phase reports final review
pending. Explicitly separate PR deliverables each receive final review.

Review runs once after all implementation phases and relevant checks pass. Review the
whole deliverable against its base, including committed/uncommitted work, in a fresh
reviewer context where supported. Resolve substantive findings and verify fixes. If
independent execution is unavailable, label the fallback self-review honestly.
[Reviewer configuration](agents/reviewer.toml) preserves read-only isolation without
selecting a model; configure model preferences through the runtime or repository.

One final review is a stage that can include multiple application-defined reviewers.
At that stage, `harness-review` reads `capabilities.code_review.details_file` from
`harness.yml`, or falls back to an existing `docs/CODEREVIEW.md`, and follows applicable
`AGENTS.md` rules. That entry point controls reviewer selection and delegation. For
example, a repository can require separate security and performance subagents for every
deliverable, with backend, frontend or requirements reviewers selected by the changed
scope. Each selected reviewer gets its own guide and the complete deliverable base;
the coordinator waits for all reviewers and consolidates findings. Repository-specific
reviewers are not replaced by the generic harness reviewer. Bootstrap preserves and
links existing review guidance without requiring a placeholder review document.

## Artifacts and context

Small work can use a ticket and a short approach in chat. Substantial features normally
use a compact `prd.md`, canonical nested `requirements.yml`, optional `fdd.md`, and
checkbox `plan.md`, usually under `docs/exec-plans/current/<work-item>/`. Existing
specifications can substitute; do not manufacture missing PRDs or designs. Templates
are suggestions, not formatting gates. Optional slice designs resolve particular
uncertainties; epic plans coordinate feature ownership and dependencies.

Keep progress, blockers, material deviations and a concise final verification summary in
the plan or PR description. No phase execution record or duplicate decision logs are
required. Update requirements/product scope for acceptance changes, design for contract
changes, and plan for task order/progress. Never weaken requirements silently.

## Install

```bash
./bin/harness-install          # stable: newest release tag
./bin/harness-install latest   # default branch
./bin/harness-status
./bin/harness-update
```

The installer maintains a checkout at `~/.local/share/harness`, selecting existing
`~/.agents/skills` (Codex) and `~/.claude/skills` (Claude Code) targets, or creating both
if neither exists. It installs symlinks inside a collision-safe `harness`/`harness_1`
namespace using metadata names, e.g. `harness-validate`, not source folder `validate`.
[install.sh](install.sh) is the clone-and-delegate entry point. Version metadata remains
in `version.json`; this change does not publish a release.

Use an interpreter with Python 3.10+ and PyYAML (`python -m pip install PyYAML` in your
chosen virtual environment). Scripts are invoked from the actual skill location. They
resolve symlinks before locating internal helpers; do not infer sibling paths from
source folder names in the installed namespace. Keep the complete source checkout;
copying individual skill directories is unsupported for helpers that share code.

## Compact bootstrap and policy

`$harness-bootstrap` creates only a missing `AGENTS.md` routing entry point. It preserves
all existing documentation and points to substantive architecture, commands/testing,
and applicable policy as discovered. Add domain documents only when needed. Empty
repositories still require investigation and useful routing; path existence is not
operational readiness. The seed script has no overwrite/force option.

`harness.yml` is optional. Version 1 capability entries remain compatible:

```yaml
version: 1
capabilities:
  code_review:
    adoption: enabled
    default: include
    # details_file: docs/CODEREVIEW.md  # optional, must exist if supplied
```

For retained capabilities (`feature_flags`, `telemetry`, `performance_requirements`,
`code_review`, `issue_tracking`), disabled adoption disables automatic use;
enabled/include means consider by default when relevant; enabled/exclude is opt-in.
This is agent policy, not a script-driven orchestrator. Omitted review policy defaults
to one final review; other omitted capabilities imply no integration. Explicitly
requested review runs even with automatic review disabled. Legacy provider/link metadata
is tolerated but not validated or consumed by the compact validator.

## Validation commands and guarantees

From the source checkout (substitute the installed skill's actual path as needed):

```bash
python skills/validate/scripts/validate_work_item.py WORK_ITEM --workflow feature
python skills/validate/scripts/validate_work_item.py WORK_ITEM --workflow work
python skills/validate/scripts/validate_work_item.py WORK_ITEM --check fdd
python skills/requirements/scripts/requirements_trace.py WORK_ITEM --action capture --bulk-file payload.yml
python skills/bootstrap/seed_harness_contract.py TARGET_REPO
python skills/bootstrap/validate_harness_contract.py TARGET_REPO
```

- `feature` requires a nonempty plan and valid requirements. `epic` requires a nonempty
  plan. `work`, `bug`, and `prototype` need only an existing work directory. Any present
  requirements file is validated. Selected `prd`, `fdd`, `plan`, or `design` checks require
  only that artifact (plus any present requirements); `--check requirements` requires YAML.
- Requirements validation checks the [canonical schema](skills/requirements/references/schema.md),
  unique IDs, nested criteria and explicit evidence files. Use `--repo-root REPO` for
  `repo:` evidence; `work:` paths resolve relative to the work item. Capture replaces
  supplied requirements by stable ID, including their full criteria; omitted requirements
  remain. Identical input is idempotent and errors leave existing content unchanged.
- Bootstrap validation requires nonempty `AGENTS.md`; optional capability policy must be
  structurally valid and any specified details paths must exist within the repository.

These checks do not enforce headings, boilerplate, Markdown links/anchors, or forbidden
words. They do not establish operational readiness, execution success or semantic
coverage. Actual check results must be recorded honestly; agents and final reviewers
assess whether evidence supports each criterion. Source-code AC tokens prove nothing.

## Migration

Existing extra repository documents remain useful; nothing deletes them. Remove old
mandatory-read and per-phase-review rules from repository-local instructions only when
authorized; skills continue to honor those explicit rules. No policy rewrite is required
for legacy version 1 configurations, but integrations should only be enabled when real.

Requirements keep nested criteria and stable IDs. Remove promotion/status metadata and
convert meaningful old proofs to explicit evidence, following the short
[schema migration notes](skills/requirements/references/schema.md). Top-level criteria
need explicit assignment to owning requirements; unsupported formats fail with a diagnostic.
Old promotion/verification commands are removed; use `--action validate` or the work-item
validator, not both for the same input. `--check all` is replaced by `--workflow feature`;
`validate_spec_pack.py` remains a deprecated wrapper for that workflow. Design `--file`
is relative to the work item. Old phase records may remain historical but are not required.

## Checks for this repository

```bash
python -m unittest discover -s tests -v
bash -n install.sh bin/harness-install bin/harness-update bin/harness-status bin/libharness.sh
```

Tests exercise schema failures, evidence paths, safe repeated updates, compact workflows,
bootstrap preservation and actual namespaced installation links in temporary directories.
[Workflow dry runs](tests/workflow-dry-runs.md) document instruction-level assessment;
they do not prove live runtime agent behavior. No issue mutations, production actions,
or releases are needed to test the harness.
