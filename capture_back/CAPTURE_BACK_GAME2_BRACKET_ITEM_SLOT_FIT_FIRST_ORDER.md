# Capture Back — Game 2 Bracket Item Slot Fit First-Order Card

## Summary
Captured a first-order Game 2 implementation card and LI rule stating that Game 2 bracket items must be rendered into image-defined bracket slots, not placed as a loose or approximate list.

## Added

- `cards/056_fit_game2_bracket_items_to_image_defined_slots_card.md`
- `li/world_cup/game2_bracket_item_slot_fit_rule.md`
- `docs/features/game2_bracket_item_slot_fit.md`

## Runtime impact
None. This overlay is card/LI/documentation only.

## Reason
The current Game 2 seeded items demonstrate the right data direction, but the next architectural requirement is to make seeded teams subordinate to the middle-layer PNG geometry. This must be treated as first-order because all later advancement depends on the same slot/item contract.
