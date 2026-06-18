# Card 192 — Refine Group Button Rail Visual Emphasis and Anchored Panel

## Intent

Make the bottom group rail visually quieter at rest and make the shared group panel appear anchored to the group control that opened it.

## Changes

- Add LI for subtle translucent group tiles and fully opaque active tracking state.
- Add board-attached group panel placement over/above the launching group tile or group label.
- Clamp the panel inside the visible gameboard viewport when possible.
- Allow internal panel scrolling when content exceeds available board viewport height.
- Preserve shared group panel behavior and local checked-in data boundary.

## Out of scope

- Pick logic changes.
- Third-place source-slot semantics.
- Standings or match data changes.
- Runtime ESPN scraping.
