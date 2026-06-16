# Card 090 — Tune R32 Pick Card Abbreviation Typography

## Intent

Refine the filled R32 pick card now that the compact card uses a three-letter team abbreviation.

## Problem

Earlier typography overlays were designed for full country names. They introduced per-team fitting logic and large full-name card dimensions. After switching to abbreviations, that logic is no longer appropriate and can create clipped or visually inconsistent cards.

## Change

- Keep the compact face as flag + team abbreviation.
- Use one fixed abbreviation font metric for all teams.
- Make the flag large within slot height.
- Remove per-team font shrinking from abbreviation rendering.
- Keep full team name in tooltip/details only.

## Verification

Run `tools/verify_wc2026_r32_pick_card_abbreviation_typography_patch.py`.
