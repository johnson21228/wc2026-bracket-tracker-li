# Capture Back: Guarded Supabase remote smoke path without changing public runtime

## Intent

Add a developer-only smoke path that can prove Supabase save/load works after dashboard SQL application.

## Applied change

Added:

- `tools/run_wc2026_supabase_remote_smoke_path.js`
- `tools/verify_wc2026_guarded_supabase_remote_smoke_path.py`

Updated:

- `site/js/services/RemoteStoreActivationGuard.js`
- `Makefile`
- `MAP.md`

## Runtime boundary

This does not activate remote mode.

This does not change public Pages runtime behavior.

This does not wire Supabase into the site.

The live smoke harness requires explicit terminal opt-in:

```text
WC2026_SUPABASE_REMOTE_SMOKE=1
WC2026_SUPABASE_SMOKE_USER_ID=<auth.users uuid>
```

## Verification

The verifier confirms:

- the smoke harness is explicit developer-only
- the remote guard remains fail-closed for public runtime
- the live remote smoke harness is not included in `make verify`
- public site files do not reference the smoke harness
