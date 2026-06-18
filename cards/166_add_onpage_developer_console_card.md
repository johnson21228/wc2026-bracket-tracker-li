# Card 166 — Add on-page developer console

## Intent

Add a console-like developer output panel that remains visible even when the board fails to mount.

## Context

The site can currently fail as an all-black page when JavaScript startup throws before the board and developer frame render.

## Acceptance

- `site/js/app.js` installs global runtime error capture.
- The page shows a developer console panel.
- Startup steps are logged visibly.
- Runtime errors are displayed visibly.
- If board startup fails, the console still renders.
- No heredoc is required to apply this card.
