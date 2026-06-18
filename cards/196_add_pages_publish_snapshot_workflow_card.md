# Card 196 — Add Pages publish snapshot workflow

## Intent

Make GitHub Pages publishing an explicit Workbench projection rather than allowing Pages hosting shape to drive the WB source layout.

## Decision

- `site/` remains the deployable app source truth.
- `gh-pages` becomes generated deployment output.
- `make publish-pages` copies `site/` contents to `gh-pages` root and pushes the snapshot.
- The workflow is documented and verified.

## Acceptance

- `make verify` includes the Pages publish snapshot verifier.
- `make publish-pages` exists.
- The publish script copies `site/` contents to `gh-pages` root.
- LI states that `gh-pages` must not be hand-edited.
