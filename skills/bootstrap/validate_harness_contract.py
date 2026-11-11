#!/usr/bin/env python3
"""Validate the compact routing contract and optional version 1 capability policy."""
from pathlib import Path
import argparse
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'requirements/scripts'))
from requirements_trace import load
import yaml


def validate_contract(root):
    entry = root / 'AGENTS.md'
    if not entry.is_file() or not entry.read_text().strip():
        raise ValueError('AGENTS.md must be a nonempty routing entry point')
    policy = root / 'harness.yml'
    if not policy.exists(): return
    data = load(policy)
    if not isinstance(data, dict) or type(data.get('version')) is not int or data['version'] != 1:
        raise ValueError('harness.yml requires version: 1')
    caps = data.get('capabilities', {})
    if not isinstance(caps, dict): raise ValueError('capabilities must be a mapping')
    for name, cap in caps.items():
        if name not in {'feature_flags', 'telemetry', 'performance_requirements', 'code_review', 'issue_tracking'}:
            raise ValueError(f'unknown capability: {name}')
        if not isinstance(cap, dict) or cap.get('adoption') not in ('enabled', 'disabled') or cap.get('default') not in ('include', 'exclude'):
            raise ValueError(f'{name} needs adoption enabled/disabled and default include/exclude')
        if 'details_file' in cap:
            rel = cap['details_file']
            if not isinstance(rel, str) or not rel or Path(rel).is_absolute(): raise ValueError(f'invalid details_file for {name}')
            path = (root / rel).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file(): raise ValueError(f'missing or out-of-scope details_file for {name}')


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('repo_root', type=Path)
    a = p.parse_args()
    try: validate_contract(a.repo_root)
    except (OSError, ValueError, yaml.YAMLError) as exc: p.exit(1, f'ERROR: {exc}\n')
    print('Routing and optional policy structure valid; operational readiness not assessed.')
    return 0


if __name__ == '__main__': raise SystemExit(main())
