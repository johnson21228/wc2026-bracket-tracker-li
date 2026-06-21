# Card 243: Center Final Four Visual Only

## Goal

Do not render the center Final Four geometry slot as a player-facing pick button.

## Scope

- Keep `CENTER-FINAL-FOUR` as SVG/geometry board authority.
- Exclude `CENTER-FINAL-FOUR` / `FINAL_FOUR` from MVC pick-slot rendering.
- Preserve the center visual box on the gameboard.
- Verify the filter so the internal slot ID cannot appear as board copy.

## Verification

Run:

- `python3 tools/verify_wc2026_center_final_four_visual_only.py`
- `make verify`
