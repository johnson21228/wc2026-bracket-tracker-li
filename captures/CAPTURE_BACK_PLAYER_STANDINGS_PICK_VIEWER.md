# Capture Back: Player Standings Pick Viewer

## Change
The Player Standings panel now treats each public player name as an actionable button. Selecting the button opens a read-only picks viewer for that player's bracket.

## Behavior
- The viewer renders from the selected standings row's `picksBySlot`.
- Picks are grouped by tournament round when possible:
  - Round of 32
  - Round of 16
  - Quarterfinal
  - Semifinal
  - Final
  - Champion / Third place
- Empty slots render as `Unpicked`.
- The panel includes an explicit close button.
- The name button and viewer use native controls, focus handling, labels, and visible focus styling.

## Privacy and write boundary
- The standings table and picks viewer use only the public player name from the standings row.
- Supabase profile reads remain limited to `id, display_name` for joining public names.
- The bracket rows read `bracket_json` and do not expose email or private account identifiers in the UI.
- No insert, update, upsert, delete, save, or write path is introduced.
- The Join-first player model and read-only standings behavior are preserved.

## Verification
Protected by `tools/verify_wc2026_player_standings_pick_viewer.py` and the existing storage-backed standings verifier.
