# Card 171 — Pick identifier developer overlay

## Intent

Add a developer overlay that shows the pick identifier inside each pick slot.

## Purpose

This is a diagnostic layer for mapping visual slots to model identifiers. It helps confirm that every visible pick location corresponds to a stable identifier from the geometry manifest.

## Acceptance

- The overlay reads `data/geometry/gameboard_manifest.json`.
- Each slot rectangle gets an identifier label inside the pick.
- The developer frame has a `Show pick identifiers` toggle.
- The copyable developer properties include `showPickIdentifiers`.
- The overlay is developer-only and does not change player pick state.
- `make verify` and `make pack` pass.
