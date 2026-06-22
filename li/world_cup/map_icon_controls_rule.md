# WC2026 Map Icon Controls Rule

The board-first Bracketeering Hub shell may expose only minimal browser-pinned map controls while the main board remains the primary surface.

Required controls:

- `+` zooms the board in through the existing View-owned zoom pipeline.
- `−` zooms the board out through the existing View-owned zoom pipeline.
- `i` opens the existing Rules panel as the temporary Get Info behavior.

The controls must be small, round, icon-like, and fixed in the upper-left browser window. They must not restore the previous floating banner actions or status panel.

The existing Supabase login surface remains the only upper-right chrome.\n## Layout refinement\n\nThe compact map controls use a small grid: `+` at upper-left, `i` immediately to its right, and `−` below the `+`. Zoom buttons must call View-owned board zoom around the visible viewport center, matching Google-Maps-style button zoom rather than browser/page zoom.\n
## Player-facing zoom refinement

The only player-facing zoom controls are the fixed round `+` and `−` map buttons. Any legacy zoom select/dropdown must remain hidden and may only serve internal runtime plumbing.
## Zoom button activation repair

The visible `+` and `−` map buttons must drive board zoom through the existing internal board zoom pipeline. The hidden legacy zoom select may remain as runtime plumbing, but the player-facing zoom surface is only the two round map buttons.
