# Player Standings board viewer

The Player Standings board viewer lets a joined player inspect another public player's picks as a large read-only board presentation.

## Flow
1. Open Standings.
2. Select `View picks` on a player row.
3. A large panel opens with `Viewing <player>'s picks` and `Read-only` copy.
4. The selected player's public `picksBySlot` values render onto board-shaped pick cells.
5. The viewer can be panned/zoomed independently.
6. `Back to my board` closes the viewer and returns focus to the player action.

## Safety
The viewer is presentation-only. It does not call save paths, does not write to browser storage, and does not send changes to Supabase. It also avoids raw private identity fields in the UI.
