# Group-stage full match time rule

All 72 World Cup 2026 group-stage matches must carry explicit kickoff time fields in the checked-in schedule model.

- `site/data/current/group_matches.json` is the runtime group panel source.
- `site/data/group_stage_matches_from_poster.json` is the poster-derived group-stage fixture source.
- `data/group_stage_matches_from_poster.json` is retained as a compatibility mirror when present.
- Kickoff times must not be implied from display order.
- The UI may render TBD teams for projected knockout fixtures, but a scheduled group-stage match must not render as `Time TBD` when published schedule evidence exists.
- FIFA remains the official schedule authority. ESPN's FIFA World Cup schedule page is accepted here as a parseable kickoff-time evidence source and cross-check.
- Stored `kickoffLocal` and `kickoffET` values are normalized to `America/New_York` for the current runtime display model.
