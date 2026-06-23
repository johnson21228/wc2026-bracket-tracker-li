# Capture Back — Storage Mode Status Surface

## Decision

Add a visible storage mode status surface before enabling account-backed bracket saving as a normal gameplay path.

## Player-facing truth

- Normal public gameplay says `Playing locally`.
- Signed-in normal gameplay still says `Playing locally`.
- Hidden dev remote-store mode says `Remote save test mode` only when the Supabase bracket store is actually active.
- If the dev flag is present but no signed-in session exists, the app remains local and says `Playing locally`.

## Safety invariants

- Remote save is not enabled by default.
- The hidden dev flag remains the only remote gameplay storage activation path.
- No local-to-remote migration.
- No dual-write.
- View and Controller do not know about Supabase bracket persistence.
