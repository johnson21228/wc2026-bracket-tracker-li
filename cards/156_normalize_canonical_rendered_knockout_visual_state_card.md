# Card 156 — Normalize Canonical Rendered Knockout Visual State

## Intent

Ensure every rendered Game 1 knockout pick comes from canonical pick state and receives the same normal visual treatment.

This follows:

- Card 154 — Implement Game 1 Canonical Pick State Model
- Card 155 — Route Game 1 Rendering Through Canonical Pick State Model

## Insight

All rendered knockout picks come from canonical state.

Therefore, rendered R16/QF/SF cards should not look different because one was produced by an older storage path, a stored bridge, a finality marker, or an adornment patch.

Canonical state decides whether a pick exists.

Rendering displays the valid canonical pick.

CSS gives all valid rendered knockout picks one consistent visual treatment.

## Problem

Some R16 cards can appear with a heavier white outline or shadow even when they are valid canonical picks.

This creates the false visual signal that some picks are more selected, older, stored, final, or special.

## Required Rule

All valid rendered knockout picks must render consistently.

Persistent heavyweight visual states are not allowed for normal rendered picks.

Heavy white outline is reserved for active interaction only:

- hover
- keyboard focus
- active tap/focus-visible state

## Required Scope

Normalize visual state for:

- `.r16PickCard`
- `.advancePickCard`
- `.storedKnockoutPickCard`
- `[data-r32-slot-fit="true"]`
- finality markers such as `[data-choice-can-remain-final]`
- classes such as `.finalEligiblePick` when applied to knockout pick cards

## Non-goals

Do not change the canonical pick-state model.

Do not rewrite menu behavior.

Do not change R32 hit testing.

Do not remove verifier coverage from Card 154 or Card 155.

## Acceptance Criteria

- Rendering still uses `WC2026_GAME1_PICK_STATE`.
- All rendered R16/QF/SF cards have the same baseline border/shadow treatment.
- No persistent heavy white outline or stored-state glow remains on normal rendered knockout cards.
- Hover/focus outline remains available for usability.
- Focused verifier passes.
