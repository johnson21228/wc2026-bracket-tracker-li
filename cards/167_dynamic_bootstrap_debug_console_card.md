# Card 167 — Dynamic bootstrap debug console

## Intent

Make the on-page developer console survive failures in board modules.

## Evidence

Card 166 was applied and `DebugConsole.js` served with HTTP 200, but a blank/black site can still happen if a static import in `site/js/app.js` fails before the console is mounted.

## Repair

`site/js/app.js` statically imports only the debug console and mount helper. Board modules are dynamically imported after the console is mounted.

## Acceptance

- The developer console appears before board module imports.
- Dynamic import failures are shown on-page.
- Board shell creation failures are shown on-page.
- `make verify` and `make pack` pass.
