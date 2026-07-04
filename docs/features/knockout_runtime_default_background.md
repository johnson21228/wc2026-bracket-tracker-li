# Knockout Runtime Default Background

The Bracketeering Hub runtime now boots with the active pub background used by the single-game runtime:

- `site/assets/board/pub_background_game1.jpeg`

This is a presentation-only default. It does not change gameplay logic, picks, scoring, standings, Supabase storage, or the board geometry.

The older `knockout_pub_background.jpeg` asset may remain in the repo as a historical/source asset, but it must not be the default image used by the single-game runtime boot path.

Runtime/default references that must point to the knockout asset:

- `site/js/services/assetPaths.js`
- `site/js/mvc/view.js`
- `site/index.html`
- the legacy `ACTIVE_GAME_BACKGROUND_IMAGES` aliases in `site/js/app.js`

Both legacy aliases point at the same active pub image so no lifecycle/presentation path can silently fall back to a stale background.
