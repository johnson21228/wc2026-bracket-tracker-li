# R32 Pick Card Abbreviation Display Rule

An R32 pick card is the compact filled-slot visual card that represents the team occupying a Round of 32 bracket slot.

## Rule

The compact R32 pick card face must render only:

- the selected team flag;
- the selected team's three-letter abbreviation.

The compact card face must not render the full team name, slot code, qualification rule, or route text.

## Abbreviation authority

The team abbreviation is the display code from tournament team data, preferably `abbr`. It must be normalized to uppercase and exactly three visible characters for the compact card.

If a team record lacks `abbr`, the UI may fall back to `code` or a derived three-letter display fallback, but this is a data-quality defect that verification should expose.

## Tooltip/details surface

The full team name belongs in the tooltip/details surface, not on the compact card face. The tooltip/details surface may show the full name, abbreviation, group, slot rule, qualification route, and change-pick interaction.

## Safety invariant

Changing compact card text from full name to abbreviation must not change pick identity, pick persistence, slot ids, slot rules, eligibility, data loading, or menu behavior.
