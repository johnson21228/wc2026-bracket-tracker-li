WB_SESSION:
Repair Game 1 Hit Testing

Problem:
- The game board rendered, but tapping/clicking did not open the chooser.
- Likely causes:
  - stale release page was opened instead of canonical page
  - patched HTML drifted and hotspot script no longer executed
  - visual board layer sat above the hotspots
  - multiple generated pages created ambiguity

Decision:
- Canonical active review page is `game1_playfield.html`.
- Release pages are snapshots only.

Changed:
- Rebuilt `game1_playfield.html` cleanly.
- Created 32 R32 hotspots explicitly at runtime.
- Set board image `pointer-events: none`.
- Set hotspot `z-index: 10`.
- Set modal `z-index: 1000`.
- Added visible status: `32 hotspots active`.
- Preserved pixelated runtime flag background, USA default, first-pick adoption, modal chooser, delete, export/import.
- Created release:
  `releases/world_cup_game_board_v007_repaired_hit_testing.html`

Review:
- Open `game1_playfield.html`.
- Confirm status says `32 hotspots active`.
- Click an R32 slot.
- Chooser should open.
