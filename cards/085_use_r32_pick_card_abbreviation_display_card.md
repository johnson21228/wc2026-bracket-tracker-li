# Card 085 — Use R32 Pick Card Abbreviation Display

## Intent

Make filled Round of 32 pick cards visually consistent by using the same font metrics for every team.

## Change

- Add an R32 pick-card abbreviation display LI rule.
- Render only the three-letter team abbreviation on the compact card face.
- Keep the full team name and slot/rule context in a single tooltip/details surface.
- Keep flag size as the dominant visual identifier.

## Acceptance

- All compact R32 pick cards use the same font size/style.
- Full team names are not rendered on the compact card face.
- Full team names remain visible in tooltip/details.
- Pick state and slot assignment behavior remain unchanged.
