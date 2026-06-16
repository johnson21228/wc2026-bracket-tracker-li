# Card 056 — Capture Open Apps After Apply Rule

## Intent

Make the running app surfaces part of every Apply review loop.

## Captured rule

Any Capture Back overlay that changes this repository's app runtime, game data, assets, or behavior must open the site app surfaces after applying:

- `site/index.html`
- `site/game1/index.html`
- `site/game2/index.html`

## Rationale

Game behavior regressions can survive static verification. The browser surface must remain visible evidence in the WB loop.

## Files

- `li/repo/open_apps_after_apply_rule.md`
- `docs/workflows/open_apps_after_apply.md`
- `prompts/apply_overlay_terminal_workflow.md`
