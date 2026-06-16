# Verify Site Bracket Pick Store

Check that Game 1 has a site-owned bracket pick store.

Run:

    python3 tools/verify_wc2026_site_bracket_pick_store_patch.py
    make verify
    make pack

Confirm that `site/game1/index.html` loads:

    ../data/game1_bracket_pick_store.js

Confirm that the store defines:

    wc2026.game1.bracketPicks
    WC2026_GAME1_BRACKET_PICK_STORE
    WC2026_GAME1_BRACKET_PICK_STORE_API
