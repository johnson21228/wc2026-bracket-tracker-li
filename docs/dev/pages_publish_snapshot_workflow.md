# GitHub Pages Publish Snapshot Workflow

The WC2026 Workbench keeps the app source of truth in `site/`.

GitHub Pages expects the public branch root to contain the deployed web surface, so the repo publishes a generated snapshot to `gh-pages` root.

## Command

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li

make verify
make pack
make publish-pages
```

## Source truth

Edit and review the app in:

- `site/index.html`
- `site/css/`
- `site/js/`
- `site/data/`
- `site/assets/`

## Published snapshot

`make publish-pages` projects the current `site/` contents into `gh-pages` root:

- `index.html`
- `css/`
- `js/`
- `data/`
- `assets/`
- `.nojekyll`
- `pages-build.txt`

`gh-pages` is generated output. Do not hand-edit it.

## Public URL

```text
https://johnson21228.github.io/wc2026-bracket-tracker-li/
```

Use cache-busting while testing immediately after publish:

```bash
URL="https://johnson21228.github.io/wc2026-bracket-tracker-li/"
STAMP="$(date +%s)"

curl -I "${URL}?v=${STAMP}"
curl -I "${URL}css/board.css?v=${STAMP}"
curl -I "${URL}js/app.js?v=${STAMP}"
curl -I "${URL}data/current/group_matches.json?v=${STAMP}"
```
