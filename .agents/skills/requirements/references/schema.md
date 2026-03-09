# Requirements Schema

`requirements.yml` is authoritative and uses:

- `version`: required integer (`1`)
- `feature`: required non-empty string
- `generated_from`: required non-empty string
- `requirements`: required non-empty list of FR records

FR record:

- `id`: required, unique, `^FR-\d{3}$`
- `title`: required non-empty string
- `status`: one of `proposed|verified_fdd|verified_plan|verified`
- `acceptance_criteria`: required non-empty list of AC records

AC record:

- `id`: required, unique, `^AC-\d{3}$`
- `title`: required non-empty string
- `status`: one of `proposed|verified_fdd|verified_plan|verified`
- `verification_method`: optional, one of `automated|manual|hybrid`, default `automated`
- `proofs`: required list
