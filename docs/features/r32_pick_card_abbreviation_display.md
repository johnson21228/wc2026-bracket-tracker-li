# R32 Pick Card Abbreviation Display

This capture defines the compact rendering for filled Round of 32 pick cards.

The board-defined slot rectangle remains the authority. To keep every team visually consistent, the compact card uses the team's three-letter abbreviation instead of the full team name. The tooltip/details surface carries the full team name and rule context.

## Compact card

The compact card shows:

- large flag;
- three-letter abbreviation.

It does not show:

- full team name;
- slot code such as `2A`;
- rule text such as `Winner Group E`;
- eligible source groups.

## Tooltip/details

The tooltip/details surface shows the full identity and rule context. Example:

```text
Ivory Coast
Code: CIV · Group E
Slot: 1E
Winner Group E
Eligible source: Group E
Click/tap to change pick
```

## Rendering boundary

Tournament data owns the team code and full name. Qualification rules own slot meaning. The UI surface decides how to render the compact card and details surface. The compact card label is display-only and must not become a data key.
