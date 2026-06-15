WB_SESSION:
Capture Simple Header And Round-of-32 Slot Tooltips

Changed:
- Captured UI requirement for a simpler public page title and top instructions.
- Captured requirement that the page tell users to drag/drop teams and scroll to see the bracket.
- Captured requirement for Round-of-32 slot tooltips explaining the rule used to assign each slot.
- Added LI rule, feature note, card, prompt, and tooltip data example.

Decision captured:
- The public UI should be simple and action-oriented.
- Workbench explanation should stay in repo/source/history or optional details, not dominate the page header.
- Round-of-32 slots should have labels plus tooltips.
- Tooltips should describe slot assignment rules, such as group winner, runner-up, or best third-place source.

Files added:
- `li/world_cup/simple_header_and_slot_tooltip_rule.md`
- `docs/features/simple_header_and_slot_tooltips_note.md`
- `cards/010_simplify_header_and_add_slot_tooltips_card.md`
- `prompts/simplify_header_and_add_slot_tooltips_to_html.md`
- `data/schema/round_of_32_slot_tooltip_example.json`

Next:
- Apply overlay.
- Implement Card 010 in the static HTML, ideally together with the Groups section and Game 1 picker work.
