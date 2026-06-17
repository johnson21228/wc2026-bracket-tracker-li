# Verify Board-Attached Choice Menu

Run:

```bash
python3 tools/verify_wc2026_board_attached_choice_menu_patch.py
python3 tools/verify_wc2026_third_place_menu_scroll_patch.py
python3 tools/verify_wc2026_opaque_menu_pub_background_patch.py
python3 tools/verify_wc2026_pages_review_pick_acceptance_patch.py
python3 tools/verify_wc2026_bracket_tracker.py
make verify
```

Manual review:

1. Open the local site.
2. Tap a bracket slot on phone or iPad.
3. Confirm the menu remains open.
4. Scroll the board outside the menu.
5. Confirm the menu moves with the board instead of closing.
6. Scroll inside a long menu.
7. Confirm the menu scrolls internally.
8. Select a team and confirm the pick renders and persists after reload.
