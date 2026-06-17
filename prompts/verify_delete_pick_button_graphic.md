# Verify Delete Pick Button Graphic

Use this prompt after applying the delete pick button graphic overlay.

Check that:

1. Existing pick-removal menu controls no longer visibly show "UnPick".
2. The control renders as a trash/delete graphic.
3. The existing deletion behavior still works.
4. Accessibility metadata says "Delete pick".
5. The patch does not alter unrelated menu choice behavior.

Run:

```bash
python3 tools/verify_wc2026_delete_pick_button_graphic_patch.py
python3 tools/verify_wc2026_bracket_tracker.py
make verify
```
