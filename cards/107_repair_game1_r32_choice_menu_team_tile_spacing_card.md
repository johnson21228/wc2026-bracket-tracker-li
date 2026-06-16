# Card 107 — Repair Game 1 R32 Choice Menu Team Tile Spacing

## Intent

Fix the active Game 1 R32 choice menu renderer so team names and metadata are visually separated.

## Acceptance

- The active `.teamTile` path is repaired.
- `.teamMeta` provides layout separation between `.teamName` and `.teamDetail`.
- `.teamDetail` has an explicit margin fallback.
- The menu no longer visually renders joined labels like `BrazilBRA`.
