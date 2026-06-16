# Card 078 — Extract Game 1 Slot Menu Data

## Intent

Move Game 1 R32 chooser/menu data out of embedded HTML and into module-owned data loading.

## Change

- Add `li/world_cup/game1_data_driven_slot_menu_rule.md`.
- Add `docs/features/game1_data_driven_slot_menu.md`.
- Add `prompts/extract_game1_slot_menu_to_data_modules.md`.
- Generate `site/data/game1_data_bundle.js` from existing JSON data.
- Update `site/game1/index.html` to load the bundle and bind data from `window.WC2026_GAME1_DATA`.
- Add `tools/verify_wc2026_game1_data_driven_menu_patch.py`.

## Acceptance

- `make verify` passes.
- `python3 tools/verify_wc2026_game1_data_driven_menu_patch.py` passes.
- `open site/game1/index.html` still allows local visual review.
- Game 1 menu behavior remains: each R32 slot shows only eligible groups/teams.
