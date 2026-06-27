# Capture Back: Knockout Runtime Default Background

## Change

The site runtime now uses the generated knockout pub calendar image as the default board background.

Runtime asset:

- `site/assets/board/knockout_pub_background.jpeg`

Source/reference copy:

- `source/images/wc2026_knockout_pub_calendar_background.jpeg`

## Why

The Bracketeering Hub has moved into a knockout-only single-game runtime. The site should no longer boot with the old group-stage pub image behind the game board.

## Scope

Presentation-only:

- default background path
- preload path
- legacy active-game background aliases
- verifier coverage

Out of scope:

- gameplay logic
- picks
- scoring
- standings
- Supabase persistence
- official truth data
- pick menus
