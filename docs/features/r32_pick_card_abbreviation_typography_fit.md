# R32 Pick Card Abbreviation Typography Fit

This repair follows the shift from full country names to three-letter team abbreviations on the compact R32 pick card.

The card face now uses a fixed abbreviation typography instead of per-team name fitting. This prevents the visual card from being resized or font-shrunk differently for Brazil, Ivory Coast, South Korea, etc.

## Desired result

- Compact face: large flag + `CIV`, `BRA`, `KOR`, etc.
- Same abbreviation font metrics for every team.
- No full team names on the card face.
- No per-team font-size fitting.
- Flag uses as much vertical space as practical without clipping.
- Tooltip/details remains responsible for the full team name and rule explanation.

## Implementation note

The runtime slot-fit pass still places the card inside `rule.boundsPx`. The typography repair only changes card-internal layout and disables older full-name fitting helpers.
