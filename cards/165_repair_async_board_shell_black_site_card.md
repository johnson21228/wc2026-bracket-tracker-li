# Card 165 — Repair async BoardShell black site

## Intent

Repair the all-black site caused by async board construction being called synchronously.

## Pack evidence

Pack 17 showed:

- `site/js/board/BoardShell.js` exports `async function createBoardShell(...)`.
- `site/js/app.js` called `const boardShell = createBoardShell(...)` without `await`.
- The next line called `boardShell.querySelector(...)`, which fails because `boardShell` is a Promise.
- The mount aborts, leaving only the black page background.

## Acceptance

- `site/js/app.js` awaits `createBoardShell`.
- Startup errors render a visible failure message instead of silent black.
- Developer frame exposes gameboard outline controls.
- `make verify` and `make pack` pass.
