# Card 285 — Player Standings board viewer

## Intent
Upgrade the first Player Standings pick viewer from a small read-only list into a large read-only gameboard viewer.

## Behavior
- Player Standings rows expose a visible `View picks` action.
- The action opens a large board viewer panel.
- The panel says whose picks are being viewed and marks the view as read-only.
- The selected row's public `picksBySlot` is rendered onto board-shaped pick slots.
- The viewer has local pan/zoom controls and a `Back to my board` close action.

## Guardrails
- Viewer state is presentation-only.
- The active user's bracket document is not replaced.
- No localStorage or Supabase write path is used by the viewer.
- Pick cells in the viewer are disabled/read-only.
- Private identity fields are not displayed.

## Verification
`tools/verify_wc2026_player_standings_board_viewer.py`
