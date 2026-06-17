# Board-Attached Choice Menu

The choice menu now follows the game board model.

Instead of treating the menu as a floating viewport tooltip that closes on scroll, the menu is treated as part of the board surface. When the board scrolls, the menu moves with the board. This is especially important on phone and iPad, where tap gestures can generate small scroll or touchmove events immediately after opening a menu.

## Behavior

- Tapping a bracket slot opens a choice menu.
- The menu is attached to the board/playfield surface.
- Scrolling the board does not close the menu.
- Long menus can still scroll internally.
- Selection, outside tap, or opening another menu can close or replace the menu.

## Rationale

The bracket is a game board. A menu belongs to the board position that opened it. Scroll dismissal is useful for ephemeral tooltips, but too aggressive for a pick menu on mobile browsers.
