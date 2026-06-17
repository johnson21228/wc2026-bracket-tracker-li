# Bracket lifecycle state

The WC2026 bracket board uses an explicit lifecycle state rather than guessing behavior from slot IDs alone.

## Phases

- `game1_r32_assignment` — Game 1 predicts/assigns R32 teams into bracket slots.
- `game1_knockout_prediction` — Game 1 predicts knockout winners from the currently assigned bracket contestants.
- `game1_locked_for_scoring` — Game 1 evidence is frozen for scoring.
- `game2_official_r32` — official R32 truth is loaded and is no longer user-predicted R32 truth.
- `game2_knockout_live` — Game 2 official-bracket knockout picks are being made or reviewed.

## Pick source separation

Game 1 and Game 2 must not overwrite each other.

Game 1 state contains:

- R32 assignment picks from the user prediction layer.
- Game 1 prediction `knockoutPicks` for R16/QF/SF and later final/champion picks.

Game 2 state contains:

- official R32 truth.
- Game 2 official-bracket `knockoutPicks`.

## Runtime decision

The board can now ask a canonical question before opening a menu:

```text
pickModeForSlotId(slotId)
```

Expected outcomes:

- R32 slot in Game 1 -> `game1_r32_assignment`
- R16/QF/SF slot in Game 1 -> `game1_knockout_pick`
- R32 slot in Game 2 -> `official_r32_display`
- R16/QF/SF slot in Game 2 -> `game2_knockout_pick`

This state layer prepares the runtime wiring that makes R16/QF/SF menus use resolved match contestants instead of the R32 group eligibility menu.
