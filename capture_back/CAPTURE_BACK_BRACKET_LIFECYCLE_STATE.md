# Capture Back — Bracket lifecycle state

## Change
Added a bracket lifecycle state layer to Game 1 runtime code and captured the associated LI rule, feature doc, prompt, and verification.

## Runtime state
The board now defines these phases:

- `game1_r32_assignment`
- `game1_knockout_prediction`
- `game1_locked_for_scoring`
- `game2_official_r32`
- `game2_knockout_live`

## Runtime API
The Game 1 page exposes:

```js
window.WC2026_BRACKET_LIFECYCLE
```

with helpers for reading/writing state and determining slot pick mode.

## Evidence boundary
Game 1 R32 assignment picks and Game 1 `knockoutPicks` are treated as Game 1 evidence. Game 2 official-bracket `knockoutPicks` are separate.

## Why this matters
The same visual bracket may serve Game 1 and Game 2 over time. Explicit lifecycle state prevents R16/QF/SF taps from accidentally falling through to the old R32 group menu path and showing an empty set when contestants exist.
