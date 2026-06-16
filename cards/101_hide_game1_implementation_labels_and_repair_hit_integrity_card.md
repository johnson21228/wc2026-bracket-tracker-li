# Card 101 — Hide Game 1 Implementation Labels and Repair Hit Integrity

## Intent
Hide raw implementation slot labels from the Game 1 board UI and double-check that R32 hit regions open the correct menus.

## Why
After the uniform SVG board migration, labels such as `3 C/D/F/G/H` can be visually confusing and appear associated with a neighboring card. These labels are implementation representation, not player-facing UI.

## Done when
- `.slotLabel` / `.pickRule` implementation labels are hidden in normal UI.
- R32 slot geometry is applied from the uniform SVG manifest.
- Position 8 remains the `3 C/D/F/G/H` third-place pool rule.
- Position 7 remains `1I` / Winner Group I.
- Verifiers pass.
