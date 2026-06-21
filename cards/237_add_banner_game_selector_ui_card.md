# Card 237: Add banner Game selector UI scaffold

## Goal

Add a visible developer-facing Game selector to the site banner/header.

## User story

As the developer, I want a visible Game 1 / Game 2 selector in the banner so the product can expose the eventual multi-game concept without implementing actual game switching yet.

## Implementation notes

- Add the selector near existing banner/header actions.
- Prefer simple HTML/CSS state over JavaScript.
- Default to Game 1.
- Allow the selected visible value to change to Game 2.
- Do not connect the control to board rendering, pick state, storage, scoring, Supabase, routing, or data loading.

## Verification

`python3 tools/verify_wc2026_banner_game_selector_ui.py`

The verifier checks:

- The banner includes `data-dev-game-selector`.
- The selector has Game 1 and Game 2 radio options.
- Game 1 is checked by default and Game 2 is not.
- CSS exists for the developer selector.
- The selector is not wired into JavaScript runtime modules.
- The verifier is registered in `make verify`.
