# Capture Back — Pages Publish Snapshot Workflow

## Captured change

Added an explicit GitHub Pages publish workflow that projects the Workbench-owned `site/` app surface into the Pages-owned `gh-pages` branch shape.

## Governance

- `site/` is the source truth.
- `gh-pages` is a generated published snapshot.
- Do not hand-edit `gh-pages`.
- Re-publish from `site/` using `make publish-pages`.

## Operator command

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li

make verify
make pack
make publish-pages
```
