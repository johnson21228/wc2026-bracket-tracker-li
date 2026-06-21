# Card 242: Zoom 50 Floating Surface Board-Rect Clamp

## Goal

Keep pick menus and group panels fully visible at 50% zoom when the rendered board is narrower than the viewport.

## Scope

- Update the shared floating surface placement helper.
- Clamp safe placement against the rendered board plane, not only the viewport/window.
- Preserve bottom-control exclusion.
- Preserve shared use by R32 pick menus, MVC pick menus, and group panels.
- Verify the board-rect safe clamp.

## Verification

Run:

- `python3 tools/verify_wc2026_zoom50_floating_surface_placement.py`
- `make verify`
