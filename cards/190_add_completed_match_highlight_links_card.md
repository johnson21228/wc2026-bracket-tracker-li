# Card 190 — Add Completed Match Highlight Links

## Intent

Store verified highlight/video links for completed World Cup 2026 group-stage matches so the group panel can open completed-match highlights when local checked-in evidence has a URL.

## Scope

- Update `site/data/current/match_highlights.json`.
- Preserve the checked-in group match/result snapshot as the score authority.
- Store only verified external highlight URLs.
- Keep runtime scraping out of scope.
- Keep third-place menu semantics out of scope.

## Acceptance

- Every completed match in `site/data/current/group_matches.json` has a highlight entry with provider, title, URL, verification date, match evidence, and verification note.
- The group panel runtime still opens highlight links in a new tab/window using external-link best practice.
- `make verify` passes.
