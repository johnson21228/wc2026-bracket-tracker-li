# Game 1 Data-Driven Slot Menu Rule

Game 1 Round of 32 chooser menus must be driven by module-owned data, not hidden duplicate arrays embedded in the HTML surface.

## Rule

For every Game 1 R32 tap:

```text
pixel hit region
-> slotId / logical slot identity
-> slot menu rule data
-> eligible group pool
-> eligible teams from tournament data
-> rendered chooser menu
-> persisted player pick
```

The UI surface may render and handle interaction, but it must not be the source of truth for:

- the 32 R32 slot identities,
- the qualification kind for each slot,
- the eligible group pool for each slot,
- the 48-team tournament/team/flag data,
- the group membership data.

## Current local-review implementation

`site/game1/index.html` loads `site/data/game1_data_bundle.js` before the Game 1 runtime script. The bundle is generated from the JSON data files so the page still works when opened directly from Finder / `file://`, where browser JSON `fetch()` can be unreliable.

Authoritative JSON inputs:

- `site/data/game1_r32_slot_menu_rules.json`
- `site/data/teams_from_flags_images.json`
- `site/data/groups_from_flags_images.json`

Generated browser bundle:

- `site/data/game1_data_bundle.js`

## Boundary

- Tournament Data owns teams, flags, display names, and groups.
- Qualification Rules owns slot eligibility and third-place group pools.
- Game 1 owns applying those rules to a user pick surface.
- UI Surface owns rendering only.

The HTML may bind `SLOT_RULES`, `GROUPS`, and `TEAMS` from `window.WC2026_GAME1_DATA`, but must not embed full duplicate data literals.
