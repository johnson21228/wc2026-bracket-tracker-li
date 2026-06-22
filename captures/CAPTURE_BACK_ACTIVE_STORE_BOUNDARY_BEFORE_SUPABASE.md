# Capture Back: Active store boundary before Supabase

This capture prepares Bracketeering for Supabase persistence without applying SQL or implementing Supabase-backed bracket storage.

- One active game remains `game1`.
- One player bracket remains one canonical `BracketDocument`.
- Future Supabase persistence remains one `user_brackets` row per player/game with the full document in `picks_json`.
- Browser-local play and signed-in remote play are separate active modes.
- Only the active store is authoritative.
- Local and remote picks are not automatically merged, migrated, reconciled, or required to match.
- `BracketDocument.phaseLocks.r32LockedAt` represents R32 lock-in.
- R32 picks cannot be changed after lock-in through the active write path.
