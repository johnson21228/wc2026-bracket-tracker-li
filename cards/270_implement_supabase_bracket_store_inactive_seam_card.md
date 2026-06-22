# Card 270 — Implement SupabaseBracketStore behind inactive remote store seam

Add the Supabase-backed bracket store module without activating it in public runtime.

## Acceptance

- `site/js/services/SupabaseBracketStore.js` exists.
- It exports `SupabaseBracketStore`.
- It exports `createSupabaseBracketStore`.
- It implements `loadUserBracket(userId)`.
- It implements `saveUserBracket(bracketDocument)`.
- It targets `user_brackets`.
- It reads/writes `picks_json`.
- It uses one row per `user_id,game_id`.
- It upserts with `onConflict: "user_id,game_id"`.
- It preserves full canonical `BracketDocument` payloads.
- It throws explicit load/save errors.
- It is not imported by public runtime entrypoints yet.
- `BracketRepository` remains local-store active by default.
- View and Controller do not call Supabase directly.
- No Supabase SQL is applied.
- No public dashboard state is changed.
