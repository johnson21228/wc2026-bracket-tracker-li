# WC2026 App Module Boundary Map

## Current inspection summary

The repo already contains strong Workbench governance and many focused World Cup LI rules. The deployable site lives under `site/` and currently has three public entry points:

- `site/index.html` — landing page
- `site/game1/index.html` — Game 1 Round-of-32 chooser board
- `site/game2/index.html` — Game 2 knockout board foundation

Important current data/assets:

- `site/data/teams_from_flags_images.json` contains 48 teams.
- `site/data/groups_from_flags_images.json` contains 12 groups of 4 teams.
- `site/data/game1_r32_slot_menu_rules.json` contains 32 Game 1 R32 slot/menu rules with pixel bounds.
- `site/data/game2_bracket_geometry_slots.json` contains bracket geometry slots for the shared board.
- `site/assets/playfield/r32_bracket_geometry_overlay.png` is the visible bracket geometry overlay.
- `site/assets/playfield/r32_game_board_hd.jpeg` and `.png` are shared board source assets.

The main architectural issue is not absence of intent. The issue is that many app responsibilities are still implemented or duplicated inside static pages. The next step is to define durable modules and then gradually extract runtime code into those modules while preserving current behavior.

## Proposed app modules

### Source Evidence

Preserves raw sources, transcriptions, screenshots, poster data, official corrections, and provenance.

Primary folders:

- `source/`
- `source/images/`
- `source/text/`
- `capture_back/`

### Tournament Data

Holds neutral tournament facts: teams, groups, flags, matches, standings, official R32, official knockout results.

Primary files:

- `site/data/teams_from_flags_images.json`
- `site/data/groups_from_flags_images.json`
- `site/data/group_stage_matches.json`
- `site/data/group_standings.json`
- `site/data/official_round_of_32.json`
- `site/data/official_knockout_results.json`

### Qualification Rules

Defines how 48 teams become 32 qualifiers and how each R32 slot knows its eligible group/place/pool.

Primary files:

- `site/data/game1_r32_slot_menu_rules.json`
- `site/data/game1_r32_slot_assignment_rules.json`
- future: `site/data/qualification_rules.json`
- future: `site/assets/js/qualification-rules.js`

### Game 1 — R32 Qualifier Picker

Lets players fill the 32 pre-knockout bracket positions using slot-aware menus.

Primary surface:

- `site/game1/index.html`

Future runtime module:

- `site/assets/js/game1-r32-picker.js`

### Game 2 — Knockout Bracket Picker

Uses a fixed R32 seed and supports winner advancement through the bracket.

Primary surface:

- `site/game2/index.html`

Current/future data:

- `site/data/game2_round_of_32_seed.json`
- `site/data/game2_bracket_geometry_slots.json`
- future: `site/assets/js/game2-knockout-picker.js`

### Scoring

Calculates Game 1 and Game 2 results without mixing picks and official data.

Primary files:

- `site/data/game_1_scoring_rules.json`
- `site/data/game_2_scoring_rules.json`
- `site/data/game_1_scores.json`
- `site/data/game_2_scores.json`

### Board Geometry

Owns the 1536 × 1024 pixel-native board plane and all slot/hit/render regions.

Primary files:

- `site/assets/playfield/r32_bracket_geometry_overlay.png`
- `site/data/game1_r32_slot_menu_rules.json`
- `site/data/game2_bracket_geometry_slots.json`
- `site/data/geometry/*.json`

Future runtime module:

- `site/assets/js/pixel-board.js`

### UI Surface

Renders pages, menus, flags, pick cards, labels, overlays, and user interaction.

Primary files:

- `site/index.html`
- `site/game1/index.html`
- `site/game2/index.html`
- future: `site/assets/css/*.css`
- future: `site/assets/js/*.js`

### Persistence / Export

Owns local storage, JSON export/import, lock status, timestamps, and correction records.

Current implementation:

- localStorage in page scripts

Future runtime module:

- `site/assets/js/pick-storage.js`

### Verification

Preserves boundaries and catches regressions.

Primary files:

- `tools/verify_wc2026_bracket_tracker.py`
- future: schema checks for teams/groups/slots/third-place pools/geometry mappings

## Near-term implementation sequence

1. Add module boundary LI and this architecture map.
2. Add verifier checks for current data shape: 48 teams, 12 groups of 4, 32 Game 1 R32 slot rules, explicit third-place pools, and pixel bounds.
3. Extract Game 1 embedded `SLOT_RULES` and `GROUPS` from `site/game1/index.html` into JSON fetch/load helpers while preserving the current menu behavior.
4. Add `site/assets/js/pixel-board.js` for board-coordinate helpers.
5. Add `site/assets/js/qualification-rules.js` for eligible-team filtering.
6. Add `site/assets/js/game1-r32-picker.js` for Game 1 orchestration.
7. Add `site/assets/js/game2-knockout-picker.js` after Game 2 winner advancement behavior is ready.

## Design invariant

A user tap on a board slot should resolve through this chain:

```text
pixel hit region
-> logical slot id
-> qualification rule or bracket feeder rule
-> eligible teams or feeder teams
-> rendered menu/pick card
-> persisted player pick
```

No step in that chain should be hidden inside ad hoc UI code once the module extraction begins.
