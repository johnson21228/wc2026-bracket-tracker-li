# Card 125: Scroll Closes All Tooltips

## Claim

When the Game 1 board scrolls, all tooltip surfaces should close.

## Why

Tooltips are anchored to a visible target. Scrolling changes the visual relationship between target and tooltip, so leaving tooltips open creates stale or misleading surfaces.

## Acceptance Criteria

- Scroll closes the side tooltip.
- Wheel movement closes the side tooltip.
- Touch scrolling closes the side tooltip.
- Legacy tooltip surfaces are suppressed when identifiable.
- Menu state and pick storage are not cleared by scrolling.

## Files

- `site/game1/index.html`
- `li/world_cup/scroll_closes_all_tooltips_rule.md`
- `tools/verify_wc2026_scroll_closes_all_tooltips_patch.py`
