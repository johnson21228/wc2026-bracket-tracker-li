# Third-place menu internal scroll

The review surface must support long third-place candidate menus without requiring server-backed state or browser dev tools.

This patch adds CSS and runtime event guards so long menus can scroll internally while preserving the prior behavior where board scrolling outside the menu dismisses floating UI.

## Review smoke test

1. Open the GitHub Pages site.
2. Tap/click a third-place R32 slot that has a long candidate menu.
3. Put the mouse or finger over the menu.
4. Scroll through the menu.
5. Select a candidate.
6. Confirm the pick appears and remains after reload.
