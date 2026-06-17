# Verify Game 1 Pick State Authority

Read `li/world_cup/game1_pick_state_authority_rule.md` and inspect `site/index.html`.

Verify:

1. Short-term R16 hardcoded hold is disabled or removed.
2. Menu preselect/highlight is not based on stale stored downstream picks.
3. R16/QF/SF menu opening is source-gated.
4. Stored knockout rendering is source-gated before `renderOneR16Pick` or `renderOneAdvancementPick` is called.
5. Clear picks resets canonical and mirror stores.

Fail if downstream stored picks can be rendered solely because they exist in a legacy store.
