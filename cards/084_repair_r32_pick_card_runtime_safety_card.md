# Card 084 — Repair R32 Pick Card Runtime Safety

## Intent

Recover Game 1 pick rendering after a fixed-font-metrics card patch broke runtime JavaScript.

## Scope

- Remove raw newline JavaScript display-name literals from `site/game1/index.html`.
- Preserve R32 pick-card rendering.
- Add LI that separates card typography from runtime pick-state safety.
- Add a verifier for the specific failure mode.

## Done when

- `make verify` passes.
- `python3 tools/verify_wc2026_r32_pick_card_runtime_safety_patch.py` passes.
- Game 1 picks render again.
