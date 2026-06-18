# Capture Back: Group Standings Model Data

## Captured decision

Add normalized current group standings data under `site/data/current/` and load it through the clean MVC model.

## Runtime boundary

The browser runtime must not scrape ESPN. A Workbench CB can update the checked-in JSON snapshot later, using ESPN or another verified public source as input.

## Files added or changed

- Added `site/data/current/group_standings.json`
- Added `site/data/current/group_matches.json`
- Added `site/data/current/match_highlights.json`
- Added `site/data/current/README.md`
- Updated `site/js/mvc/model.js`
- Added `tools/verify_wc2026_group_standings_model_data.py`
- Updated `Makefile` verify target

## Next implementation step

Render the group standings panel in the View and add Controller actions to open it from group-derived pick menu context.
