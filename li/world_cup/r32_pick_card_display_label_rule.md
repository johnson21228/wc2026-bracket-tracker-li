# R32 Pick Card Display Label Rule

The compact Round of 32 pick card uses a three-letter display label, not the full team name.

## Terminology

- **Full team name**: the human-readable team name, such as `Ivory Coast`.
- **Three-letter display label**: the compact three-character label used on the pick card face, such as `CIV`.
- **Data field**: the current team data stores this label as `abbr`.

The UI should not call this compact pick-card value merely `Code` unless the surface is intentionally describing a formal source code. For user-facing Game 1 pick-card details, prefer `Card label` or `3-letter label`.

## Compact card rule

A filled R32 pick card face must show:

1. the selected team flag
2. the selected team's three-letter display label

The full team name must not be rendered on the compact pick-card face.

## Tooltip/details rule

The tooltip or details surface may show the full team name and the card label together:

- Full name: Ivory Coast
- Card label: CIV
- Group: E
- Slot: 2B
- Meaning: Runner-up Group B

The full team name is the primary explanatory value in the details surface. The three-letter label is secondary and explains what is shown on the compact card.

## Runtime safety

All R32 pick-card rendering paths must use one helper for the compact label. The helper may read `team.abbr`, but the rendered UI concept is `r32PickCardLabel(team)`.
