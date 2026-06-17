# Card 123: Menu Selection Storage and Render

## Claim

A knockout choice menu selection must persist a pick into the bracket cell that opened the menu and re-render that cell.

## Acceptance Criteria

- The menu records or resolves the active assignment slot.
- Selecting an R16 team writes to `r16Picks[slotId]`.
- Selecting a QF/SF/final team writes to `advancementPicks[slotId]`.
- The stored pick records `assignedSlotId`.
- The page calls `renderPicks()` after saving.
- The menu closes after successful assignment.
- A verifier protects these implementation markers.

## Governed Files

- `site/game1/index.html`
- `li/world_cup/menu_selection_storage_render_rule.md`
- `tools/verify_wc2026_menu_selection_storage_render_patch.py`
