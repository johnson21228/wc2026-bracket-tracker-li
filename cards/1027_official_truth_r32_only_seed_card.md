# Card 1027: Official Truth R32-Only Seed

## Goal

Clear all site-owned official truth picks except known Round of 32 team occupants.

## Files

- `site/data/current/official_truth.json`
- `captures/CAPTURE_BACK_OFFICIAL_TRUTH_R32_ONLY_SEED.md`
- `cards/1027_official_truth_r32_only_seed_card.md`
- `li/world_cup/official_truth_r32_only_seed_rule.md`
- `tools/verify_wc2026_official_truth_r32_only_seed.py`

## Acceptance

- `official_truth.json` keeps R32 occupant truth.
- `official_truth.json` has no non-R32 winner/result picks.
- Verification fails if non-R32 official truth is reintroduced prematurely.
