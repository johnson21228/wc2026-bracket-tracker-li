# Capture Back — Async BoardShell black site repair

## Problem

The site was all black after the gameboard outline work.

## Cause

The board shell became async when it began fetching/parsing the SVG gameboard, but `site/js/app.js` still treated it as synchronous.

## Repair

- Make `startApp` async.
- Await `createBoardShell`.
- Catch startup failures and render a visible error message.
- Restore gameboard developer controls.
