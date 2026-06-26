# R32 Pick Card Rendering Rule

A Round of 32 pick card is the compact visual representation of a selected team inside a bracket slot.

## Authority

The card represents the player's selected team first. It must not primarily represent the slot label, seed code, source bracket text, or feeder rule.

## Required visible content

A filled R32 card must show:

- the selected team flag
- the selected team name

The team flag must be large enough to act as a primary visual identifier, not a small decorative icon.

## Optional secondary content

The card may show qualification/seed metadata only as quiet secondary text. Examples:

- `2A`
- `Winner Group A`
- `Runner-up Group A`
- `Best third-place team from Groups A/B/C/D/F`

Secondary metadata must never visually compete with the team name or flag.

## Suppressed competing labels

A filled R32 card must suppress or cover competing source slot labels when they create ambiguity.

Example: if South Korea is picked into a slot, the filled card should read as a South Korea card. A nearby/underlying `2B` label must not show through the filled card in a way that makes the pick appear attached to a different slot.

## Rendering priority

Inside a filled R32 slot, visual priority is:

1. selected flag
2. selected team name
3. optional quiet qualification metadata
4. source slot labels only when not confusing

## Game 1 behavior

For Game 1, the R32 card represents the Admin_/official hydrated occupant for that slot. In normal player mode it is not a player-authored qualifier prediction. A player BracketDocument may carry the R32 occupant for rendering/preselection compatibility only when that record was copied from Supabase Admin_/official and marked `playerAuthored: false`.

## Game 2 behavior

For Game 2, the R32 card represents the seeded knockout team or the user's selected advancement team. The visual card should still read as a team card first.
