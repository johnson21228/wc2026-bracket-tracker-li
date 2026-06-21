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


Final player-facing chrome refinement:
- Non-group knockout menus must not render source-label rows when the source label is a backend slot ID such as L-R16-01.
- Non-group knockout menus must not render generic section headers such as "Winner choices".
- The player-facing menu chrome is: clean title, candidate team choices, close control.


Group-source player-facing chrome refinement:
- Group seed labels such as 1A, 2B, or 3C are compact backend/source identifiers and must not render as pick-menu subtitle chrome.
- Enum-style source roles such as GROUP-RUNNER-UP are datamodel terms and must not render in player UI.
- Group-backed menus may show a clean group button, such as "Group B", and candidate teams.


Bracket-cell empty pick refinement:
- Durable slot IDs such as L-R16-02 must not render inside empty player-facing bracket cells.
- Empty pick cells should render player-facing placeholder text such as "Pick" or a specific player-facing label such as "Champion".
- Slot IDs remain valid as data attributes, controller keys, persistence keys, and test identifiers only.
