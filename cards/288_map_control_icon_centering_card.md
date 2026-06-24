# Card 288: Map Control Icon Centering

## Goal
Make the player-facing map controls look centered by replacing font-dependent `+`, `−`, and italic `i` text with explicit geometric icons.

## Acceptance
- Zoom-in, zoom-out, and info controls preserve their existing runtime data attributes and `aria-label` values.
- Each button contains a `span.map-icon-glyph` with `aria-hidden="true"`.
- Plus/minus/info visible marks are CSS-drawn geometry, not button text.
- The info icon is a centered dot and stem, not an italic font glyph.
- The change is View/CSS-only and does not alter pick, zoom, panel, or storage behavior.

## Verification
Run:

```bash
python3 tools/verify_wc2026_map_control_icon_centering.py
```
