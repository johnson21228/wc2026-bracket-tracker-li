# Card 138 — Repair long third-place menu scrolling

## Intent

Make long third-place candidate menus reviewable on desktop and touch devices.

## Problem

Some R32 third-place slots can expose a long candidate list. When the pointer is over that menu, wheel/touch scrolling can be captured by the board-level scroll-close behavior instead of scrolling the menu itself.

## Acceptance

- Long choice menus are internally scrollable.
- Mouse wheel over the menu scrolls the menu, not the board.
- Touch move over the menu scrolls the menu on iPad/iPhone.
- Board-scroll dismissal still works when scrolling outside the open menu.
- Existing pick acceptance and storage behavior remains intact.
