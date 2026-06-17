# Verify Retarget Open Choice Menu

Run:

```bash
python3 tools/verify_wc2026_retarget_open_choice_menu_patch.py
python3 tools/verify_wc2026_anchor_menu_to_picked_item_patch.py
python3 tools/verify_wc2026_board_attached_choice_menu_patch.py
python3 tools/verify_wc2026_bracket_tracker.py
make verify
```

Manual test:
1. Open menu for one R32 slot.
2. Tap another pickable slot while the first menu is open.
3. Confirm the new slot's menu opens from that same tap.
4. Confirm duplicate filtering reruns.
5. Confirm selection saves and closes.
