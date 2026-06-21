# Capture Back: Knockout pick menu no-feeder language

## Intent

Remove player-facing "feeder" wording from knockout winner pick menus.

## Rule

Feeder relationships remain internal model logic. The pick menu should not display labels such as:

- Feeder choices
- KNOCKOUT-* FEEDER

Player-facing language should describe the action instead:

- Pick winner
- Winner choices

## Scope

This is a UI-language cleanup only. It does not change bracket dependency logic, pick storage, source slot IDs, or canonical pick IDs.


Player-facing ID refinement:
- Durable pick IDs such as L-R16-01, R32-01, CHAMPION, and KNOCKOUT-* are backend/datamodel identifiers only.
- Pick menus must not render these IDs as visible titles, section labels, source roles, or accessibility labels.
- Knockout winner menus should present the candidate choices directly under a player-facing title such as "Make your pick".
