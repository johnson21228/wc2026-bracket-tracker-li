# iPhone Touch Map Mode Rule

The WC2026 board must behave like a map on iPhone Safari.

The browser viewport owns fixed chrome such as zoom controls, info controls, identity panels, and floating panels. The board plane owns pan and zoom state. Touch gestures inside the board viewport must move or zoom the board plane rather than causing browser-page zoom/scroll that pushes controls off screen.

Rules:
- One-finger touch drag on non-interactive board background pans the board viewport.
- Two-finger pinch on non-interactive board background zooms the board around the pinch midpoint.
- Pick slots, group buttons, zoom buttons, info buttons, sign-in/profile surfaces, menus, and panels remain tappable and are excluded from board gesture capture.
- Browser touch behavior is suppressed only within the board viewport.
- Fixed controls remain fixed-size, viewport/safe-area-aware browser chrome.
- Existing desktop mouse drag, double-click zoom, and wheel zoom behavior must remain unchanged.
