# Card 284: Player Standings Pick Viewer

## Goal
Let a joined player open another player's public, read-only bracket picks directly from the Player Standings panel.

## Scope
- Make each public player name in the Standings table a real button.
- Open a read-only picks viewer for that row.
- Render the selected player's `picksBySlot` grouped by round.
- Show `Unpicked` for empty pick slots.
- Keep the existing Join-first, read-only standings model.

## Non-goals
- No storage mutation.
- No save, insert, update, upsert, or delete path.
- No raw email, auth ID, or private account identifier display.

## Acceptance
- Player names in the Standings panel are visibly actionable.
- Selecting a player opens a keyboard-accessible, screen-reader reasonable read-only picks viewer.
- Picks are grouped as Round of 32, Round of 16, Quarterfinal, Semifinal, Final, and Champion / Third place.
- Empty slots display player-facing `Unpicked` text.
- The viewer can be closed clearly and focus returns to the player button.
- `make verify` and `make pack` pass.

## Verification
Run:

```bash
python3 tools/verify_wc2026_player_standings_pick_viewer.py
make verify
make pack
```
