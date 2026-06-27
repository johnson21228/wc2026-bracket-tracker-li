# Rule: Player Standings Has No Pick Links

Player Standings must not expose a link or button to open another player's picks or board.

Rules:
- Public player names may be shown as standings text.
- Rows must not render `View picks`, `Open picks`, `View bracket`, or equivalent pick-inspection actions.
- The standings store may still read public rows for scoring/leaderboard presentation.
- No save/write path may be introduced from standings.
