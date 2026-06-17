# Game 1 lifecycle status surface rule

The Game 1 board must expose its current lifecycle phase on the board surface.

Requirements:

- The lifecycle display is player-facing, not only developer-facing.
- It must read from the lifecycle model/seed data.
- It must fail soft when lifecycle data is unavailable.
- It must not mutate picks, standings, official lock data, or user storage.
- It should reinforce the Game 1 promise: pick before lock, watch groups reshape the board, compare the read later.
