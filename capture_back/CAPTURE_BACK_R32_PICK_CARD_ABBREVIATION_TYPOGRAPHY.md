# Capture Back — R32 Pick Card Abbreviation Typography

## Captured issue

The card now correctly shows the three-letter abbreviation, but the typography and slot-internal layout need tuning. The flag and abbreviation should feel intentional, consistent, and unclipped.

## Captured decision

R32 pick cards are abbreviation cards, not full-name cards. Since abbreviations are fixed length, the runtime should use one shared font size/style instead of shrinking labels per team.

## Added LI

- `li/world_cup/r32_pick_card_abbreviation_typography_rule.md`

## Patched surface

- `site/game1/index.html`

## Verifier

- `tools/verify_wc2026_r32_pick_card_abbreviation_typography_patch.py`
