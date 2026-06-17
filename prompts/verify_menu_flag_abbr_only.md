# Verify Menu Flag + Abbreviation Only Rendering

Run:

```bash
python3 tools/verify_wc2026_menu_flag_abbr_only_patch.py
python3 tools/verify_wc2026_board_attached_choice_menu_patch.py
python3 tools/verify_wc2026_third_place_menu_scroll_patch.py
python3 tools/verify_wc2026_opaque_menu_pub_background_patch.py
python3 tools/verify_wc2026_pages_review_pick_acceptance_patch.py
python3 tools/verify_wc2026_bracket_tracker.py
make verify
```

Manual review:

1. Open the site locally.
2. Tap a pickable bracket slot.
3. Confirm menu rows show only flag + three-letter code.
4. Select a team and confirm the pick stores/renders.
5. Open a long third-place menu and confirm internal menu scroll still works.
6. Confirm board scroll does not close the menu.
