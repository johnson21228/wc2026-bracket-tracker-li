# Capture Back — Dynamic bootstrap debug console

## Problem

A debug console loaded as a static dependency cannot help if another static dependency fails before `app.js` executes.

## Change

`site/js/app.js` now mounts the developer console first, then dynamically imports:

- `site/js/services/assetPaths.js`
- `site/js/board/BoardShell.js`
- `site/js/dev/DeveloperFrame.js`

## Result

The page should show module import progress and any thrown error on-page.
