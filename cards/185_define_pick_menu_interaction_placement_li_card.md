# Card 185: Define pick menu interaction and placement LI

## Intent

Capture the pick menu interaction rules before runtime implementation.

The pick menu is not only a candidate list. It is a bracket-attached interaction surface that must expose current pick state, clearing, group evidence, closing, and placement relative to the source bracket slot.

## Desired behavior

- If a slot already has a pick, the menu shows a clear-pick action near the top of the menu.
- The clear-pick action is distinct from team choices and does not get buried below long team lists.
- The menu includes a prominent close button near the top edge.
- The close button closes the menu without mutating pick state.
- The menu opens next to the bracket slot that invoked it.
- The menu remains attached to the scrollable game board plane and scrolls with the board.
- The menu is shifted up/down/left/right as needed so it remains fully exposed within the visible scrollable board area whenever possible.
- Group labels in the menu remain clickable evidence/source affordances that open the group panel without selecting or clearing a pick.

## MVC boundary

- Model owns pick state, clear-pick availability, source titles, grouped candidate choices, group panel source references, and downstream invalidation.
- View owns menu rendering, close button rendering, clear-pick rendering, slot-adjacent placement, clipping avoidance, and scroll-with-board behavior.
- Controller owns open, close, clear, select, and group-panel-open actions.

## Acceptance

- `li/world_cup/pick_menu_interaction_placement_rule.md` defines the durable rule.
- `docs/features/pick_menu_interaction_placement.md` explains the intended UX and MVC split.
- `capture_back/CAPTURE_BACK_PICK_MENU_INTERACTION_PLACEMENT_LI.md` captures the change.
- `tools/verify_wc2026_pick_menu_interaction_placement_li.py` verifies the LI exists and includes the required concepts.
- `make verify` runs the verifier.

## Non-goals

This card does not implement runtime menu placement, clear-pick buttons, close buttons, or group-panel launching. It defines the LI that governs that implementation.
