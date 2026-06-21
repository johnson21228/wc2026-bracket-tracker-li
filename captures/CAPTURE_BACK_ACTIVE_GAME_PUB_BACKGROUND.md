# Capture Back: Active Game Pub Background

## Intent

The developer Game selector now drives the visible pub background image as presentation-only UI.

## Runtime source assets

- Game 1: `site/assets/board/pub_background_game1.jpeg`
- Game 2: `site/assets/board/knockout_pub_background.jpeg`

Published Pages paths:

- `assets/board/pub_background_game1.jpeg`
- `assets/board/knockout_pub_background.jpeg`

## Behavior

- Game 1 remains selected by default.
- Game 1 uses `assets/board/pub_background_game1.jpeg`.
- Game 2 uses `assets/board/knockout_pub_background.jpeg`.
- Switching the developer Game selector updates the board background immediately.
- The Rules panel continues to follow the active selected game.

## Boundary

This is not gameplay switching. It does not change pick state, scoring, storage,
Supabase/Auth behavior, routes, group data, knockout data, or board geometry.
