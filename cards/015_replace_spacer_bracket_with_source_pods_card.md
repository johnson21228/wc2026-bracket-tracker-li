# Card 015 — Replace Spacer Bracket With Source Pods

## Intent

Replace the current spacer-based bracket layout with a source-adjacent pod layout.

## Why

The vertical alignment remains hard to tune with global CSS spacing. The better model is to place each result directly adjacent to the source matches that feed it.

## Acceptance

- R32 source pairs and their R16 result are in the same local pod.
- R16 pods compose into QF pods.
- QF pods compose into SF pods.
- Final is composed from semifinal pods.
- Drag/drop behavior still works.
- Export/import JSON still works.
- Slot labels/tooltips remain available.
- Screenshot readability improves.
