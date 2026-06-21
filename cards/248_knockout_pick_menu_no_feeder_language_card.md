# Card 248: Knockout pick menu no-feeder language

## Status

Implemented

## Goal

Remove internal feeder terminology from player-facing knockout winner pick menus.

## Behavior

- Knockout menus should not show "Feeder choices".
- Knockout menu source/detail text should not show "KNOCKOUT-* FEEDER".
- Feeder dependencies remain internal model logic.

## Verification

`tools/verify_wc2026_knockout_pick_menu_no_feeder_language.py`


Player-facing ID rule:
- Player UI must not expose durable pick IDs, game IDs, source IDs, or slot IDs.
- These identifiers remain valid for model/controller/storage logic only.
- Pick menu chrome should use player-facing language and candidate team choices.


Final player-facing chrome rule:
- No source-label rows for backend slot IDs.
- No generic "Winner choices" section headers for non-group knockout menus.
- Group headers remain allowed only for real group-backed sections.


Group-source chrome rule:
- Group seed labels such as 1A, 2B, or 3C are backend/source identifiers, not player-facing chrome.
- Enum-style source roles such as GROUP-RUNNER-UP must be hidden from player UI.
- Group-backed pick menus may keep clean group names and team choices.


Bracket-cell empty pick rule:
- Empty player-facing bracket cells must not show durable slot IDs such as L-R16-02.
- Use player-facing placeholder text for empty pick cells.
- Keep durable IDs only in data/model/controller/storage surfaces.
