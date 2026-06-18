# Group Match Snapshot Poster Truth

The group panel runtime expects every four-team group to expose all six group-stage matches as local checked-in model data.

The Workbench's group-stage match schedule originated from the poster-derived source file:

- `site/data/group_stage_matches_from_poster.json`

That poster-derived artifact is the schedule authority for the current local group-match snapshot. Current or manually normalized evidence may still provide match results, kickoff times, and external IDs, but it must not remove poster fixtures from the local group-match model.

## Runtime rule

The site runtime reads only local checked-in JSON:

- `site/data/current/group_matches.json`
- `site/data/current/match_highlights.json`

It must not fetch, parse, or scrape ESPN at runtime.

## Group panel expectation

For every group A–L, the group panel should have six total matches:

- completed matches render result-first
- not-completed matches render kickoff/time/date evidence, or `Time TBD` when no time is available
- highlight links render only when local checked-in highlight data has a URL

## Data rule

If `site/data/current/group_matches.json` contains fewer than six matches for any group, verification should fail unless a future LI explicitly marks the snapshot as intentionally partial.
