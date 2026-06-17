# Verify Apply Selection to Picked Cell

Run:

    python3 tools/verify_wc2026_apply_selection_to_picked_cell_patch.py
    make verify
    make pack

Manual test:

1. Clear picks if needed.
2. Fill the two upstream R32 cells for `L-R16-01`.
3. Tap `L-R16-01`.
4. Choose one team from the menu.
5. Confirm the selected team appears in `L-R16-01`.
6. Refresh the page.
7. Confirm the selected team remains in `L-R16-01`.
