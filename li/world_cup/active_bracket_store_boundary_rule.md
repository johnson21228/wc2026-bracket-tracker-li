# Active bracket store boundary before Supabase

The Bracketeering Pages site must keep browser-local play and future signed-in Supabase play as separate active modes.

Current implemented mode:
- `local`
- active store is browser/local storage behind the repository/session seam
- Supabase is ignored for bracket persistence

Future reserved mode:
- `remote`
- active store will be `SupabaseBracketStore`
- signed-in bracket state will be loaded and saved through `user_brackets.picks_json`

Core invariant:
Only the active store is authoritative. Local and remote pick contents do not need to match, merge, migrate, reconcile, or overwrite each other.

Shared contract:
Both modes use the same `BracketDocument` shape and game rules. The shared contract is document shape and write rules, not shared pick contents.

R32 lock invariant:
R32 picks may be created or changed only before R32 lock-in. After `phaseLocks.r32LockedAt` exists on the active `BracketDocument`, active write-path logic must refuse R32 mutations while leaving later non-R32 picks governed by their own game phase rules.

Future persistence target:
- one `user_brackets` row per player/game
- full document in `picks_json`

Supabase boundary:
This rule prepares the seam only. It does not apply Supabase SQL, does not change public dashboard state, and does not implement `SupabaseBracketStore`.
