# Verify Prevent Duplicate R32 Menu Assignments

Check that R32 and third-place menus do not offer teams already assigned to other R32 slots.

Run:

```bash
python3 tools/verify_wc2026_prevent_duplicate_r32_menu_assignments_patch.py
python3 tools/verify_wc2026_board_attached_choice_menu_patch.py
python3 tools/verify_wc2026_anchor_menu_to_picked_item_patch.py
python3 tools/verify_wc2026_bracket_tracker.py
make verify
```

Manual test:

1. Pick a team into an R32 slot.
2. Open another R32/third-place menu.
3. Confirm the already-picked team is not offered.
4. Reopen the original slot.
5. Confirm its current team remains available.
6. Confirm selection still saves and survives reload.
