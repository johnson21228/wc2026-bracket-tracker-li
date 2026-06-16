# Extract Game 1 Slot Menu to Data Modules

Use this prompt when continuing the Game 1 menu/data boundary work.

The goal is to keep Game 1 behavior intact while moving data authority out of `site/game1/index.html`.

Preserve this flow:

```text
pixel hit region
-> slotId
-> slot menu rule
-> eligible groups
-> eligible teams
-> menu render
-> persisted pick
```

Constraints:

- Do not reintroduce full duplicated `SLOT_RULES` or `GROUPS` arrays in the HTML.
- Keep direct local review working with `open site/game1/index.html`.
- Treat `site/data/game1_r32_slot_menu_rules.json` as the Game 1 R32 menu-rule source.
- Treat `site/data/teams_from_flags_images.json` as the team/flag source.
- Treat `site/assets/playfield/r32_game_board_hd.png` as the current Game 1/Game 2 shared board authority.
- Retain `site/assets/playfield/r32_bracket_game_board_template.png` as legacy compatibility unless all references are intentionally migrated.

After changes, run:

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li
make verify
python3 tools/verify_wc2026_game1_data_driven_menu_patch.py
make pack
open site/game1/index.html
```
