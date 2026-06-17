# Verify Short-Term R16 Hardcoded Hold

Run:

    python3 tools/verify_wc2026_short_term_r16_hold_patch.py
    make verify
    make pack

Manual browser check:

    window.WC2026_SHORT_TERM_R16_HOLD.findSource()
    window.WC2026_SHORT_TERM_R16_HOLD.apply()
