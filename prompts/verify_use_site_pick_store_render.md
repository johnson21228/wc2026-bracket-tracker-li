# Verify Use Site Pick Store Render

Run:

    python3 tools/verify_wc2026_use_site_pick_store_render_patch.py
    make verify
    make pack

Manual check:

1. Open Game 1.
2. Make an R32 pick.
3. Open the adjacent R16 choice menu.
4. Pick a team.
5. Confirm the R16 cell renders.
6. Refresh and confirm the R16 cell still renders.
