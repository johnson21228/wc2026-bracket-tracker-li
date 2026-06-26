# Official truth bracket as hidden player

The current Supabase design stores the Official Results / truth source as a hidden player-style bracket row:

- `bracket_kind = official`
- editable by the official results admin account through the normal game board
- readable by signed-in users as truth data
- excluded from normal player standings and player panels
- compared against user picks only where official picks exist

Invariants:

1. `bracket_kind = official` must not appear in the Players panel.
2. `bracket_kind = player` remains the only normal standings/player-list row kind.
3. The official bracket is loaded separately from player standings.
4. The board may compare a user pick to official truth only when official truth exists for that slot.
5. Incorrect user picks may render beside the official pick.
6. There is no green official-results banner. The admin editor must not render an “Editing Official Results” rail, banner, or blocking status surface.
7. The game board remains the truth editor for the official/admin account; no separate admin console is required for this stage.
