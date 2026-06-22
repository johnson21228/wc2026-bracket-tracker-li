# Capture Back: Mouse double-click board zoom

## Intent

Add the next low-risk gesture-owned gameboard behavior: mouse double-click on empty board space zooms the board around the pointer.

## Boundary

This is View-owned navigation only. It changes board viewport scale and scroll position through the existing board zoom path. It does not change picks, scoring, storage, Supabase, BracketDocument, Game 1/Game 2 data, or result data.

## Touch and pick safety

Do not disturb iPad/iPhone browser touch navigation. Do not add custom `touchstart`, `touchmove`, or touch pinch handlers in this Capture Back.

Double-click zoom must ignore pick buttons, group buttons, menus, panels, banner controls, rules controls, zoom controls, links, inputs, and other interactive surfaces. Tap/click pick behavior remains owned by the existing pick controllers.

## Implementation

- Add `BOARD_DOUBLE_CLICK_ZOOM_STEP` beside the existing board zoom constants.
- Add an idempotent `installMouseBoardDoubleClickZoom()` View helper.
- Track the most recent pointer type so touch double-tap is not treated as board zoom.
- Add a `dblclick` listener on `[data-board-scroll]` for mouse-only empty-board zoom.
- Reuse `zoomBoardAroundPoint(...)` so zoom remains centered at the pointer and uses the existing clamp/select synchronization behavior.
- Wire a verifier into `make verify`.

## Verification

`tools/verify_wc2026_mouse_double_click_zoom.py` proves the mouse-only double-click zoom path exists, is wired, reuses pointer-centered zoom, excludes interactive controls, and does not add custom touch handlers.
