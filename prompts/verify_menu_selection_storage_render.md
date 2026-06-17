# Verify Menu Selection Storage and Render

Check that choosing a team from a knockout choice menu writes and renders the bracket cell.

Run:

    python3 tools/verify_wc2026_menu_selection_storage_render_patch.py
    make verify
    make pack

Manual check:

1. Tap `L-R16-01`.
2. Choose one team.
3. Confirm the chosen team appears in `L-R16-01`.
4. Refresh the page.
5. Confirm the pick is still present.
