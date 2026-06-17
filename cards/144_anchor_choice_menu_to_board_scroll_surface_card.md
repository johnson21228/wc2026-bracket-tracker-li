# Card 144: Anchor Choice Menu to Board Scroll Surface

## Claim

Choice menus belong to the bracket slot that opened them, not to the viewport.

## Why

On phone and iPad, a tap can be followed by small touchmove, scroll, or visual-viewport events. If scroll dismisses menus, the menu may open and close immediately. The game board model is clearer: the menu should move with the board and close only on selection, outside tap, or another explicit menu action.

## Acceptance Criteria

- Board scrolling does not close the choice menu.
- Choice menus are attached to the board/playfield layer.
- When the board scrolls or pans, the open menu moves with the board.
- Long menus still scroll internally when the pointer/touch is over the menu.
- Outside tap and selection remain valid dismissal actions.

## Files

- `site/index.html`
- `docs/features/board_attached_choice_menu.md`
- `li/world_cup/board_attached_choice_menu_rule.md`
- `tools/verify_wc2026_board_attached_choice_menu_patch.py`
