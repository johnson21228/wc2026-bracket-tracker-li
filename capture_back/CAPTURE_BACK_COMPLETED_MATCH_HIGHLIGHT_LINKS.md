# Capture Back — Completed Match Highlight Links

## Captured change

Added verified external highlight/video links for completed World Cup 2026 group-stage matches to `site/data/current/match_highlights.json`.

## Boundary

- Local checked-in JSON remains the runtime source.
- No runtime scraping was added.
- Pick logic and third-place menu semantics are unchanged.
- Group match results remain governed by `site/data/current/group_matches.json`.

## Report

- Completed matches in current snapshot: 24
- Highlight links newly stored by this CB when absent: up to 24
- Completed matches intentionally left missing: 0 for the current snapshot
- Explicit check: United States 4-1 Paraguay now has a verified FOX Sports highlight URL.

## Runtime behavior

The group panel may render completed matches as links only when a match ID appears in `match_highlights.json` with a valid URL. External links must open in a new tab/window with `target="_blank"` and `rel="noopener noreferrer"`.
