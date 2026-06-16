# Card 045 — Fix Game 1 duplicate JS state declarations

## Intent
Restore Game 1 hit target runtime by removing stale duplicate `const STORAGE_KEY`, `state`, and `activeSlot` declarations.

## Why
The page had two `const STORAGE_KEY` declarations in the same script scope. Browsers reject the script at parse time, so no hotspots are created.

## Acceptance
- `site/game1/index.html` has exactly one `const STORAGE_KEY` declaration.
- Browser console logs `game1_reset_visible_hit_layer 32`.
- Browser console logs `game1_duplicate_js_state_fix ok`.
- 32 opaque hotspot buttons are visible and clickable.
