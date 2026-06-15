# Card 000 — Capture Initial Group-Stage Schedule From Poster

## Status

Captured Back.

## Intent

Preserve the uploaded poster image and derive starter group-stage match data from it.

## Source

- `source/images/match_schedule_group_stage_poster_michelob_ultra.jpeg`

## Derived data

- `data/group_stage_matches_from_poster.json`
- `data/groups_from_poster.json`
- `source/text/poster_transcription.md`

## Acceptance

- Original image is preserved.
- Structured match data includes date, group, home team, away team, and abbreviations.
- Data is marked as poster-derived and pending official verification.
- Any visual ambiguity is recorded rather than silently corrected.
- The project origin story is captured:
  `photo in a bar → structured data → static game → evolving pool site`.

## Capture Back

- `capture_back/CAPTURE_BACK_CARD_000_POSTER_SOURCE.md`
