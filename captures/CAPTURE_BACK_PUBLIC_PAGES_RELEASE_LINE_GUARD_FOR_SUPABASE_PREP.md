# Capture Back: Public Pages release-line guard for Supabase prep

This capture adds a governance guard for Supabase preparation work.

- `main` is the public Pages release line.
- Supabase/Auth/storage work stays on feature branches until intentionally approved.
- Unfinished Supabase/Auth/storage work must not be published accidentally.
- `tools/force_pages_publish.py` and equivalent publish paths must not be used from Supabase prep branches unless explicitly scoped.
- Local/browser play must continue to work until remote persistence is intentionally released.
- Supabase SQL/dashboard changes are separate explicit actions.
- A browser-safe publishable key is not itself a release signal.
- Merge/publish readiness requires clean hygiene, verify, pack, browser smoke test, correct identity posture, local-mode fallback, explicit Supabase SQL/dashboard posture, and accepted public Pages publish risk.

No runtime site behavior is changed by this capture.
