# Card 082 — Tune R32 Pick Card Slot Fit

## Intent

Ensure Round of 32 filled pick cards fit inside the pixel-defined slot space on the gameboard.

## Changes

- Add R32 pick-card slot fit LI.
- Add feature documentation.
- Patch Game 1 rendering so cards are constrained to `boundsPx`.
- Make flags as large as the slot height reasonably allows.
- Fit team names within the card before truncation.

## Verification

- `make verify`
- `python3 tools/verify_wc2026_r32_pick_card_slot_fit_patch.py`
- Visual review of `site/game1/index.html`
