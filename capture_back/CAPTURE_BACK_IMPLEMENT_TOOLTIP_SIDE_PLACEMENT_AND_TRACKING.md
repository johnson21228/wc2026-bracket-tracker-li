# Capture Back: Implement Tooltip Side Placement and Tracking

## Summary

Implemented a side-placement tooltip layer for Game 1 so explanatory tooltip content does not cover the underlying pick.

## Decision

The Game 1 page now has a governed tooltip layer that:

- places tooltip content beside the target where possible
- avoids using the tooltip as an occluding layer
- preserves pointer tracking between the target and tooltip
- supports clickable tooltip actions through `data-tooltip-action-href`

## Boundary

This implementation is a UI behavior patch. It does not change bracket choice resolution, lifecycle state, or scoring.

## Evidence

- `site/game1/index.html`
- `tools/verify_wc2026_tooltip_side_placement_patch.py`
