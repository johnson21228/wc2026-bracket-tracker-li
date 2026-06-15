# Prompt — Add Round-of-32 Slot Labels To HTML

```text
Update the WC2026 Bracket Tracker HTML and data model so each Round-of-32 slot has a qualification label.

Requirements:
- Read LI first.
- Preserve existing bracket/team/player state.
- Add or use `data/official_round_of_32_slot_rules.json`.
- Show slot labels in bracket slots before teams are assigned.
- When a team is resolved, show both team and slot label.
- Keep slot meaning separate from assigned team.
- Export/import JSON must preserve slot label data.
- Produce a new static HTML release and WB_SESSION Capture Back.
```
