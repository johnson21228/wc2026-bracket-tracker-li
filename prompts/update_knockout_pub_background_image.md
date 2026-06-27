# UPDATE KNOCKOUT PUB BACKGROUND IMAGE

You are helping me maintain the `wc2026-bracket-tracker-li` Workbench repo.

Repo root:

`/Users/stevejohnson/Developer/wc2026-bracket-tracker-li`

LI means Language Infrastructure. CB means Capture Back.

## Trigger phrase

When I say **UPDATE KNOCKOUT PUB BACKGROUND IMAGE**, use this prompt.

## Task

Generate the most up-to-date knockout-round gameboard background image for the Bracketeering Pub site.

The runtime target image is:

- `site/assets/board/knockout_pub_background.jpeg`

Use the existing runtime image as the base/reference image:

- Base image: `site/assets/board/knockout_pub_background.jpeg`

The replacement image must follow the same overall visual style, mood, composition language, and pub/gameboard feel as the base image. Do not redesign the whole board into a different visual product.

## Grounding rule

Do not rely on memory.

Before generating or editing the image, inspect the latest repo data and source truth available in the current repo or latest uploaded pack.

Start with:

- `site/data/current/knockout_matches.json`
- `site/data/current/official_truth.json`

Also inspect these files when present:

- `site/data/current/teams.json`
- `site/data/current/group_standings.json`
- `source/text/knockout_schedule_evidence_20260618.json`
- `source/text/knockout_pub_calendar_background_manifest.json`

The schedule JSON owns dates, match numbers, round names, times, venues, and bracket edges. The official truth JSON owns known R32 team occupants when available. The image is a projection, not schedule authority.

## Image concept

Create a clean pub-style knockout calendar/gameboard background.

Each day's image section must show:

1. The date at the top of that day's section.
2. One row for each match on that date.
3. Each known match row as:

`Flag vs Flag`

4. If either or both teams in a match are not yet known, show the row as:

`TBD`

Do not print long team names in match rows. Do not print bracket feeder codes like `1A`, `2B`, `W73`, or `3C/D/F/G/H` in the final image rows unless specifically asked in a later prompt. The image should be readable at gameboard scale.

## Flag rule

Use national flags for known teams.

Make each flag as tall as it can be while still fitting nicely inside the match row. The flags should feel prominent and legible, not tiny decoration.

Keep consistent row height and spacing. Avoid crowding. Preserve enough visual quiet space so the board remains usable as a background behind site overlays.

## Known-team resolution rule

Resolve teams from the current site truth only.

For Round of 32 rows, map known R32 occupants from `site/data/current/official_truth.json` into the corresponding R32 match row when the slot is known.

If the repo has an explicit mapping between R32 slot ids and knockout match numbers, use that mapping. If the mapping is not explicit, inspect the current runtime/data modules that render the board before guessing.

If a match cannot be confidently mapped to two known teams, render that row as `TBD`.

For later rounds whose teams depend on match winners, render `TBD` unless the repo has official completed winner truth for that match.

## Date grouping rule

Group rows by the `date` field from `site/data/current/knockout_matches.json`.

Use the repo's date values exactly. Do not invent or shift dates.

A good date header is compact and readable, for example:

- `JUNE 28`
- `JUNE 29`
- `JULY 1`
- `FINAL — JULY 19`

The header style should follow the base image's pub/chalk/calendar style.

## Layout rule

Prefer a calendar-board composition that fits all knockout dates cleanly.

The image should communicate the full tournament path without becoming a dense spreadsheet. Use day sections, compact rows, generous padding, and consistent alignment.

Rows should be simple:

- known: `🇧🇷  vs  🇩🇪`
- unknown: `TBD`

The exact flags shown must come from current repo truth.

## Style rule

Follow the base image style:

- pub/gameboard atmosphere
- warm/bracket-party energy
- board/calendar feel
- readable date headers
- high-contrast match rows
- no photorealistic player portraits
- no FIFA/brand logos unless already present in the base image and safe to preserve
- no cluttered tiny text

Keep the result useful as a site background. The game UI will sit on top of it.

## Required output before image generation

Before generating or updating the image, report:

- files inspected
- which file is schedule authority
- which file is team-occupant truth
- dates found
- number of matches per date
- which R32 matches have two known teams, one known team, or no known teams
- any mapping uncertainty

If any mapping uncertainty exists, state it and render uncertain rows as `TBD` rather than guessing.

## Required output after image generation

After generating the candidate image, provide a CB-ready patch plan:

- replace `site/assets/board/knockout_pub_background.jpeg`
- optionally add/update a source image under `source/images/`
- optionally add/update a manifest under `source/text/`
- add/update a capture under `captures/`
- add/update a card under `cards/`
- add/update a verifier under `tools/`
- run the targeted verifier
- run `make verify`
- run `make pack`

## CB rule

Only if I ask “CB this,” generate a download/apply overlay pattern.

The apply instructions must start with:

`cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li`

The CB must preserve the existing prompt and LI governance style. Do not silently overwrite unrelated image/data files.


Verifier keywords: one row for each match. Do not guess teams.
