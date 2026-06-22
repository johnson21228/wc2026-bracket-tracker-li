# Card 268 — Public Pages release-line guard for Supabase prep

Add LI and verification that protect the public GitHub Pages site while Supabase/Auth/storage work continues on a feature branch.

## Acceptance

- `main` is documented as the public Pages release line.
- Supabase prep branches are documented as integration/prep lanes, not public release lanes.
- Unfinished Supabase/Auth/storage work must not publish accidentally.
- Merge/publish readiness requires:
  - `python3 tools/clean_repo_hygiene.py`
  - `make verify`
  - `make pack`
  - browser smoke test
  - local/browser play without Supabase
  - intentional identity surface posture
  - explicit Supabase SQL/dashboard posture
  - accepted public Pages publish risk
- Publish tooling from Supabase prep branches is guarded.
- Supabase SQL/dashboard changes remain separate explicit actions.
- No runtime behavior changes.
