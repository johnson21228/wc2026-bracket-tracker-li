# Capture Back: Menu Selection Storage and Render Contract

## Summary

Captured the rule that a knockout choice menu selection must persist into the bracket cell that opened the menu and then re-render that cell.

## Decision

The knockout choice menu is an assignment surface, not just a chooser. A selection writes a normalized pick to the active bracket slot storage and immediately re-renders the bracket.

## Scope

- R16 winner picks use `r16Picks` and `saveR16Picks`.
- QF/SF/final advancement picks use `advancementPicks` and `saveAdvancementPicks`.
- The selected pick includes assignment metadata so the stored value can be traced back to the bracket cell.

## Evidence

- `site/game1/index.html`
- `tools/verify_wc2026_menu_selection_storage_render_patch.py`
