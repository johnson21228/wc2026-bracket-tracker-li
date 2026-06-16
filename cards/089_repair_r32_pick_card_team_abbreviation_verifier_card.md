# Card 089 — Repair R32 Pick Card Team Abbreviation Verifier

## Intent

Repair the verifier for the R32 pick-card team abbreviation authority work.

## Problem

The verifier incorrectly ran `node --check` directly against `site/game1/index.html`, which fails on Node versions that reject `.html` as an unknown module extension.

## Rule

HTML pages must be syntax-checked by extracting inline JavaScript into a temporary `.js` file first.

## Acceptance

- `make verify` passes after overlay residue is removed.
- `python3 tools/verify_wc2026_r32_pick_card_team_abbreviation_patch.py` passes.
- The verifier still guards the team-abbreviation rendering rule.
