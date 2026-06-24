# Capture Back: Map Control Icon Centering

## Intent
Replace font-rendered `+`, `−`, and italic `i` map controls with explicit geometric icon glyphs so the visible marks are optically centered inside the circular browser chrome.

## Change
- Map control buttons keep their existing button hooks and accessible labels.
- Visible control marks move into `aria-hidden` glyph spans.
- Plus and minus marks are drawn with CSS bars.
- Info is drawn as a centered dot and stem, not an italic serif text glyph.

## Boundary
This is a View/CSS-only polish change. It does not change board zoom behavior, info-panel behavior, control placement, z-index policy, or Supabase/gameplay state.

## Verification
`tools/verify_wc2026_map_control_icon_centering.py` checks the markup, CSS icon geometry, Makefile integration, and this capture/card pair.
