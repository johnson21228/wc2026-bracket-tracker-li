# Card 247: Final Four pick display

## Status

Implemented

## Goal

Use the CENTER-FINAL-FOUR geometry as a visual container for the canonical Final Four pick display.

## Requirements

- Keep CENTER-FINAL-FOUR visual-only.
- Render FINAL-LEFT and FINAL-RIGHT as semifinal-winner picks.
- Render CHAMPION as the final winner pick.
- Render THIRD-PLACE-WINNER as the third-place winner pick.
- Route all choices through the existing controller/model pick pipeline.
- Avoid adding a separate storage model.

## Verification

`tools/verify_wc2026_final_four_pick_display.py`
