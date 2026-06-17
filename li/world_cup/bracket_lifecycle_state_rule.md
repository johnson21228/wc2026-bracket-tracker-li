# LI Rule — Bracket lifecycle state

The bracket board must carry an explicit lifecycle state whenever the same visual surface can serve both Game 1 and Game 2.

## Canonical phases

The allowed lifecycle phases are:

- `game1_r32_assignment`
- `game1_knockout_prediction`
- `game1_locked_for_scoring`
- `game2_official_r32`
- `game2_knockout_live`

## Game 1 evidence boundary

Game 1 results evidence must be preserved independently of Game 2:

- user-predicted R32 assignments
- user-predicted `knockoutPicks`

Loading official R32 truth for Game 2 must not destroy Game 1 prediction evidence.

## Game 2 evidence boundary

Game 2 uses official R32 truth and has its own official-bracket `knockoutPicks`.

## Menu authority

When a slot is tapped, the lifecycle state determines which menu rule applies:

- Game 1 R32 assignment phase: R32 slots use group/slot eligibility choices.
- Game 1 knockout prediction phase: R16/QF/SF slots use resolved match contestants from feeding bracket slots.
- Game 2 phases: official truth is the source for R32 and downstream knockout contestants.

An empty-state menu is valid only when required feeder contestants are actually missing.
