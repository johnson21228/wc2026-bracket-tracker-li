# Game 1 R32 Slot Menu Mapping

Game 1 now has durable data for deciding which group menu to show for every Round of 32 slot.

Data source:

- `site/data/game1_r32_slot_menu_rules.json`
- `site/data/groups_from_flags_images.json`

Runtime behavior:

1. The user taps a pixel-native R32 slot.
2. The slot rule is looked up.
3. The menu shows only the eligible group or group pool.
4. The menu renders team graphics using flag emoji, abbreviation, country name, and group.
5. The selected team is assigned to that slot and persisted in localStorage.

The menu decision belongs to the slot, not to the user's later choice.
