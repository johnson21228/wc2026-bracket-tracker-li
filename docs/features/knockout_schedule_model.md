# Knockout Schedule Model

This feature captures the knockout-round schedule required by the WC2026 site.

Runtime data:

- `site/data/current/knockout_matches.json`

Design/source evidence:

- `source/text/knockout_schedule_evidence_20260618.json`
- `source/images/wc2026_knockout_pub_calendar_background.jpeg`
- `source/text/knockout_pub_calendar_background_manifest.json`

Runtime image projection:

- `site/assets/board/knockout_pub_background.jpeg`

The generated pub background is atmospheric. It is not the schedule authority. The JSON model owns dates, times, venues, timezones, and bracket edges.

The corrected pub image must communicate the correct scope: 32 teams qualify for the knockout stage, not 24.
