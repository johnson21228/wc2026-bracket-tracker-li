# Capture Back: Supabase Roomy Identity Panel

## Intent
Move Supabase sign-in out of the cramped header form and into a roomy identity panel while keeping bracket persistence local.

## Boundary
- Supabase Auth may be exercised from the local or Pages site.
- The active bracket store remains localStorage.
- SupabaseBracketStore remains inactive behind the fail-closed remote store guard.
- No public runtime writes to `user_brackets`.

## Result
The header now shows a compact sign-in/status button. Opening it displays a full-width email input, clear identity-only copy, error/status space, and a short click cooldown to avoid repeated magic-link rate-limit requests.
