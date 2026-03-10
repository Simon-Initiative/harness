# Validation

Run work-item validation before and after implementation.

```bash
python3 <skills_root>/validate/scripts/validate_work_item.py <work_item_dir> --check all
```

Resolve `<skills_root>` as the directory that contains the installed harness skills. Do not resolve the validator path relative to the repository or current working directory.

If validation fails, fix docs and rerun before marking the work complete.
