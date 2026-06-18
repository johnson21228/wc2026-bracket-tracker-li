# Card 207: Pick conflicts warn, not block

## Intent

Preserve source-scoped user picks even when the current bracket state detects a conflict.

## Change

- Add LI for the hard/soft pick boundary.
- Keep source-scoped menus.
- Stop treating duplicate R32 picks as import blockers.
- Stop clearing downstream picks during import solely because the current feeder state has changed.
- Rely on pick validity rendering to flag conflicts.

## Verification

`tools/verify_wc2026_pick_conflicts_warn_not_block.py`
