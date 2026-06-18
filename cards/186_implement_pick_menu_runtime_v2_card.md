# Card 186 — Implement Pick Menu Runtime v2

## Intent

Implement the Pick Menu LI as runtime behavior: grouped candidate sections, clickable group labels, clear-pick near the top, prominent close, and board-attached placement that remains fully exposed over the scrollable game board.

## Scope

- Add a model-owned pick menu descriptor.
- Render menu groups and group-panel links in the view.
- Route close, clear, team pick, and group-panel actions through the controller.
- Keep ESPN/source updates outside browser runtime.

## Acceptance

- `model.getPickMenu(slotId)` returns title, source label, current pick, clear availability, grouped choices, and anchor geometry.
- Team choices remain separate from group-panel labels.
- Existing picks expose a clear action near the top of the menu.
- The menu has a prominent close button.
- The menu is absolutely positioned inside the board plane and scrolls with the game board.
- The group-panel open path uses local checked-in model data.
