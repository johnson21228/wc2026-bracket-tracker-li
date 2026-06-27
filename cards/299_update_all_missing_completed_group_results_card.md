# Card 299: Update all missing completed group results

## Intent

Bring the site data current by patching every completed group-stage match result that is missing locally.

## Boundary

This is a data/results update only.

Do not modify:

- R32 pick behavior
- R32 group-panel tap behavior
- preselection behavior
- player standings logic
- Supabase storage logic
- board geometry

## Done when

- Missing completed group results are patched.
- Affected standings are recomputed.
- Evidence is captured under `source/text/`.
- Verification passes.
- Pack succeeds.
