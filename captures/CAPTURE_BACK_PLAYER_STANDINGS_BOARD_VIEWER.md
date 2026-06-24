# Capture Back — Player Standings board viewer

## Request
Add a full read-only gameboard panel from Standings after the simple list viewer proved the public player-picks data path.

## Captured outcome
- Standings player names/actions now open a full-board-style read-only viewer panel.
- The panel uses the selected public row `picksBySlot` as its only pick source.
- The panel renders board linework plus positioned pick cells using the board geometry manifest.
- The panel has read-only copy, zoom controls, drag-pan support, and a `Back to my board` close action.
- The viewer does not write to localStorage or Supabase and does not replace the active bracket document.

## Verification
- `tools/verify_wc2026_player_standings_board_viewer.py`
- `make verify`
- `make pack`
