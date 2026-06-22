# Lifecycle Stage Presentation-Only Gameplay

The Bracketeering Pub lifecycle stage selector is a presentation control, not a gameplay gate.

## Stage-owned presentation

The selected stage may still control:

- Group Stage background
- Knockout Stage background
- rules/help/status copy
- stage label/context

## Precedent-owned gameplay

Pick availability is determined only by precedent availability.

- R32 picks are available when their candidate menu/source exists.
- Later knockout picks are available when their predecessor winners exist.
- Empty downstream picks remain unavailable only when their precedent is missing.

## Prohibited behavior

The selected stage must not:

- disable pick cells
- change bracket rendering rules
- change pick highlighting rules
- block pick pre-selection
- create a wrong-game disabled state

## Migration note

Legacy game-1/game-2 hooks may remain while runtime naming is migrated. They can help select background/context, but they cannot own gameplay availability.


Lifecycle presentation-only gameplay invariant:

- lifecycle stage is presentation-only
- selected stage must not change bracket rendering rules
- selected stage must not change pick highlighting rules
- selected stage must not block pick pre-selection
- pick availability is determined only by precedent availability
- Group Stage background may still use pub_background_game1
- Knockout Stage background may still use knockout_pub_background

