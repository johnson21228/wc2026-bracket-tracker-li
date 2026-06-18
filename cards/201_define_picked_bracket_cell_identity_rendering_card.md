# Card 201: Define and Implement Picked Bracket Cell Identity Rendering

## Intent
Make filled bracket cells scan like game-board tokens.

## Rule
A picked bracket cell renders only the team flag visual and canonical three-letter code.

## Implementation
Use the selected team's existing flag visual, currently emoji, scaled to the cell height. Show the selected team's canonical `abbr` value beside it.

## Acceptance
- Runtime picked cells include `.picked-cell-identity`.
- Runtime picked cells include `.picked-cell-flag`.
- Runtime picked cells include `.picked-cell-code`.
- Full team name is not visible inside the picked cell.
- Full team name may remain in menus, panels, tooltips, and accessible labels.
- Verification is wired into `make verify`.
