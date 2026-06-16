# R32 Pick Card Team Abbreviation Rule

An R32 pick card is the compact filled-slot card rendered inside a board-defined Round of 32 slot.

## Vocabulary

Use these terms only:

- **Full team name**: the human-readable country/team name, such as `Ivory Coast`.
- **Team abbreviation**: the canonical three-letter compact country/team abbreviation stored in `team.abbr`, such as `CIV`.
- **R32 pick card face**: the compact always-visible card inside the game-board slot.
- **R32 pick details surface**: the tooltip/popover/details surface for full name and rule context.

Do not use `Code`, `Card label`, or `display label` for the compact visible value. Those terms created ambiguity between source data, FIFA codes, and UI labels.

## Rendering rule

The R32 pick card face must render:

1. the team flag, as large as the slot permits; and
2. the team abbreviation from `team.abbr`.

The R32 pick card face must not render the full team name.

## Details rule

The R32 pick details surface must render the full team name first and may show the team abbreviation as explicit secondary metadata:

- Full team name: Ivory Coast
- Team abbreviation: CIV

The details surface may also show group, slot rule, eligible source groups, and interaction text.

## Runtime invariant

All compact R32 pick-card face rendering must go through one helper:

```js
r32TeamAbbreviation(team)
```

The helper must read `team.abbr` first and return a three-character uppercase value. Fallbacks may exist only to keep the UI alive during incomplete data, but verification must require all 48 teams to have valid `team.abbr` values.
