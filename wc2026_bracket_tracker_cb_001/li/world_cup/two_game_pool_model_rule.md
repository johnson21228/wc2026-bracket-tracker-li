# Two-Game Pool Model Rule

## Purpose

The World Cup Bracket Tracker Workbench supports two related prediction games backed by one tournament truth model.

## Game 1 — Round-of-32 Qualifier Pick Game

Before the official knockout field is known, players predict which 32 teams will advance out of the 48-team group stage.

This game stores:

- player identity
- selected 32 teams
- submission timestamp
- lock status
- scoring rules
- score after official Round of 32 is known

Game 1 must not require the official Round-of-32 bracket slots to exist.

## Game 2 — Knockout Bracket Pick Game

After the official Round of 32 field and bracket slots are known, players predict the full knockout bracket:

- Round of 32 winners
- Round of 16 winners
- Quarterfinal winners
- Semifinal winners
- Final winner / Champion

Game 2 should not open until the official Round-of-32 field and match slots are available.

## Separation Rule

Keep these separate:

1. tournament truth
2. Game 1 picks
3. Game 1 scoring
4. official Round-of-32 bracket
5. Game 2 picks
6. Game 2 scoring
7. released HTML views

Do not mix player predictions with official results.

## Lock Rule

Each game has its own lock moment.

- Game 1 locks before group-stage results make advancement obvious.
- Game 2 locks before knockout play begins.

Corrections after lock must be recorded as corrections, not silent edits.
