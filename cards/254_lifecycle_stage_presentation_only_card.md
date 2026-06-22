# Card 254: Make lifecycle stage presentation-only for picking and rendering

## Status

Ready to apply.

## Problem

The lifecycle stage selector was renamed to Group Stage / Knockout Stage, but earlier active-game behavior can still make the selected stage act like a gameplay gate. That makes the same bracket render or pick differently depending on the selected stage.

## Decision

Lifecycle stage is presentation-only for gameplay.

Pick availability is determined only by precedent availability.

## Scope

The stage selector may still change:

- the pub background image
- rules/help/status copy
- stage label/context

The stage selector must not change:

- pick-cell enabled state
- pick highlighting
- bracket rendering rules
- controller pre-selection acceptance

## Runtime rule

A pick is available when its precedent data exists. A pick is unavailable only when its precedent is missing.

Legacy game-1/game-2 hooks may remain as migration plumbing, but they must not disable player pick surfaces.

## Verification

`tools/verify_wc2026_lifecycle_stage_presentation_only_picks.py` verifies the new invariant and rewrites the prior active-game pick verifiers to assert presentation-only stage behavior rather than old wrong-game gating.


Lifecycle presentation-only gameplay invariant:

- lifecycle stage is presentation-only
- selected stage must not change bracket rendering rules
- selected stage must not change pick highlighting rules
- selected stage must not block pick pre-selection
- pick availability is determined only by precedent availability
- Group Stage background may still use pub_background_game1
- Knockout Stage background may still use knockout_pub_background

