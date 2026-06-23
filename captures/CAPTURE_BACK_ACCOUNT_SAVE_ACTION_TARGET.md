# Capture Back — Account Save Action Target

## Decision

Persistent storage should be first-class as an explicit account action, not as a constant storage-mode banner.

## Product behavior

Normal gameplay is local-first. The player makes picks immediately in browser-local state. Account persistence is introduced through a `Save Picks` action near the login/account chrome.

## Invariants

- No persistent `Playing locally` pill.
- No automatic Supabase write on every pick.
- No dual-write.
- No local-to-remote migration yet.
- No remote load/overwrite behavior yet.
- Hidden dev Supabase bracket store mode remains available for technical testing.
- View and Controller do not call Supabase bracket persistence directly.

## Next step

Wire the enabled `Save Picks` action to a single explicit Supabase upsert through the existing BracketStore/BracketDocument seam.
