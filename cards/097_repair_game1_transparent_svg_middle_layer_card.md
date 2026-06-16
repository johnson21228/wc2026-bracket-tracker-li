# Card 097 — Repair Game 1 Transparent SVG Middle Layer

## Intent

Repair the first Game 1 uniform SVG board switch so the SVG acts as transparent middle-layer linework and geometry truth, while Game 1 R32 hit targets and pick cards use the SVG-derived manifest.

## Capture

The first visible migration showed the proof SVG as an opaque board surface with checker/proof title and old pick-card coordinates. The desired gameboard architecture is layered: background image underneath, transparent SVG linework in the middle, and manifest-driven interaction/pick cards above.

## Acceptance

- SVG has no checker/proof background.
- SVG has no visible proof title.
- SVG slot outlines are transparent fills with strokes only.
- Game 1 bottom background remains visible underneath.
- Game 1 R32 hit regions use the uniform SVG manifest bounds.
- Game 1 R32 pick cards use the uniform SVG manifest bounds.
- Game 2 remains unmigrated.
