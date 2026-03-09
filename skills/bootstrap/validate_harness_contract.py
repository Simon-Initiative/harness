#!/usr/bin/env python3
"""Validate the required harness contract files in a repository."""

from __future__ import annotations

from pathlib import Path
import argparse
import sys

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


REQUIRED_FILES = [
    "AGENTS.md",
    "ARCHITECTURE.md",
    "harness.yml",
    "docs/CODEREVIEW.md",
    "docs/ISSUE_TRACKING.md",
    "docs/OPERATIONS.md",
    "docs/STACK.md",
    "docs/BACKEND.md",
    "docs/TESTING.md",
    "docs/TOOLING.md",
    "docs/DESIGN.md",
    "docs/FRONTEND.md",
    "docs/PLANS.md",
    "docs/PRODUCT_SENSE.md",
    "docs/QUALITY_SCORE.md",
    "docs/RELIABILITY.md",
    "docs/SECURITY.md",
    "docs/design-docs/index.md",
    "docs/design-docs/core-beliefs.md",
    "docs/exec-plans/tech-debt-tracker.md",
    "docs/generated/db-schema.md",
    "docs/product-specs/index.md",
    "docs/product-specs/new-user-onboarding.md",
]

REQUIRED_DIRS = [
    "docs/exec-plans/current",
    "docs/exec-plans/archive",
    "docs/references",
]

VALID_CAPABILITIES = {
    "feature_flags",
    "telemetry",
    "performance_requirements",
    "code_review",
    "issue_tracking",
}

VALID_ADOPTION = {"enabled", "disabled"}
VALID_DEFAULT = {"include", "exclude"}


def load_yaml(path: Path) -> dict:
    if yaml is None:
        raise RuntimeError("PyYAML is required to validate harness.yml")
    return yaml.safe_load(path.read_text()) or {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    errors: list[str] = []

    for rel in REQUIRED_DIRS:
        if not (root / rel).is_dir():
            errors.append(f"missing required directory: {rel}")

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"missing required file: {rel}")

    harness_path = root / "harness.yml"
    if harness_path.exists():
        try:
            data = load_yaml(harness_path)
            if data.get("version") != 1:
                errors.append("harness.yml must set version: 1")
            caps = data.get("capabilities")
            if not isinstance(caps, dict):
                errors.append("harness.yml must define capabilities as a mapping")
            else:
                for name in VALID_CAPABILITIES:
                    if name not in caps:
                        errors.append(f"harness.yml missing capability: {name}")
                        continue
                    entry = caps[name] or {}
                    if entry.get("adoption") not in VALID_ADOPTION:
                        errors.append(f"{name}.adoption must be one of {sorted(VALID_ADOPTION)}")
                    if entry.get("default") not in VALID_DEFAULT:
                        errors.append(f"{name}.default must be one of {sorted(VALID_DEFAULT)}")
                    details_file = entry.get("details_file")
                    if not isinstance(details_file, str) or not details_file:
                        errors.append(f"{name}.details_file must be set")
                    elif not (root / details_file).exists():
                        errors.append(f"{name}.details_file does not exist: {details_file}")
                unknown = set(caps.keys()) - VALID_CAPABILITIES
                if unknown:
                    errors.append(f"unknown capabilities in harness.yml: {sorted(unknown)}")
        except Exception as exc:  # pragma: no cover
            errors.append(f"failed to parse harness.yml: {exc}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Harness contract validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
