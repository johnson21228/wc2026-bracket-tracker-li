# Capture Back: Hydrate only Supabase Admin R32 into player picks

## Why

The player board still expects preceding bracket slots to contain selected teams before later-round cells become pre-selectable. After making R32 pure Admin truth, R16++ cells could remain empty/unpickable when the R32 feeder path did not materialize into the player picks map.

## Decision

Copy ONLY R32 entrant slots from Supabase Admin_/official into each player BracketDocument. Do not copy any Admin_/official later-round official truth.

## Behavior

- Supabase Admin_/official remains the only R32 authority.
- Player documents may store mirrored R32 entries for rendering/preselection compatibility.
- Mirrored R32 entries are marked `playerAuthored: false`.
- Normal players cannot edit R32.
- Player R16++ picks remain player-authored.
- Missing Supabase Admin R32 fails closed, leaving R32 unset and R16++ preselection unavailable.

## Verification

`tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py` verifies:

- Copy ONLY R32 from Supabase Admin_/official.
- Do not copy Admin R16++ truth into player brackets.
- Do not copy R32 from static JSON.
- Existing player R16++ picks survive hydration.
- Stale player/local R32 is overwritten by Supabase Admin R32.
- Missing Supabase Admin R32 remains unset/fail-closed.
