# Player Standings Pick Viewer

The Player Standings panel is a public comparison surface for joined players. A player name in the standings table is an interactive button that opens a read-only view of that player's bracket picks.

The viewer renders from the standings row's `picksBySlot` object. It groups slots by round where possible: Round of 32, Round of 16, Quarterfinal, Semifinal, Final, and Champion / Third place. Empty slots use the player-facing label `Unpicked`.

The surface must remain read-only. It may read public standings rows and public display names, but it must not insert, update, upsert, delete, save, or otherwise mutate bracket storage. It must not display raw email addresses, raw auth IDs, or private account identifiers.

Accessibility requirements:
- Player names are real `button` controls.
- The picks viewer has a labeled region.
- The viewer has a clear close button.
- Keyboard focus is visible and returned to the originating player button when the viewer closes.
