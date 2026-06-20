# Card 234: Remove player-facing Capture/Export/Import UI

## Intent
Players should see gameplay controls, not storage/debug plumbing.

## Change
Remove the visible player-facing controls for:

- Capture Picks
- Export Picks
- Import Picks
- JSON import file input controls

## Preservation
Keep runtime state behavior intact:

- localStorage play continues.
- Canonical BracketDocument/save seam remains.
- Internal export/import helpers may remain for migration, diagnostics, or future developer-only affordances, provided they are not visible in normal player UI.

## Acceptance

- No player-facing Capture Picks, Export Picks, Import Picks, or import file controls render from `site/index.html`.
- `site/js/mvc/view.js` does not bind normal-player export/import controls.
- Existing pick behavior remains unchanged.
- localStorage save/restore remains available.
- `make verify` passes.
- `make pack` passes.
