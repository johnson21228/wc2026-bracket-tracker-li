# Capture Back: Canonical Knockout Assignment Surface

## Summary

Replaced stacked knockout menu assignment wrappers with one canonical assignment surface.

## Contract

A knockout choice menu is an assignment surface for the bracket cell that opened it.

Selection must:

1. preserve the opening cell as the target,
2. write the selected team to round-specific storage,
3. render the same bracket cell,
4. close the menu, and
5. close competing tooltip surfaces.

## Evidence

- `site/game1/index.html`
- `tools/verify_wc2026_canonical_knockout_assignment_surface_patch.py`
