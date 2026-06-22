# Guarded Supabase remote smoke path

This smoke path is for proving that the applied Supabase schema/RLS can accept and load a private draft BracketDocument through `SupabaseBracketStore`.

It is intentionally terminal-only.

It is intentionally not wired into the public site runtime.

## Required explicit invocation

```bash id="708vw7"
WC2026_SUPABASE_REMOTE_SMOKE=1 \
WC2026_SUPABASE_SMOKE_USER_ID=<auth.users uuid> \
node tools/run_wc2026_supabase_remote_smoke_path.js
```

## Expected result

```text id="4l9kp0"
OK: guarded Supabase remote smoke path can save/load one private draft BracketDocument when explicitly enabled.
```

## Boundary

This does not activate remote mode.

This does not alter the public GitHub Pages runtime.

This does not make the sign-in UI save brackets remotely.
