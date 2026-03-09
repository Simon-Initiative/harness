#!/usr/bin/env python3
"""Manage and validate requirements.yml traceability for harness work items."""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"ERROR: PyYAML is required: {exc}")
    raise SystemExit(1)

AC_PATTERN = re.compile(r"\bAC-\d{3}\b")
FR_PATTERN = re.compile(r"\bFR-\d{3}\b")


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text()) or {}


def dump_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def requirements_path(work_item_dir: Path) -> Path:
    return work_item_dir / 'requirements.yml'


def ensure_doc(work_item_dir: Path) -> dict:
    path = requirements_path(work_item_dir)
    if path.exists():
        return load_yaml(path)
    return {'work_item': work_item_dir.name, 'requirements': [], 'acceptance_criteria': []}


def validate_doc(doc: dict) -> list[str]:
    errors: list[str] = []
    seen_fr = set()
    seen_ac = set()
    for item in doc.get('requirements', []):
        rid = item.get('id')
        if not rid:
            errors.append('requirement entry missing id')
        elif rid in seen_fr:
            errors.append(f'duplicate requirement id: {rid}')
        else:
            seen_fr.add(rid)
    for item in doc.get('acceptance_criteria', []):
        aid = item.get('id')
        if not aid:
            errors.append('acceptance criterion entry missing id')
        elif aid in seen_ac:
            errors.append(f'duplicate acceptance criterion id: {aid}')
        else:
            seen_ac.add(aid)
    return errors


def next_id(prefix: str, existing: list[str]) -> str:
    nums = [int(x.split('-')[1]) for x in existing if x.startswith(prefix + '-')]
    return f"{prefix}-{(max(nums) + 1) if nums else 1:03d}"


def action_capture(work_item_dir: Path, bulk_file: str | None) -> int:
    doc = ensure_doc(work_item_dir)
    if not bulk_file:
        print('ERROR: --bulk-file is required for capture')
        return 1
    bulk_path = Path(bulk_file)
    if not bulk_path.is_absolute():
        bulk_path = (work_item_dir / bulk_file).resolve()
    payload = load_yaml(bulk_path)
    fr_existing = [x.get('id', '') for x in doc.get('requirements', [])]
    ac_existing = [x.get('id', '') for x in doc.get('acceptance_criteria', [])]
    for item in payload.get('requirements', []):
        entry = dict(item)
        entry.setdefault('id', next_id('FR', fr_existing))
        fr_existing.append(entry['id'])
        doc.setdefault('requirements', []).append(entry)
    for item in payload.get('acceptance_criteria', []):
        entry = dict(item)
        entry.setdefault('id', next_id('AC', ac_existing))
        ac_existing.append(entry['id'])
        doc.setdefault('acceptance_criteria', []).append(entry)
    errors = validate_doc(doc)
    if errors:
        for error in errors:
            print(f'ERROR: {error}')
        return 1
    dump_yaml(requirements_path(work_item_dir), doc)
    print(f'Captured requirements into {requirements_path(work_item_dir)}')
    return 0


def action_validate_structure(work_item_dir: Path) -> int:
    doc = load_yaml(requirements_path(work_item_dir))
    errors = validate_doc(doc)
    if errors:
        for error in errors:
            print(f'ERROR: {error}')
        return 1
    print('requirements.yml structure is valid')
    return 0


def refs_in_file(path: Path) -> tuple[set[str], set[str]]:
    if not path.exists():
        return set(), set()
    text = path.read_text()
    return set(FR_PATTERN.findall(text)), set(AC_PATTERN.findall(text))


def verify_doc_refs(doc: dict, refs: tuple[set[str], set[str]], label: str) -> int:
    _fr_refs, ac_refs = refs
    missing = []
    for item in doc.get('acceptance_criteria', []):
        if item.get('id') not in ac_refs:
            missing.append(item.get('id'))
    if missing:
        print(f'ERROR: missing {label} references for: {missing}')
        return 1
    print(f'{label} references verified')
    return 0


def action_verify_fdd(work_item_dir: Path) -> int:
    doc = load_yaml(requirements_path(work_item_dir))
    return verify_doc_refs(doc, refs_in_file(work_item_dir / 'fdd.md'), 'fdd')


def action_verify_plan(work_item_dir: Path) -> int:
    doc = load_yaml(requirements_path(work_item_dir))
    return verify_doc_refs(doc, refs_in_file(work_item_dir / 'plan.md'), 'plan')


def action_verify_implementation(work_item_dir: Path) -> int:
    doc = load_yaml(requirements_path(work_item_dir))
    repo_root = work_item_dir
    while repo_root != repo_root.parent and not (repo_root / '.git').exists():
        repo_root = repo_root.parent
    refs = set()
    for path in repo_root.rglob('*'):
        if path.is_file() and path.suffix in {'.py', '.js', '.ts', '.tsx', '.ex', '.exs', '.rb', '.go', '.java', '.kt', '.rs'}:
            refs.update(AC_PATTERN.findall(path.read_text(errors='ignore')))
    missing = [item.get('id') for item in doc.get('acceptance_criteria', []) if item.get('id') not in refs]
    if missing:
        print(f'ERROR: missing implementation proof for: {missing}')
        return 1
    print('implementation references verified')
    return 0


def action_master_validate(work_item_dir: Path, stage: str | None) -> int:
    doc = load_yaml(requirements_path(work_item_dir))
    errors = validate_doc(doc)
    if errors:
        for error in errors:
            print(f'ERROR: {error}')
        return 1
    if stage == 'fdd_only':
        return action_verify_fdd(work_item_dir)
    if stage == 'plan_present':
        return max(action_verify_fdd(work_item_dir), action_verify_plan(work_item_dir))
    if stage == 'implementation_complete':
        return max(action_verify_fdd(work_item_dir), action_verify_plan(work_item_dir), action_verify_implementation(work_item_dir))
    print('requirements.yml master validation passed')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('work_item_dir', help='Work item dir, e.g. docs/exec-plans/current/my-work-item')
    parser.add_argument('--action', required=True)
    parser.add_argument('--stage')
    parser.add_argument('--bulk-file')
    args = parser.parse_args()

    work_item_dir = Path(args.work_item_dir)
    if not work_item_dir.exists():
        print(f'ERROR: work item directory not found: {work_item_dir}')
        return 1

    if args.action == 'capture':
        return action_capture(work_item_dir, args.bulk_file)
    if args.action == 'validate_structure':
        return action_validate_structure(work_item_dir)
    if args.action == 'verify_fdd':
        return action_verify_fdd(work_item_dir)
    if args.action == 'verify_plan':
        return action_verify_plan(work_item_dir)
    if args.action == 'verify_implementation':
        return action_verify_implementation(work_item_dir)
    if args.action == 'master_validate':
        return action_master_validate(work_item_dir, args.stage)
    print(f'ERROR: unsupported action: {args.action}')
    return 1


if __name__ == '__main__':
    sys.exit(main())
