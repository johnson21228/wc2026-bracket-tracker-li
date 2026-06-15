WB_SESSION:
Capture Round-of-32 Drop Only Rule

Changed:
- Captured requirement that drag/drop placement should be limited to Round-of-32 slots.
- Added LI rule explaining that later rounds should be populated by winner selection, official results, or derived advancement.
- Added feature note, card, and implementation prompt.

Decision captured:
- Drop only is wanted for R32 placement.
- R16, QF, SF, Final, and Champion slots should not accept arbitrary team drops.
- Later rounds should represent bracket logic, not free placement.

Files added:
- `li/world_cup/round_of_32_drop_only_rule.md`
- `docs/features/r32_drop_only_note.md`
- `cards/018_limit_drag_drop_to_round_of_32_card.md`
- `prompts/limit_drag_drop_to_round_of_32.md`

Next:
- Apply overlay.
- Implement Card 018 in the static HTML.
