# Group Standings Model Data

The group standings panel uses checked-in JSON model data rather than runtime scraping.

## Data files

```text
site/data/current/group_standings.json
site/data/current/group_matches.json
site/data/current/match_highlights.json
```

## Update workflow

A later CB can refresh these files when ESPN/FIFA standings change:

1. Capture the source and timestamp.
2. Update `source.capturedAt`, `source.url`, and `source.notes`.
3. Replace changed standings rows and match rows.
4. Leave unknown highlight links empty rather than inventing URLs.
5. Run `make verify` and `make pack`.

## Model functions

The clean MVC model exposes:

- `getGroupStandings(groupId)`
- `getGroupMatches(groupId)`
- `getMatchHighlights(matchId)`
- `getGroupContext(groupId)`
- `getThirdPlaceTable()`
