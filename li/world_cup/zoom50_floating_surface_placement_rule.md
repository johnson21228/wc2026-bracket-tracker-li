# Zoom-50 floating-surface placement rule

When the board is rendered at 50% zoom, floating UI surfaces must remain fully visible and above bottom controls.

The View must place pick menus and group panels from rendered screen coordinates using `getBoundingClientRect()`. Placement must not depend only on unscaled native board coordinates.

The shared placement rule is:

1. Render the floating surface in an overlay layer above board content.
2. Measure the anchor, board plane, viewport, and bottom controls with `getBoundingClientRect()`.
3. Compute a safe rectangle that excludes the group rail and bottom controls.
4. Prefer the normal placement when it fits.
5. Otherwise flip above/below or left/right.
6. Clamp the surface into the safe rectangle.
7. Apply internal scrolling when the surface cannot fully fit.
8. Use z-index values that keep pick menus and group panels in front of the group rail and bottom gameboard buttons.

This rule applies to R32 pick menus, clean MVC pick menus, and group panels.
