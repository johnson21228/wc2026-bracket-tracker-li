# R32 Pick Card Runtime Repair

This patch repairs the Game 1 page after the fixed-font-metrics pass introduced raw newline characters into JavaScript string literals for multi-word team names. That invalid JavaScript stopped the page runtime, causing picks to disappear.

## What went wrong

The intended behavior was visual: let team names use consistent metrics and wrap within the slot. The implementation attempted to encode preferred line breaks directly into JavaScript strings, but those strings contained literal newlines. In browser JavaScript, a normal quoted string cannot span physical lines, so the script failed to parse.

## Repair

The repair removes the fragile display-name break table and returns to valid team-name rendering. The card should rely on CSS wrapping and fixed metrics rather than generated raw newline strings.

## LI added

`li/world_cup/r32_pick_card_runtime_safety_rule.md` records that R32 pick-card typography changes are not allowed to break pick state, data loading, or card rendering.
