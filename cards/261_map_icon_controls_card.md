# Card 261: Add upper-left map icon controls

## Goal

Add compact map-style controls to the full-window board shell:

- `+` zoom in
- `−` zoom out
- `i` get info

## Acceptance

- The controls are small, round, icon-style buttons fixed in the upper-left browser window.
- The `+` and `−` buttons use the existing View-owned board zoom behavior.
- The `i` button opens the existing Rules panel as temporary info behavior.
- The previous floating action/status controls remain hidden.
- The existing login control remains in the upper-right browser window.
- `make verify` includes `tools/verify_wc2026_map_icon_controls.py`.\n## Refinement\n\n- `i` sits to the right of `+`.\n- `−` sits below the `+` column.\n- Button zoom is board zoom around the visible viewport center, not page zoom.\n
## Player-facing zoom refinement

- Hide `.board-zoom-controls` explicitly.
- Keep `+` and `−` as the only visible zoom controls.
- Keep the legacy zoom select only as internal runtime plumbing if the View still needs it.
## Zoom button activation repair

- Remove brittle direct `boardZoomInButton` / `boardZoomOutButton` refs.
- Delegate icon zoom clicks from the View root.
- Step the hidden internal `[data-board-zoom]` select and dispatch `change` so the existing zoom runtime performs the board zoom.
