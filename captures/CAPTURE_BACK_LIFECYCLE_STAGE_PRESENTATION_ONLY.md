# Capture Back: Lifecycle Stage Presentation-Only Gameplay

## Intent

Keep the lifecycle stage selector, but make it presentation-only for gameplay.

The selected stage may still change the pub background image and player-facing rules/help/status copy. It must not disable pick cells, change bracket rendering rules, change pick highlighting rules, or block pick pre-selection.

## New invariant

Pick availability is determined only by precedent availability.

A pick cell is selectable when the upstream team or candidate inputs required for that pick exist. R32 picks are available when their candidate menu/source exists. Later knockout picks are available when their predecessor winners exist. Empty downstream picks may remain unavailable only because their precedent is missing, not because the selected lifecycle stage is Group Stage or Knockout Stage.

## Keep

- Group Stage background remains tied to the Group Stage selection.
- Knockout Stage background remains tied to the Knockout Stage selection.
- Rules/help/status copy may remain stage-specific.
- Legacy game-1/game-2 runtime hooks may remain during migration.

## Remove / relax

- Active-game pick gating.
- Wrong-game disabled styling.
- Selected-stage-only pick enforcement.
- Controller pre-selection rejection based solely on active game/stage.

## Verification target

- Switching Group Stage / Knockout Stage changes the background only.
- Existing picks render the same in both stages.
- Pick cells enabled by precedent are selectable in both stages.
- Pick cells without precedent remain unavailable in both stages.
- No wrong-game disabled state appears solely because of stage.


Lifecycle presentation-only gameplay invariant:

- lifecycle stage is presentation-only
- selected stage must not change bracket rendering rules
- selected stage must not change pick highlighting rules
- selected stage must not block pick pre-selection
- pick availability is determined only by precedent availability
- Group Stage background may still use pub_background_game1
- Knockout Stage background may still use knockout_pub_background

