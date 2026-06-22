# Card 251: Final Stack SVG Truth

## Goal

Adopt the approved final-stack SVG layout as the geometry truth for semifinal winners and champion placement.

## Scope

- SVG-first geometry change.
- Derived manifest updates only.
- No pick storage changes.
- No scoring changes.
- No pick menu candidate changes.

## Acceptance

- `FINAL-LEFT`, `FINAL-RIGHT`, and `CHAMPION` are derived from `site/assets/playfield/uniform_pick_card_gameboard.svg`.
- `CHAMPION` is same-size as the SF-winner slots and centered on the SVG centerline.
- `FINAL-LEFT` and `FINAL-RIGHT` are mirrored around the centerline.
- Existing Final Four display and pick rendering verifiers still pass.
