# Game 1 R32 Slot Qualification Mapping

This restores the older Game 1 bracket logic: each R32 target knows what it represents before a team is selected.

Examples:

- `2A` means runner-up Group A.
- `1F` means winner Group F.
- `3 A/B/C/D/F` means a best third-place team from that group pool.

The menu is therefore slot-aware. Tapping a slot opens a team picker filtered to the slot's allowed group or group pool. This keeps Game 1 as a Round-of-32 assignment game rather than a generic drag/drop board.

The mapping is stored at:

```text
site/data/game1_r32_slot_assignment_rules.json
```

The runtime currently embeds the same mapping into `site/game1/index.html` so it works from `file://` without a local server.
