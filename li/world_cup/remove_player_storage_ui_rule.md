# Remove player-facing storage UI rule

Core rule: Bracketeering Pub players should not see storage/debug plumbing in the normal game UI.

The normal player surface must not render controls labeled or wired as:

- Capture Picks
- Export Picks
- Import Picks
- JSON import file controls

This rule does not require deleting internal storage helpers. Until remote persistence is fully stable, internal export/import serialization and localStorage helpers may remain available for migration, diagnostics, or developer-only affordances. They must not be visible as normal player controls.

Acceptance requires:

- no player-facing Capture/Export/Import controls in `site/index.html`
- no normal-player export/import file binding in `site/js/mvc/view.js`
- localStorage anonymous play remains intact
- canonical BracketDocument/save seam remains intact
- `make verify` and `make pack` pass
