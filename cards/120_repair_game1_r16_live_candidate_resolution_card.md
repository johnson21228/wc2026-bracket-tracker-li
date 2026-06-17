# Card 120: Repair Game 1 R16 Live Candidate Resolution

## Claim

`L-R16-01` should resolve candidate teams from live upstream R32 picks.

## Problem

The R16 slot can show `Waiting for both R32 teams` while the visual upstream R32 pick cards are already filled.

## Decision

Map logical R32 feeder IDs such as `L-R32-01` and `L-R32-02` to manifest slot IDs such as `R32-L-M1A` and `R32-L-M1B`.

## Acceptance Criteria

- `L-R16-01` resolves `L-R32-01` and `L-R32-02`.
- Manifest aliases such as `R32-L-M1A` and `R32-L-M1B` are accepted.
- R16 menu can show two live upstream teams when both R32 picks exist.
- The waiting message appears only when the upstream picks are actually missing.

## Files

- `site/game1/index.html`
- `tools/verify_wc2026_game1_r16_live_candidate_resolution_patch.py`
- `capture_back/CAPTURE_BACK_REPAIR_GAME1_R16_LIVE_CANDIDATE_RESOLUTION.md`
- `docs/features/game1_r16_live_candidate_resolution_repair.md`
- `li/world_cup/game1_r16_live_candidate_resolution_rule.md`
