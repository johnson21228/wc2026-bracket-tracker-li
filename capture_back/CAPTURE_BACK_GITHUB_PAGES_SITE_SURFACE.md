# Capture Back — GitHub Pages Site Surface

## Reason

The repo had loose root HTML files that made it unclear which page was live and which page should be deployed. The user identified `index.html` as stale and asked for a deployable site folder with dependencies inside it so the project can be quickly deployed on GitHub Pages.

## Decision

Create an explicit `site/` product surface:

- `site/index.html`
- `site/game1/index.html`
- `site/game2/index.html`
- `site/assets/`
- `site/data/`

Root HTML files are removed from the deploy posture.

## Outcome

Future UI work should target `site/` first. Workbench source, LI, prompts, cards, and capture-back material remain outside the public site folder.
