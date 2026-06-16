# Card 118: Define Tooltip Side Placement and Tracking

## Claim

Bracket tooltips should be placed beside the underlying pick instead of covering it.

## Problem

When a tooltip appears over a pick, it hides the bracket item the user is trying to inspect or select.

If the tooltip contains a clickable action, dismissing it as soon as the pointer leaves the pick prevents the user from reaching the action.

## Decision

Show tooltips to the side of the pick where possible.

If the tooltip is interactive, treat both the pick and tooltip as part of the same active interaction region.

## Acceptance Criteria

- Tooltip does not obscure the pick it explains.
- Tooltip remains visually associated with the pick.
- Tooltip can be entered by pointer/touch movement when it has clickable content.
- Tooltip dismisses only after the user leaves both the pick and tooltip interaction region.
- Small-screen fallback is explicit if side placement is impossible.

## Files

- `capture_back/CAPTURE_BACK_TOOLTIP_SIDE_PLACEMENT_AND_TRACKING.md`
- `docs/features/tooltip_side_placement_and_tracking.md`
- `li/world_cup/tooltip_side_placement_and_tracking_rule.md`
- `prompts/implement_tooltip_side_placement_and_tracking.md`
