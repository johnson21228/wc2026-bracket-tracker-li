# Pages Publish Fail-Closed Rule

main is the source of truth for the Bracketeering Pub site. The GitHub Pages branch is generated deployment output.

A Pages publish must be fail-closed: it may not report success merely because `gh-pages` was committed or pushed. It must project the committed `site/` tree from `main` into `gh-pages`, push the generated branch, and then prove that the live deployed JSON matches the source data.

Critical live deployed JSON:

- `data/current/group_matches.json`
- `data/current/group_standings.json`
- `data/current/match_highlights.json`

Required commands:

- `make publish-pages` performs a strict publish and verifies live data before success.
- `make check-pages` independently verifies live data freshness against local `site/data/current` source files.
- `make publish-pages-force` creates an empty `gh-pages` commit when needed to force a redeploy, then still verifies live data before success.

The publish command must fail nonzero if live deployed JSON is stale, mismatched, unreachable, or missing expected canary rows.
