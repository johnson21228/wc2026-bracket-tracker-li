WB_SESSION:
Capture Round-of-32 Slot Labels

Changed:
- Captured the requirement that bracket slots should include qualification labels, not only empty drop targets.
- Added LI rule separating slot meaning from team assignment.
- Added starter data file for official Round-of-32 slot rules.
- Added JSON schema for slot-label data.
- Added Card 008 and prompt to implement this in the static HTML.

Decision captured:
- Round-of-32 slots should preserve useful information about what kind of team goes into the slot.
- The official team may be unknown, but the slot label can still be known.
- Later, the slot can resolve from pending label to actual team assignment.

Example:
```text
Before:
R32-M1-A: Winner Group A

After:
R32-M1-A: Mexico — Winner Group A
```

Files added:
- `li/world_cup/round_of_32_slot_label_rule.md`
- `data/schema/round_of_32_slot_rule_schema.json`
- `data/official_round_of_32_slot_rules.json`
- `cards/008_capture_round_of_32_slot_labels_card.md`
- `prompts/add_round_of_32_slot_labels_to_html.md`

Next:
- Apply overlay.
- Later populate actual official slot labels from verified bracket source.
- Incorporate labels into Game 1/Game 2 HTML UI.
