# Card 086 — Repair R32 Pick Card Abbreviation Rendering

## Intent

Ensure the compact Round of 32 pick-card face actually uses the team's three-letter abbreviation.

## Problem

A prior LI rule declared abbreviation display, but the runtime surface could still render a full team name depending on which rendering path was active.

## Change

- Add a single helper for compact R32 pick-card display codes.
- Patch Game 1 filled-card rendering to call that helper.
- Keep full team names out of compact card HTML.
- Keep full team names available to tooltip/details surfaces.

## Acceptance

- The compact card face renders `abbr`/three-letter code.
- The compact card face does not render full team name fields.
- Verification checks all 48 team records have three-letter `abbr` values.
