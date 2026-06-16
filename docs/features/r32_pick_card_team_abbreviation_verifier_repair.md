# R32 Pick Card Team Abbreviation Verifier Repair

The team-abbreviation authority overlay applied, but its verifier attempted to run `node --check` directly against `site/game1/index.html`.

Recent Node versions reject `.html` as an unknown file extension. The repaired verifier extracts inline script blocks from the HTML page and checks the extracted JavaScript as a temporary `.js` file.

The verifier still checks the intended behavior:

- compact R32 pick cards use `r32TeamAbbreviation(pick)`
- compact R32 pick cards do not render full team names
- tooltip/details language uses `Team abbreviation`
- all team records expose a valid three-character `team.abbr`
- Game 1 inline JavaScript parses when Node is available
