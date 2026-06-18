# Capture Back — Pick identifier developer overlay

## Problem

The gameboard needs an inspectable mapping from visual pick slots to the identifier used by the data/model layer.

## Change

Added `site/js/board/PickIdentifierLayer.js`.

The layer reads the geometry manifest and renders a label inside each pick slot.

## Boundary

This layer is diagnostic. It does not mutate the geometry manifest, source SVG, or player pick state.
