# Rule — Player Standings board viewer is read-only presentation

When a standings row opens another player's picks, the app must treat that viewed board as temporary read-only presentation state.

The viewed player's `picksBySlot` may be projected into board-shaped cells for inspection, but it must not become the active user's bracket document. The viewer must not write to localStorage, Supabase, or the active pick controller/save pipeline.

The UI must clearly identify the viewed public player and provide a close/back path to the user's own board.
