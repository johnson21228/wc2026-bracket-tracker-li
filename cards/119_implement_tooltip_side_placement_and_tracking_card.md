# Card 119: Implement Tooltip Side Placement and Tracking

## Claim

Game 1 tooltips should appear beside the pick and remain reachable when the tooltip contains clickable content.

## Governing Rule

- `li/world_cup/tooltip_side_placement_and_tracking_rule.md`

## Implementation

Patch `site/game1/index.html` with a side-placement tooltip layer.

## Acceptance Criteria

- Tooltip does not cover the pick when side placement is available.
- Tooltip is positioned within viewport bounds.
- Tooltip remains open while pointer moves between pick and tooltip.
- Tooltip can expose a clickable action with `data-tooltip-action-href`.
- Escape key and outside tap/click dismiss the tooltip.
- Verifier confirms required implementation markers.

## Files

- `site/game1/index.html`
- `tools/verify_wc2026_tooltip_side_placement_patch.py`
- `capture_back/CAPTURE_BACK_IMPLEMENT_TOOLTIP_SIDE_PLACEMENT_AND_TRACKING.md`
