# Knockout Pub Background Image Prompt Rule

The Workbench must keep a reusable prompt for updating the Bracketeering Pub knockout background image from current site truth.

Required prompt:

- `prompts/update_knockout_pub_background_image.md`

Runtime target:

- `site/assets/board/knockout_pub_background.jpeg`

Rules:

- Use `site/data/current/knockout_matches.json` as schedule authority.
- Use `site/data/current/official_truth.json` as known R32 team-occupant truth.
- Use the existing runtime image as the base/reference image.
- Group the generated image by date.
- Show the date at the top of each day section.
- Show one row for each match.
- Known rows render as `Flag vs Flag`.
- Unknown or uncertain rows render as `TBD`.
- Flags should be as tall as they can be while fitting cleanly in the row.
- Do not guess teams when slot-to-match mapping is uncertain.
- The image is a projection only; JSON remains authority.
