# Card 269 — Supabase remote bracket store contract before implementation

Define the future Supabase-backed bracket store contract before implementing it.

## Goal

Keep Supabase persistence behind the existing store/repository/session seam.

## Acceptance

- Future remote store contract is documented.
- Future remote store uses:
  - `loadUserBracket(userId)`
  - `saveUserBracket(bracketDocument)`
- Remote persistence target is one `user_brackets` row per player/game.
- Full canonical `BracketDocument` is stored in `picks_json`.
- Local and remote modes remain separate.
- Only the active store is authoritative.
- No automatic local/remote merge is introduced.
- View and Controller do not call Supabase directly for bracket persistence.
- R32 lock invariant is preserved for future remote persistence.
- No runtime behavior is changed in this CB.
- No Supabase SQL is applied.
