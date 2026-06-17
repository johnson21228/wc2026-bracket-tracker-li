# Verify third-place menu scroll

Inspect the WC2026 bracket site and verify that long third-place candidate menus are internally scrollable.

Required checks:

- `site/index.html` contains the long-menu scroll CSS and JS markers.
- Wheel and touchmove events over menu surfaces stop propagation to board-scroll close behavior.
- Menu CSS uses bounded max-height, `overflow-y: auto`, `overscroll-behavior: contain`, and touch scrolling support.
- Existing Pages review pick acceptance remains active.
