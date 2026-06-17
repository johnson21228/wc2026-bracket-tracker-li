# Capture Back: Canonical Knockout Assignment Render Repair

## Summary

Repairs the Game 1 knockout choice menu so a selected team is applied to the bracket cell that opened the menu and is rendered in that same cell.

## Problem

The page accumulated multiple wrappers for menu assignment, storage, and rendering. The anchored menu tile click path can bypass later wrapper-based assignment fixes.

## Decision

Make the anchored knockout choice menu own the canonical assignment path:

1. record the opening bracket cell as the assignment target
2. write the selected team to the round-specific store
3. render the chosen team into that same cell
4. close the menu

## Evidence

- `site/game1/index.html`
- `tools/verify_wc2026_canonical_assignment_render_repair_patch.py`
