# Card 232: Make Pages publish fail-closed and live-data verified

## Problem

Pages publish reported success while the live GitHub Pages URL still served stale `data/current/group_matches.json`.

## Decision

`main` is the source of truth. `gh-pages` is generated output. Publish is only complete after the live deployed critical JSON matches the committed `site/` source JSON.

## Acceptance

- `make publish-pages` is strict and live-data verified.
- `make check-pages` detects stale deployed data.
- `make publish-pages-force` can force a redeploy and still fail closed.
- Critical JSON files are compared by canonical JSON hash.
- June 19 result canary rows are checked.
- `make verify` and `make pack` continue to pass.
