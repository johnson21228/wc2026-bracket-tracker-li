# Knockout Pub Background Image Prompt Rule

# Knockout Pub Background Runtime Image and Update Prompt Rule

The Workbench must keep the knockout pub background as a generated static site asset backed by current JSON truth and an explicit reusable update prompt.

Runtime target:

- `site/assets/board/knockout_pub_background.jpeg`

Required prompt:

- `prompts/update_knockout_pub_background_image.md`

Required workflow doc:

- `docs/workflows/update_knockout_pub_background_image.md`

Required manifest:

- `source/text/knockout_pub_background_generated_manifest.json`

Data authorities:

- `site/data/current/knockout_matches.json` is schedule authority.
- `site/data/current/official_truth.json` is known R32 team-occupant truth and known team/truth authority.
- `site/data/model/teams.json` supplies team identity and flag emoji metadata.
- The generated JPEG is only a visual projection; JSON remains authority.

Runtime rule:

- The site must use `site/assets/board/knockout_pub_background.jpeg` as the knockout-board/pub-calendar background.
- Replacing that file is the supported background update path.
- This must not change gameplay logic, Supabase state, picks, scoring, standings, or pick menus.

Next-update rule:

- Future `UPDATE KNOCKOUT PUB BACKGROUND IMAGE` runs must use the latest accepted runtime image as the base image.
- Future runs should behave as incremental refreshes: preserve approved calendar layout and replace only newly resolved `TBD` rows when authoritative data is present.
- Do not redraw or redesign the whole poster unless explicitly requested.

Visual rules:

- Preserve the pub-photo-inspired calendar/poster look.
- Keep the calendar-card layout, red date headers, parchment card bodies, title area, and warm pub wall feel.
- Keep the upper-left bulb/neon sign dimmed.
- Place `Flag vs Flag`, `vs`, and `TBD` directly on the date-card background.
- Do not draw individual row frames, row boxes, borders, pills, rounded rectangles, or highlight bands.
- Flags should be as tall as they can be while fitting cleanly.
- `TBD` must be tiny/subtle.
- `vs` must be tiny/subtle and aligned to the visual centerline of the flags.
- Do not add footer/caption/provenance text under the calendar.

Truth rules:

- Do not invent teams.
- Do not guess unresolved winners.
- If both teams are authoritative, render `Flag vs Flag`.
- If either side is unknown, render tiny/subtle `TBD`.
- Do not render feeder labels, match IDs, kickoff times, or long team names in the final row.
