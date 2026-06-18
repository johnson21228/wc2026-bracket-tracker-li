# Card 184: Add group standings model data

## Purpose

Add normalized checked-in model data for the group standings panel so the clean MVC site can load current group standings without scraping ESPN from the browser runtime.

## Boundary

This card adds model data support only. It does not render the group standings panel UI yet.

## Source posture

The first seed is a manually checked standings snapshot from ESPN's FIFA World Cup standings page and match-result evidence available at capture time.

The site runtime consumes local JSON under `site/data/current/`.

## Files

- `site/data/current/group_standings.json`
- `site/data/current/group_matches.json`
- `site/data/current/match_highlights.json`
- `site/data/current/README.md`
- `tools/verify_wc2026_group_standings_model_data.py`

## MVC acceptance criteria

- `site/js/mvc/model.js` loads the current group data.
- Model exposes group standings, group match list, highlight data, group context, and third-place table context.
- View and Controller do not hardcode standings values.
- Browser runtime does not scrape ESPN.
- A later CB can replace the JSON snapshot and rerun verify/pack.
