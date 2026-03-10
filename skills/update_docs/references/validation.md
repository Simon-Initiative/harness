# Validation

Run work-item validation for each affected work item:

```bash
python3 <skills_root>/validate/scripts/validate_work_item.py <work_item_dir> --check all
```

Resolve `<skills_root>` as the directory that contains the installed harness skills. Do not resolve the validator path relative to the repository or current working directory.
