# Stage Gates

`master_validate` enforces minimum AC status by stage:

- `fdd_only`: every AC must be at least `verified_fdd`
- `plan_present`: every AC must be at least `verified_plan`
- `implementation_complete`: every AC must be `verified`
