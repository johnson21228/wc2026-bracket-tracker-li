# Capture Back: Repair Export All Picks TODO

## Captured Decision

Create a TODO item for repairing Bracketeering Pub pick export completeness before implementing code changes.

## Why

The export feature is user-trust critical. If the board shows picks that are not exported, the player cannot safely preserve or share their bracket state.

## Key Finding

The observed export includes all 32 R32 picks, so the immediate defect is not missing R32 picks. The observed defect is incomplete later-round export coverage plus the spelling inconsistency in `braketeering` vs `bracketeering`.

## Durable TODO

- `docs/dev/todo_repair_bracketeering_pub_export_all_picks.md`
- `cards/210_repair_bracketeering_pub_export_all_picks_card.md`
