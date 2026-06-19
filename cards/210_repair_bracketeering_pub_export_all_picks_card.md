# Card 210: Repair Bracketeering Pub Export Completeness

## Intent

Capture a high-priority TODO to repair the Bracketeering Pub export so it preserves every pick made by the player.

## Trigger

A user-exported JSON file showed the export filename/app id still using `braketeering`, and the exported data included complete R32 picks but only partial later-round picks.

## Observation

The site visibly showed picks made for all R32 slots. The export confirmed that R32 was complete, but later knockout pick coverage was incomplete.

## Requirement

The export must represent all picks the site knows about, not merely one in-memory or single-localStorage representation.

## Acceptance Criteria

- Fix filename spelling: `bracketeering-pub-picks-${date}.json`.
- Fix app id spelling: `wc2026.bracketeeringPub.picks`.
- Export all known Game 1 picks across current and durable stores.
- Normalize exported picks to a stable `slotId: teamId` shape.
- Include export summary counts so incomplete exports are visible immediately.
- Add verification that catches spelling regressions and partial-store export regressions.

## TODO Document

See:

- `docs/dev/todo_repair_bracketeering_pub_export_all_picks.md`
