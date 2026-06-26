# Force player R32 display to match Admin_/official

## Living invariant

`playerVisibleR32 = Admin_/official R32 truth`.

R32 picks/occupants are not player picks. R32 occupants are not player-authored picks. They are owned by `Admin_/official` in Supabase. Player BracketDocuments may store hydrated R32 mirror records for rendering, scoring, and R16++ preselection compatibility, but those records must be copied only from Supabase Admin_/official and marked `playerAuthored: false`.

## Runtime rule

For the public player site:

- read the Supabase `Admin_/official` official bracket document on app startup
- extract only its R32 occupant slots
- strip stale R32 occupant values from player/local/legacy state
- copy ONLY Supabase Admin_/official R32 entrants into player `picksBySlot` as mirror records
- render R32 occupant cells from the hydrated player BracketDocument for compatibility
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

The main board model hydrates ONLY Supabase Admin_/official R32 entrants into player `picksBySlot`. Rendering and R16++ preselection can then use the existing player-document path, while normal player R32 `setPick` calls remain rejected and stale local/static R32 values remain invalid copy sources.
