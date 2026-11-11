#!/usr/bin/env python3
"""Validate structure and explicit file references; never infer behavioral coverage."""
from pathlib import Path
import argparse
import os
import re
import tempfile
try:
    import yaml
except ImportError:
    raise SystemExit("ERROR: PyYAML is required; install it with python -m pip install PyYAML")


class UniqueLoader(yaml.SafeLoader):
    pass


def mapping(loader, node):
    result = {}
    for key, value in node.value:
        key = loader.construct_object(key)
        if not isinstance(key, str) or key in result:
            raise ValueError(f'duplicate or non-string YAML key: {key!r}')
        result[key] = loader.construct_object(value)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def load(path):
    return yaml.load(path.read_text(), Loader=UniqueLoader)


def fields(value, required, optional=()):
    if not isinstance(value, dict):
        raise ValueError('expected a mapping')
    missing = set(required) - value.keys()
    unknown = value.keys() - set(required) - set(optional)
    if missing or unknown:
        raise ValueError(f'missing fields {sorted(missing)}; unsupported fields {sorted(unknown)}. See requirements/references/schema.md for migration.')


def nonempty(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be a nonempty string')


def sequence(value, label):
    if not isinstance(value, list) or not value:
        raise ValueError(f'{label} must be a nonempty list')


def validate(doc, work, repo=None):
    fields(doc, ('version', 'requirements'))
    if type(doc['version']) is not int or doc['version'] != 1:
        raise ValueError('unsupported requirements version; expected 1')
    sequence(doc['requirements'], 'requirements')
    seen = set()
    def identifier(value, prefix):
        if not isinstance(value, str) or not re.fullmatch(prefix + r'-\d{3,}', value):
            raise ValueError(f'invalid {prefix} identifier: {value!r}')
        if value in seen:
            raise ValueError(f'duplicate identifier: {value}')
        seen.add(value)
    for fr in doc['requirements']:
        fields(fr, ('id', 'title', 'acceptance_criteria'))
        identifier(fr['id'], 'FR'); nonempty(fr['title'], 'requirement title')
        sequence(fr['acceptance_criteria'], 'acceptance_criteria')
        for ac in fr['acceptance_criteria']:
            fields(ac, ('id', 'title'), ('evidence',))
            identifier(ac['id'], 'AC'); nonempty(ac['title'], 'criterion title')
            evidence = ac.get('evidence', [])
            if not isinstance(evidence, list):
                raise ValueError('evidence must be a list')
            for ev in evidence:
                fields(ev, ('path', 'supports'), ('command', 'result'))
                nonempty(ev['supports'], 'evidence supports')
                nonempty(ev['path'], 'evidence path')
                prefix, sep, relative = ev['path'].partition(':')
                base = work if prefix == 'work' else repo if prefix == 'repo' else None
                if not sep or base is None or not relative or Path(relative).is_absolute():
                    raise ValueError('evidence path needs work:relative/file or repo:relative/file with --repo-root')
                base = base.resolve(); target = (base / relative).resolve()
                if not target.is_relative_to(base) or not target.is_file():
                    raise ValueError(f'invalid evidence path: {ev["path"]}')
                if ('command' in ev) != ('result' in ev):
                    raise ValueError('execution evidence requires both command and result')
                for key in ('command', 'result'):
                    if key in ev: nonempty(ev[key], key)
    return doc


def capture(work, payload, repo=None):
    incoming = validate(load(payload), work, repo)
    target = work / 'requirements.yml'
    current = validate(load(target), work, repo) if target.exists() else {'version': 1, 'requirements': []}
    by_id = {fr['id']: fr for fr in current['requirements']}
    by_id.update({fr['id']: fr for fr in incoming['requirements']})
    merged = validate({'version': 1, 'requirements': list(by_id.values())}, work, repo)
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', dir=work, delete=False) as tmp:
            name = tmp.name
            yaml.safe_dump(merged, tmp, sort_keys=False)
        os.replace(name, target)
    finally:
        if name and Path(name).exists(): Path(name).unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('work_item_dir', type=Path)
    parser.add_argument('--action', default='validate', choices=['validate', 'capture'])
    parser.add_argument('--bulk-file', type=Path)
    parser.add_argument('--repo-root', type=Path)
    args = parser.parse_args()
    try:
        if not args.work_item_dir.is_dir(): raise ValueError('work item directory does not exist')
        if args.action == 'capture':
            if args.bulk_file is None: raise ValueError('capture requires --bulk-file')
            payload = args.bulk_file if args.bulk_file.is_absolute() else args.work_item_dir / args.bulk_file
            capture(args.work_item_dir, payload, args.repo_root)
        else:
            validate(load(args.work_item_dir / 'requirements.yml'), args.work_item_dir, args.repo_root)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        parser.exit(1, f'ERROR: {exc}\n')
    print('Structure and explicit evidence paths valid. Execution and semantic coverage are not verified.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
