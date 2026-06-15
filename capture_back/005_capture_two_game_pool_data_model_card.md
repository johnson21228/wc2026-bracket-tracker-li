# Card 005 — Capture Two-Game Pool Data Model

## Intent

Define the data model for the World Cup Bracket Tracker as two related prediction games.

## Game 1

Players pick the 32 teams that will advance from the 48-team group stage.

## Game 2

After the official Round of 32 field is known, players fill out a complete knockout bracket.

## Acceptance

- Game 1 and Game 2 are stored separately.
- Tournament truth is stored separately from player picks.
- Scoring rules are explicit per game.
- Official Round of 32 is represented as future unknown state.
- Poster-derived source data is preserved as initial evidence.
