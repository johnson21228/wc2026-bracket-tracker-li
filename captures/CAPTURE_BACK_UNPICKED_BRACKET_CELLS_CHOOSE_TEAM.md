# Capture Back: Unpicked Bracket Cells Choose Team

## Intent

Empty/unpicked bracket cells render the centered player-facing prompt:

`Choose Team`

## Scope

View-only rendering change. No pick storage, pick IDs, assignment logic, FIFA bridge logic, scoring, result data, picked-cell rendering, or pick menu candidate logic changes.

## Verification

`tools/verify_wc2026_unpicked_bracket_cells_choose_team.py` verifies the helper returns `Choose Team`, does not use internal slot IDs as visible fallback text, keeps picked-cell identity rendering intact, and centers the empty-cell label through CSS.
