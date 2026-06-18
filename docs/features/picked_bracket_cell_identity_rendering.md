# Picked Bracket Cell Identity Rendering

Picked bracket cells render as compact game-board identity tokens:

`[flag visual] [3-letter code]`

The filled bracket cell should be quick to scan. Full country names remain available in menus, panels, tooltips, and accessible labels, but not as visible text inside the compact picked cell.

## Runtime posture

The current runtime may use emoji flags from the selected team model. Emoji flags are scaled with `font-size` so the flag visual occupies most of the available cell height.

The LI contract says "flag visual" rather than "emoji flag" so later image/SVG flag assets can replace emoji without changing the user-facing rule.

## Acceptance

- Picked cells show flag visual plus canonical three-letter code.
- Picked cells do not visibly show the full team name.
- Flag visual scales to the cell height.
- Code comes from `selectedTeam.abbr` or existing selected-team id fallback.
