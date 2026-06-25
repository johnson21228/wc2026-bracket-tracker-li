# Capture Back: force player R32 display to match Admin_/official

## Goal

Make the public player site always display R32 occupant slots from the Supabase `Admin_/official` official bracket document.

## Invariant

`playerVisibleR32 = Admin_/official R32 truth`.

R32 picks/occupants are not player picks. Player brackets may display hydrated R32 values only as mirrored official truth.

## Changes

- Wired the main app to pass a Supabase official bracket store into the board model.
- Made R32 display slots resolve through Admin_/official truth instead of player/local picks.
- Stripped stale player/local R32 values before render/save.
- Rejected player edits to R32 occupant slots.
- Disabled public/runtime R32 choice generation from group data when official truth is wired.
- Added fail-closed Admin_/official R32 documents for missing/unreadable official truth.
- Updated hydration so partial Admin truth overwrites stale player R32 values and leaves missing Admin slots unset.

## Verification

`tools/verify_wc2026_force_player_r32_matches_admin_official.py` proves:

- the main player board uses Supabase Admin_/official as the official R32 source
- R32 display is projected from Admin_/official
- stale player/local R32 values are stripped
- player R32 edits are rejected
- public runtime does not generate fallback group choices for R32
- missing/unreadable Admin truth fails closed

## Expected test behavior

If `Admin_/official` has only Germany in R32, the player site must show exactly Germany in that official R32 slot and no additional fake R32 occupants.
