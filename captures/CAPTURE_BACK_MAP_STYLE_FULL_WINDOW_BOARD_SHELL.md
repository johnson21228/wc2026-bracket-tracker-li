# Capture Back: Map-style full-window board shell

## Intent
Convert the Bracketeering Hub page chrome from a document-style page into a map-style board surface.

## Change
- Preserve existing HTML runtime hooks.
- Keep board scroll/pan/zoom behavior View-owned.
- Make the board scroll surface fill the viewport.
- Hide hero/banner text from the player-facing surface.
- Restyle existing controls as overlay chrome.
- Keep rules and status as overlays.

## Non-goals
No changes to pick model, controller behavior, slot geometry, SVG source truth, manifests, scoring/rules data, lifecycle semantics, or storage/Supabase seams.

## Verification
`tools/verify_wc2026_map_style_full_window_board_shell.py` verifies the shell rule and required hooks.
