# Capture Back: Map Icon Controls

## Intent

Add minimal upper-left browser chrome for the full-window board shell:

- zoom in
- zoom out
- get info

## Decision

Use three small round icon buttons pinned to the upper-left browser window. The info button uses the existing Rules panel for now.

## Runtime boundary

Zoom remains View-owned and uses the same board zoom pipeline as wheel/pinch/select zoom. No pick model, controller, or Supabase persistence behavior changes.

## Verification

`tools/verify_wc2026_map_icon_controls.py` checks the DOM hooks, CSS placement, View-owned zoom wiring, LI artifacts, and Makefile integration.\n## Refinement\n\nThe info control is positioned immediately to the right of the `+` zoom button. The `+` and `−` controls zoom the board around the current browser viewport center, matching map-style button zoom behavior.\n
## Player-facing zoom refinement

Only the fixed upper-left `+` and `−` map icon buttons are player-facing zoom controls. The legacy zoom select is hidden and retained only as internal runtime scale plumbing.
## Zoom button activation repair

The `+` and `−` map icon buttons now step the hidden internal board zoom select and dispatch its `change` event. This reuses the existing board zoom runtime while keeping the legacy zoom dropdown hidden from players.
