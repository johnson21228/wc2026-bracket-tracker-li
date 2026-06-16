# Card 088 — Repair R32 Pick Card Team Abbreviation Authority

## Intent

Repair the Round of 32 pick-card LI and runtime so the compact card uses only the team abbreviation from `team.abbr`.

## Problem

Earlier rules and patches used overlapping terms: `abbr`, `code`, `display label`, and `card label`. The Game 1 runtime still had a full-name render path for the compact pick card.

## Accepted outcome

- Compact R32 pick card face shows flag + three-letter team abbreviation.
- Full team name appears in the tooltip/details surface.
- User-facing details say `Team abbreviation`, not `Code` or `Card label`.
- Game 1 compact rendering uses `r32TeamAbbreviation(team)`.
- Verification fails if the old full-name compact helper is still used.
