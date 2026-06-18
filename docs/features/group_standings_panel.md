# Group Standings Panel

The group standings panel is a planned single-site feature for the clean MVC runtime.

It will give each group-derived pick menu a way to show the current group context: standings, match scores, match status, kickoff times, and optional highlight links.

The panel is governed by `li/world_cup/group_standings_panel_rule.md`.

## Initial implementation target

The first implementation should use checked-in JSON data under `site/data/current/`.

Suggested files:

```text
site/data/current/group_standings.json
site/data/current/group_matches.json
site/data/current/match_highlights.json
```

The runtime should not scrape ESPN or YouTube from the browser. WB/CB updates may refresh the normalized data as games are played.

## MVC shape

- Model: loads current group data and derives rank context.
- View: renders the panel.
- Controller: opens/closes the panel from pick menus or group context actions.

## Third-place note

Third-place R32 slot labels must be source-group labels such as `3RD A/E/H/I/J`, not rank-position labels like “third-place position 1.”
