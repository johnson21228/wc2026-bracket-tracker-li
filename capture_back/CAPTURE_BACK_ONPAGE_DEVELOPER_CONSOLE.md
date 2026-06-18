# Capture Back — On-page developer console

## Problem

A black site gives no useful runtime evidence.

## Change

Added `site/js/services/DebugConsole.js` and rewired `site/js/app.js` so developer output is visible on-page.

## Result

The page can now report:

- app startup
- board shell creation
- developer frame creation
- mount completion
- thrown errors
- unhandled promise rejections
