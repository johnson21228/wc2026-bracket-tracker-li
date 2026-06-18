# Capture Back: Pick Menu Interaction and Placement LI

## Summary

Added LI for pick menu behavior that must be preserved before runtime work begins.

## Captured decisions

- Pick menus must show a clear-pick action near the top when a slot already has a pick.
- Pick menus must show a prominent close button.
- Pick menus must open next to the slot that invoked them.
- Pick menus must remain attached to the scrollable board plane and scroll with the board.
- Pick menus must shift placement to avoid clipping off the visible board area whenever possible.
- Group labels in grouped candidate menus are clickable evidence links that open the group panel without mutating picks.
- Model owns pick state, grouped choices, source labels, clear availability, and cascade clearing.
- View owns rendering, close/clear affordance rendering, placement, clipping avoidance, and scroll-with-board behavior.
- Controller owns user actions only.

## Files

- `cards/185_define_pick_menu_interaction_placement_li_card.md`
- `li/world_cup/pick_menu_interaction_placement_rule.md`
- `docs/features/pick_menu_interaction_placement.md`
- `tools/verify_wc2026_pick_menu_interaction_placement_li.py`

## Verification

`make verify` runs `tools/verify_wc2026_pick_menu_interaction_placement_li.py`.
