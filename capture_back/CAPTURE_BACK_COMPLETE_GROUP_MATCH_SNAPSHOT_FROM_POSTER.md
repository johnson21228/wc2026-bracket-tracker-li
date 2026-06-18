# Capture Back — Complete Group Match Snapshot from Poster Authority

## Captured decision

The group panel should show all group matches, not only the matches present in a partial current-results snapshot.

Because the site and workbench started from the poster-derived World Cup schedule surface, `site/data/group_stage_matches_from_poster.json` is treated as the local schedule authority for group-stage match fixtures.

## Implementation

This CB completes `site/data/current/group_matches.json` from the poster-derived group-stage fixture file:

- every Group A–L has six matches
- existing completed/current evidence is preserved where it matches a poster fixture
- missing poster fixtures are added as scheduled local snapshot entries
- source notes record that poster-derived fixtures are the current schedule authority

## Runtime boundary

The browser runtime continues to read local checked-in JSON only. It does not scrape ESPN or any other live source at runtime.

## Deferred

Third-place slot allocation and third-place menu semantics are intentionally deferred.
