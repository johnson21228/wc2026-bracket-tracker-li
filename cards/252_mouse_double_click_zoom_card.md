# Card 252: Mouse double-click board zoom

## Goal

Make the gameboard feel more like a gesture-owned play surface by adding mouse double-click zoom around the pointer.

## Scope

View/navigation only.

## Requirements

- Double-click empty board space zooms in around the pointer.
- Reuse the existing board zoom/clamp math.
- Ignore touch double-tap and non-mouse pointer sources.
- Ignore double-clicks on pick buttons, group buttons, menus, panels, banner controls, rules controls, zoom controls, links, and inputs.
- Preserve mouse drag-pan.
- Preserve MacBook two-finger scrolling.
- Preserve Cmd/Ctrl-wheel zoom.
- Preserve tap/click-to-pick behavior.
- Do not change picks, scoring, storage, Supabase, BracketDocument, Game 1/Game 2 data, or result data.

## Verification

- `python3 tools/verify_wc2026_mouse_double_click_zoom.py`
- `python3 tools/verify_wc2026_mouse_drag_board_pan.py`
- `python3 tools/verify_wc2026_pages_owned_board_wheel_pinch_zoom.py`
- `make verify`
- `make pack`
