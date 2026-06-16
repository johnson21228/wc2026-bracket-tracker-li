# Game 1 R32 Slot Menu Mapping Rule

Game 1 must know what menu to show for each Round of 32 bracket position before opening the tap menu.

Each R32 slot maps to a qualification rule, such as winner of a group, runner-up of a group, or a best third-place pool. The menu for that slot is filtered from the group/flag/country data according to the slot rule.

The rule is pixel-native: the slot's logical item, hit target, rendered pick card, and menu rule all resolve to the same source board pixel region.

Winner and runner-up slots show the four teams from one group. Third-place slots show the teams from the allowed group pool.

This rule restores the behavior where tapping a bracket position opens the appropriate group-based chooser rather than a global unfiltered team list.
