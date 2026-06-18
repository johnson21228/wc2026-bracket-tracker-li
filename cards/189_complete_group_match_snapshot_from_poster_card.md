# Card 189 — Complete Group Match Snapshot from Poster Authority

## Intent

Align the current group-panel match evidence data with the Workbench's poster-derived group-stage schedule authority.

Each four-team World Cup group must have six group matches available to the runtime group panel. Completed matches may carry current result evidence, while not-completed matches may remain scheduled and show kickoff/date evidence when available.

## Scope

- Normalize `site/data/current/group_matches.json` so Groups A–L each contain six matches.
- Use `site/data/group_stage_matches_from_poster.json` as the group-match schedule authority.
- Preserve completed match scores, kickoff times, and ESPN/manual evidence already present in the current snapshot when they correspond to poster fixtures.
- Add missing poster fixtures as scheduled local snapshot matches.
- Mark the current match snapshot source notes so poster-derived schedule authority is explicit.
- Add verification that every group has six current match records.

## Out of scope

- Third-place R32 allocation semantics.
- Live ESPN/FIFA runtime scraping.
- Pick eligibility changes.
- Group standings refresh.
