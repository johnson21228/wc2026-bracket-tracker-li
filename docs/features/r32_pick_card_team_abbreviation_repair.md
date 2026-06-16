# R32 Pick Card Team Abbreviation Repair

This repair resolves the R32 pick-card terminology and rendering confusion.

The compact card inside the Round of 32 board slot must use the three-letter **team abbreviation** from `team.abbr`, not the full team name and not a generic field called `Code`.

Example:

- Full team name: Ivory Coast
- Team abbreviation: CIV
- R32 pick card face: flag + CIV
- R32 pick details surface: Ivory Coast, Team abbreviation: CIV, group/slot context

The repair updates Game 1 so the compact card face routes through `r32TeamAbbreviation(team)` and the details surface uses `Team abbreviation`, not `Code` or `Card label`.
