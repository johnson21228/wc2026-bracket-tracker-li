# Card 116 — Add Game 1/Game 2 bracket lifecycle state

## Intent
Add an explicit lifecycle state so the Game 1 board no longer has to infer behavior only from slot type.

## Rule
The bracket surface must know whether it is operating as:

- `game1_r32_assignment`
- `game1_knockout_prediction`
- `game1_locked_for_scoring`
- `game2_official_r32`
- `game2_knockout_live`

## Why
R32 slots and knockout slots require different menus. Without lifecycle state, a tapped R16/QF/SF slot can be routed through the old R32 group menu and show an empty set even when the match contestants exist.

## Evidence to preserve
Game 1 evidence must remain durable:

- user-predicted R32 assignment picks
- user-predicted `knockoutPicks`

Game 2 evidence must remain separate:

- official R32 truth
- Game 2 official-bracket `knockoutPicks`
