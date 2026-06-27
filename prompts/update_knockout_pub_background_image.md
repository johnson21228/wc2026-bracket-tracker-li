# UPDATE KNOCKOUT PUB BACKGROUND IMAGE

Use this prompt when the knockout pub background needs to be regenerated from current site data.

## Trigger

```text
UPDATE KNOCKOUT PUB BACKGROUND IMAGE
```

## Role

You are updating the WC2026 Bracketeering knockout pub background image. This is a visual asset generation task, not a runtime/UI redesign task.

## Runtime target

The site uses this exact image as the knockout-board pub background:

```text
site/assets/board/knockout_pub_background.jpeg
```

Generate a replacement for that same path. Do not create a new runtime image path unless explicitly asked.

## Base image

The accepted base image for each future update is the latest runtime file.

## Base image for the next update

Use the current runtime image as the base/reference image:

```text
site/assets/board/knockout_pub_background.jpeg
```

This matters: future updates should start from the latest accepted calendar image, not from an older draft. Preserve the latest accepted composition, lighting edits, row placement, flag scale, subtle `vs`, subtle `TBD`, and no-footer cleanup.

The base image is inspired by a real pub photo of the WC2026 group-stage match schedule poster. Preserve that look. The output should look like the same pub calendar/poster artifact, not a new dashboard, not a new bracket UI, and not a generic schedule graphic.

## Data authorities

Read current site data from:

```text
site/data/current/knockout_matches.json
site/data/current/official_truth.json
site/data/model/teams.json
site/data/current/group_standings.json
```

Use `knockout_matches.json` for dates and match rows. Use `official_truth.json` for authoritative known teams. Use team data only to resolve each known team’s associated flag emoji.

## Update behavior for future runs

Treat this as an incremental calendar refresh:

- Keep already-approved resolved `Flag vs Flag` rows in the same style and position unless the authoritative data changed.
- Replace only `TBD` rows whose teams are now authoritative in `official_truth.json`.
- Leave unresolved rows as tiny/subtle `TBD`.
- Do not move date cards, redraw the overall poster, or redesign the calendar just because new teams were added.
- Do not reintroduce footer/caption/provenance text.
- Do not brighten the upper-left bulb or neon sign again.

## Visual requirements

Preserve the current runtime image calendar layout as closely as possible:

- Keep the same pub wall / poster / warm sports-bar atmosphere.
- Keep the same overall calendar grid and date-card arrangement.
- Keep the same red date headers, parchment cards, title area, and poster-like texture.
- Keep upper-left bulb/neon lighting dimmed so it does not compete with the calendar.
- Do not replace the calendar with a new layout.
- Do not add a modern table, dashboard, bracket diagram, or app UI.
- The generated background should look very similar to the current runtime image at a glance.

Only update the match rows inside the existing date cards.

## Match-row rendering

For each date card:

- Show the date at the top, following the base image calendar style.
- Show one row for each knockout match on that date. In other words, render one row for each match in the schedule for that day.
- Each known match row should contain only:

```text
Flag vs Flag
```

- Generate the flag images from the associated team flag emoji.
- Render the flags as high-resolution image glyphs, not as tiny text.
- Make each flag as tall as possible while still fitting cleanly inside the row; the flag should be as tall as it can be without crowding the row.
- Place the flags and `vs` directly over the existing calendar-card background.
- Do not draw any frame, outline, rounded rectangle, box, pill, panel, highlight band, or border around individual match rows.
- Do not put the row data inside a separate container.
- A subtle flag shadow is acceptable only if it helps readability; it must not read as a row frame.
- Keep the row uncluttered and poster-like.

For any match where either team is not yet authoritative, render the whole row as:

```text
TBD
```

The `TBD` text must be tiny, quiet, and subtle. It should be the smallest readable label that still communicates unresolved status. Do not let `TBD` compete visually with known flag rows, date headers, or the poster title. Prefer muted dark ink with reduced opacity, centered in the row.

The `TBD` text must sit directly on the calendar-card background with no row frame, no box, and no border.

The `vs` between flags must be tiny, quiet, subtle, and aligned to the visual centerline of the flags. Raise it as needed so it sits on the flag centerline rather than dropping low.

## Forbidden visual additions

Do not add any footer, caption, provenance line, generation note, metadata text, or explanatory text under the calendar.

Do not render text such as:

```text
Updated from site data
flags from emoji
unresolved matches TBD
```

anywhere in the image.

## Truth rules

Do not rely on memory. Read the current repo files every time before deciding which rows are known or unresolved.

- Do not invent teams.
- Do not guess teams.
- Do not guess unresolved winners.
- Do not use provisional or likely teams unless they are already present in `official_truth.json`.
- Do not render feeder labels such as `1A`, `2B`, `W73`, or `3C/E/F/H/I` in the final image.
- Do not render match IDs, kickoff times, or long team names in the final row text.
- If both teams are known, render `Flag vs Flag`.
- If either side is unknown, render tiny/subtle `TBD`.

## Output

Create a replacement background image suitable for:

```text
site/assets/board/knockout_pub_background.jpeg
```

Also produce a small manifest at:

```text
source/text/knockout_pub_background_generated_manifest.json
```

The manifest should describe:

- the base image used
- the site data files used
- which rows rendered `Flag vs Flag`
- which rows rendered `TBD`
- confirmation that no individual row frames/boxes were drawn
- confirmation that no footer/caption/provenance text was drawn under the calendar
- confirmation that this was treated as an incremental update from the latest accepted runtime image

The image should remain a background asset. Do not change gameplay logic, site controls, Supabase data, bracket runtime, pick menus, standings, or scoring.


## Local verification after applying a generated replacement

After placing the generated image and manifest in the repo, run:

```bash
make verify
make pack
```
