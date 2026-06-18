# Current Data Snapshots

This folder contains normalized checked-in data used by the clean MVC site runtime.

The browser must not scrape ESPN, FIFA, YouTube, or other third-party sites at runtime. A Workbench CB may update these snapshots when standings, results, match status, or highlight links change.

## Files

- `group_standings.json` — current group tables and derived third-place table.
- `group_matches.json` — group-stage match schedule/result evidence.
- `match_highlights.json` — optional highlight URLs, empty until verified.
