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

## Persistence wiring

The `Save Picks` action now saves the current local-first BracketDocument snapshot through the existing SupabaseBracketStore seam. This is a single explicit account save. It does not enable automatic remote writes, dual-write, local-to-remote migration, or remote load/overwrite behavior.


## Signed-in account persistence

Once a player is signed in, account persistence is the normal visible persistence surface. The site checks for saved account picks on page load/session resume and on login.

If saved account picks exist and the device has no local picks, the account picks may load automatically. If both account picks and device-local picks exist, the UI exposes an explicit `Load Saved` action rather than silently overwriting local play.

Signed-out play remains local-only.
