# Card 087 — Repair R32 Pick Card Display Label Language

## Intent

Repair the R32 pick-card abbreviation implementation so the compact three-letter value is treated as a card display label, while the full country/team name remains available in the tooltip/details surface.

## Acceptance

- Compact filled R32 pick cards render the three-letter label.
- Full names do not appear on compact card faces.
- Tooltip/details surfaces show the full name.
- Tooltip/details surfaces describe the compact value as `Card label` or `3-letter label`, not ambiguous `Code`.
- All 48 team records have a three-letter `abbr` value.
