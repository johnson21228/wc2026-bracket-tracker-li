# Fail-Closed Pages Publish With Live Data Verification

The Pages publish workflow is source-projection, not hand editing. `main` owns the site source under `site/`; `gh-pages` is generated deployment output.

Use:

```bash
make publish-pages
```

This command refuses dirty source, runs `make verify`, confirms the current `main` commit is pushed to `origin/main`, projects `site/` into a fresh `gh-pages` worktree, writes `pages-build.txt`, commits and pushes `gh-pages`, then polls the live GitHub Pages JSON with a cache-busting query string.

Use:

```bash
make check-pages
```

This independently compares live deployed JSON against local source JSON:

- `site/data/current/group_matches.json`
- `site/data/current/group_standings.json`
- `site/data/current/match_highlights.json`

Use:

```bash
make publish-pages-force
```

This forces a redeploy with an empty `gh-pages` commit when the generated tree is otherwise identical. It still verifies live deployed data before reporting success.

The command may not print “Pages publish complete” unless live JSON matches source JSON. If GitHub Pages is still serving stale data, the command retries and then fails nonzero.
