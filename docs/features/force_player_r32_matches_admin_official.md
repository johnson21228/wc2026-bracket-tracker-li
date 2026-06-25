# Force player R32 display to match Admin_/official

## Living invariant

`playerVisibleR32 = Admin_/official R32 truth`.

R32 picks/occupants are not player picks. They are owned by `Admin_/official` in Supabase. Player brackets may display a hydrated R32 field, but that display is a projection of Admin_/official truth, not player-authored state.

## Runtime rule

For the public player site:

- read the Supabase `Admin_/official` official bracket document on app startup
- extract only its R32 occupant slots
- strip/ignore all R32 occupant values from player/local/legacy state
- render R32 occupant cells from `Admin_/official` only
- reject player writes to R32 occupant cells
- do not generate R32 choices from group data when official truth is wired
- fail closed when `Admin_/official` is missing or unreadable

Partial Admin truth is valid. If `Admin_/official` has one R32 occupant, the player board shows exactly one R32 occupant and leaves the rest unset. Static JSON and localStorage must not complete the field in public runtime.

## Anti-slop vocabulary

Say:

- Admin_/official R32 truth
- R32 occupant truth
- hydrated R32 display
- mirrored official R32 field
- player-owned later-round picks

Do not say:

- player R32 picks
- R32 fallback picks
- inferred R32 picks
- static R32 truth

## Implementation note

The main board model treats R32 display slots specially: `selectedTeam(slotId)` returns the Admin_/official team for R32 slots and returns player-owned picks only for non-R32 slots. Player/local R32 values are stripped before render/save, and R32 `setPick` calls are rejected.
