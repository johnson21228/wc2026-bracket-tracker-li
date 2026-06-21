# Capture Back: Zoom 50 Floating Surface Board-Rect Clamp

## Intent

Repair pick menu and group panel placement at 50% zoom when the board occupies only part of the visible viewport.

## Problem

At 50% zoom, floating surfaces could be clamped against the scroll viewport/window but still spill to the right of the rendered board plane. Because the board plane clips its children, the pick menu or group panel could appear partly off-board and be visually clipped.

## Change

The shared floating surface placement helper now intersects the safe client rectangle with:

- the board scroll viewport
- the browser window
- the rendered board plane rectangle

This makes the placement helper choose left/above/below alternatives when the right side does not fit inside the visible rendered board.

## Surfaces covered

The fix applies through the shared helper used by:

- R32 pick menus
- MVC pick menus
- group panels

## Verification

`tools/verify_wc2026_zoom50_floating_surface_placement.py` now requires the board-rect safe area clamp and marker.
