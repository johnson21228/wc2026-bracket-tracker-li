# Capture Back: iPhone Touch Map Mode

## Outcome

The WC2026 Bracketeering board now has a scoped iPhone/touch map-mode path.

## Behavior

- The board viewport captures touch map gestures.
- One-finger touch drag pans the board.
- Two-finger pinch zooms the board around the pinch midpoint.
- Browser-page scroll/zoom is suppressed only within the board viewport.
- Pick slots, group buttons, zoom controls, info controls, identity panels, menus, and floating panels remain tappable.
- Fixed zoom controls remain viewport/safe-area browser chrome.
- Desktop mouse drag, double-click zoom, and wheel zoom remain unchanged.

## Files

- `site/js/mvc/view.js`
- `site/css/board.css`
- `li/world_cup/iphone_touch_map_mode_rule.md`
- `docs/features/iphone_touch_map_mode.md`
- `tools/verify_wc2026_iphone_touch_map_mode.py`
