# Card 233: Make zoom-50 floating surfaces fully visible

## Intent
Pick menus and group panels must remain fully visible and usable when the Pages-owned board zoom is set to 50%.

## Rule
At 50% zoom, every floating interaction surface must be placed from rendered screen coordinates with `getBoundingClientRect()`, clamped to a safe visible rectangle, and kept above bottom controls.

## Scope
- R32 pick menus.
- Clean MVC pick menus.
- Group panel popovers opened from the group rail or from pick-menu group links.

## Acceptance
- Pick menus are fully visible at 50% zoom.
- Group panels are fully visible at 50% zoom.
- Menus and panels use shared placement logic.
- Bottom controls remain visible, but menus and panels render in front of them.
- Bottom controls are excluded from the safe placement rectangle.
- `make verify` runs the zoom-50 floating surface verifier.
