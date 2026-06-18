# Capture Back: Picked Bracket Cell Identity Rendering

## Change
Defined and implemented the picked bracket cell as a compact identity token:

`[flag visual] [3-letter code]`

## Why
A filled bracket cell should be quickly scannable. The full team name belongs in explanatory surfaces, not inside the compact game-board cell.

## Implementation note
The current runtime can use emoji flags and scale them with font size. The LI rule intentionally says "flag visual" so image/SVG flags can replace emoji later without changing the contract.

## Verification
Added `tools/verify_wc2026_picked_bracket_cell_identity_rendering.py` and wired it into `make verify`.
