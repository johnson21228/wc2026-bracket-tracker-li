# Card 049 — Fix Game 2 Tiebreaker Verifier Indentation

## Intent

Repair the verifier after the Game 2 official seed/tiebreaker LI block was inserted outside the verifier function indentation.

## Acceptance

- `tools/verify_wc2026_bracket_tracker.py` compiles.
- `make verify` can run past the Game 2 tiebreaker LI verifier block.
- The Game 2 official seed/tiebreaker LI files remain required by verification.
