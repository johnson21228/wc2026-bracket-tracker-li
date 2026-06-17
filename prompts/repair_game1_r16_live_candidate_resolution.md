# Repair Game 1 R16 Live Candidate Resolution

Patch Game 1 so R16 slots derive candidate choices from live upstream R32 picks.

Verify that `L-R16-01` maps to `L-R32-01` and `L-R32-02`, including manifest aliases `R32-L-M1A` and `R32-L-M1B`.

Run:

    python3 tools/verify_wc2026_game1_r16_live_candidate_resolution_patch.py
    make verify
    make pack
