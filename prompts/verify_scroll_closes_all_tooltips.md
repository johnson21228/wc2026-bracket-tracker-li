# Verify Scroll Closes All Tooltips

Open Game 1 and verify:

1. Hover/tap a pick until a tooltip appears.
2. Scroll the page or board.
3. Confirm the tooltip closes.
4. Open a knockout choice menu.
5. Confirm scroll dismissal does not erase the selected bracket cell or stored picks.

Run:

    python3 tools/verify_wc2026_scroll_closes_all_tooltips_patch.py
    make verify
    make pack
