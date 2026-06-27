# UPDATE KNOCKOUT PUB BACKGROUND IMAGE Workflow

This workflow regenerates the Bracketeering Pub knockout background image from current site truth.

Runtime target:

- `site/assets/board/knockout_pub_background.jpeg`

Base/reference image for every future update:

- the latest accepted runtime image at `site/assets/board/knockout_pub_background.jpeg`

The workflow is incremental. It should preserve the current accepted calendar/poster image and replace only newly resolved `TBD` rows when `site/data/current/official_truth.json` now has authoritative teams for that match.

Authoritative data inputs:

- `site/data/current/knockout_matches.json` for dates, matches, rounds, times, venues, and bracket edges.
- `site/data/current/official_truth.json` for known official R32 occupants and later authoritative truth.
- `site/data/model/teams.json` for team abbreviation and flag emoji metadata.
- `site/data/current/group_standings.json` only when it helps resolve current official truth references without guessing.

The image is a generated projection. It must not become the schedule authority.

Calendar rules:

- Preserve the pub-photo-inspired calendar/poster layout.
- Preserve date cards, red date headers, parchment card bodies, warm pub lighting, and the dimmed upper-left bulb/neon sign.
- Update only match rows inside existing date cards.
- Known match rows render as `Flag vs Flag` using high-resolution flag images generated from flag emoji.
- Unresolved rows render as tiny/subtle `TBD`.
- The `vs` marker is tiny/subtle and aligned to the visual centerline of the flags.
- Flags, `vs`, and `TBD` sit directly on the calendar-card background.
- Do not draw row frames, row boxes, rounded rectangles, pills, highlight bands, or borders.
- Do not add any footer/caption/provenance line under the calendar.

Runtime rule:

- The site uses `site/assets/board/knockout_pub_background.jpeg` for the knockout-board background.
- Replacing that asset updates the site background without changing gameplay logic.

The prompt for this workflow is:

- `prompts/update_knockout_pub_background_image.md`
