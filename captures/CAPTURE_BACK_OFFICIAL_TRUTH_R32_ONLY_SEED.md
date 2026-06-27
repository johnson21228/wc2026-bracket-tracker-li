# Capture Back: Official Truth R32-Only Seed

## Intent

Official truth should currently seed only the known Round of 32 team occupants.

The site-owned official truth JSON must not prefill later-round winners before knockout matches are actually decided. R16, QF, SF, Final, third-place, and Champion truth picks should remain absent until those results are known and intentionally entered.

## Runtime rule

`site/data/current/official_truth.json` may contain `picksBySlot` entries for `*-R32-*` slots.

Any `picksBySlot` entry outside Round of 32 is considered stale or premature result truth during the current pre-knockout seed state.

## Why

Players should pick winners themselves. Official truth is used for scoring and standings comparison. If later-round official picks remain seeded too early, standings/scoring can look like outcomes are known before they are actually official.

## Verification

`tools/verify_wc2026_official_truth_r32_only_seed.py` enforces that every `picksBySlot` key in `site/data/current/official_truth.json` is an R32 slot.
