# UPDATE KNOCKOUT PUB BACKGROUND IMAGE Workflow

This workflow captures a reusable prompt for regenerating the Bracketeering Pub knockout background image from current site truth.

Runtime target:

- `site/assets/board/knockout_pub_background.jpeg`

Base/reference image:

- `site/assets/board/knockout_pub_background.jpeg`

Authoritative data inputs:

- `site/data/current/knockout_matches.json` for dates, matches, rounds, times, venues, and bracket edges.
- `site/data/current/official_truth.json` for known official R32 occupants.

The image is a generated projection. It must not become the schedule authority.

The generated board should group by date, put the date at the top of each day section, and use one row per match. Known match rows should use `Flag vs Flag`; unresolved rows should say `TBD`.

Flags should be as tall as they can be while still fitting nicely in each row. Long team names and feeder codes should not be printed in the image rows unless a later prompt explicitly asks for them.
