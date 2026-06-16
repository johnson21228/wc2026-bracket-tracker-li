# Verify Site Pick Store Candidate Fallback

Run:

    python3 tools/verify_wc2026_site_pick_store_candidate_fallback_patch.py
    make verify
    make pack

Manual check:

1. Create two R32 picks feeding `L-R16-01`.
2. Tap `L-R16-01`.
3. Confirm the R16 menu shows exactly two teams.
