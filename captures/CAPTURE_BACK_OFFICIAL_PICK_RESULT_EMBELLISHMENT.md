# Capture Back — Official Pick Result Embellishment

## Intent

Restore the player-facing result feedback that makes a missed knockout pick immediately legible, and carry the same visual language into the center Final Four semifinal winner rows.

## Change

Ordinary knockout slots with a resolved wrong pick now again show:

- a red result outline;
- the picked team struck through;
- a stable `Correct: <flag> <team>` badge placed below the slot rather than compressed inside the team row.

The correct-winner badge is now a direct child of the slot button. This keeps it visible even when the normal pick value uses a single-line flex layout or a short bracket-cell height.

The center Final Four renderer now consumes the official comparison data it already received for `FINAL-LEFT` and `FINAL-RIGHT`:

- correct semifinal winner picks receive the green result outline;
- incorrect semifinal winner picks receive the red outline and struck-through pick;
- incorrect semifinal winner picks show the same `Correct: <flag> <team>` feedback.

The Final and third-place rows use the same mechanism automatically when their official results become available.

## Truth boundary

This is rendering only. It does not change:

- official knockout result data;
- player picks;
- scoring;
- advancement or reachability logic;
- Supabase persistence;
- bracket geometry.

## Verification

Added `tools/verify_wc2026_official_pick_result_embellishment.py` and wired it into `make verify`.

The verifier protects:

- the ordinary-slot correct-winner badge;
- the red incorrect-pick state;
- Final Four correct/incorrect classification;
- Final Four correct-winner feedback;
- the required CSS hooks.

## Capture fields

- WB_SESSION: restore missed-pick rendering and extend result embellishment to semifinals
- Changed: ordinary wrong-pick badge placement; Final Four official-result rendering; CSS; verifier; Makefile
- Authority: existing official knockout result truth and model comparison state
- Mutation: presentation and verification only
- Unresolved: visual browser review after local deployment
- Next: run the supplied verification and inspect one wrong quarterfinal pick plus both semifinal winner rows
