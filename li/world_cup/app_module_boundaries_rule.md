# WC2026 App Module Boundaries Rule

## Purpose

The WC2026 Bracket Tracker is a static website with at least two games, but it must be governed as a modular app. Tournament facts, game rules, player picks, scoring, board geometry, and UI rendering must remain separate responsibilities.

This rule exists to prevent one HTML page or one JavaScript block from becoming the hidden authority for tournament truth, slot qualification, third-place logic, scoring, persistence, or board geometry.

## Required module boundaries

### 1. Source Evidence Module

Owns source artifacts and provenance.

Responsibilities:

- preserve raw source artifacts under `source/`
- record whether data is poster-derived, flag-image-derived, demo, manual, or official
- maintain source priority from `li/world_cup/source_authority_rule.md`
- never silently overwrite official tournament facts

Must not:

- store player picks
- decide game scoring
- render UI

### 2. Tournament Data Module

Owns neutral tournament facts.

Responsibilities:

- 48 team records
- 12 groups of 4 teams
- flag identity for each team
- match schedule and results
- group standings
- official Round-of-32 field once known
- official knockout results once known

Preferred data files:

- `site/data/teams_from_flags_images.json` until official data replaces or verifies it
- `site/data/groups_from_flags_images.json` until official data replaces or verifies it
- `site/data/group_stage_matches.json`
- `site/data/group_standings.json`
- `site/data/official_round_of_32.json`
- `site/data/official_knockout_results.json`

Must not:

- contain user selections
- contain UI pixel geometry
- contain scoring presentation state

### 3. Qualification Rules Module

Owns how group-stage outcomes map to the 32-team knockout field.

Responsibilities:

- define the 24 automatic qualifiers: 12 group winners and 12 group runners-up
- define the best 8 third-place qualifiers
- define third-place ranking criteria in order
- define which third-place pools are eligible for each R32 slot
- expose a deterministic function-like contract: group standings + R32 slot rule -> eligible team set or official assigned team

This module is the authority for menus shown in Game 1 R32 slots and for official slot assignment after standings are known.

Must not:

- know where a slot is drawn on the board
- know how menu tiles look
- mutate Game 2 picks

### 4. Admin_/official Module — Round-of-32 Occupant Authority

Owns the official Round-of-32 occupant field. Normal players do not assign, project, or predict R32 occupants.

Responsibilities:

- let Admin_/official assign official team occupants to Game 1 R32 slots
- persist those occupants in the Supabase Admin_/official official bracket document
- expose ONLY Supabase Admin_/official R32 entrants for player BracketDocument hydration
- preserve partial Admin_/official truth without filling missing R32 slots from static JSON, localStorage, or stale player documents

Must not:

- copy Admin_/official R16, QF, SF, Final, Champion, or third-place truth into normal player documents
- let normal players author R32 occupant slots
- use a player bracket as the source of truth for the official R32 field

### 5. Player Knockout Module — R32 Winner and Later Picks

Owns the player-owned knockout picks after the official R32 occupants are available.

Responsibilities:

- hydrate ONLY R32 entrant slots from Supabase Admin_/official into player BracketDocuments for rendering, scoring, and R16++ preselection compatibility
- mark hydrated R32 entries with Admin_/official source/authority metadata and `playerAuthored: false`
- let players pick R32 match winners and R16/QF/SF/final/champion winners
- advance winners downstream only through valid feeder paths
- clear dependent downstream picks when a player-owned upstream pick changes

Must not:

- generate official R32 slots from player picks
- copy Admin_/official later-round truth into player documents
- use demo seed data without visibly marking it as demo/non-official

### 6. Scoring Module

Owns scoring rules and score calculation.

Responsibilities:

- keep Game 1 scoring separate from Game 2 scoring
- calculate Game 1 correct R32 predictions against official data
- calculate Game 2 bracket score against official knockout results
- expose tiebreaker metadata without changing bracket authority

Preferred data files:

- `site/data/game_1_scoring_rules.json`
- `site/data/game_2_scoring_rules.json`
- `site/data/game_1_scores.json`
- `site/data/game_2_scores.json`

Must not:

- change source data
- change player picks silently
- make UI-only assumptions about official truth

### 7. Board Geometry Module

Owns the pixel-native game board plane.

Responsibilities:

- preserve the native 1536 × 1024 coordinate system
- define every slot, hit target, rendered card region, connector, and advancement destination in board pixels
- keep Game 1 and Game 2 aligned to the same board plane when sharing the board
- treat the source PNG/JPEG board as geometry authority until a future generated geometry source replaces it

Preferred data files:

- `site/data/game1_r32_slot_menu_rules.json` for Game 1 R32 pixel hit/menu regions
- `site/data/game2_bracket_geometry_slots.json` for Game 2 bracket slot regions
- `site/data/geometry/*_manifest.json` for geometry provenance

Must not:

- decide which teams are eligible
- store picks
- decide scoring

### 8. UI Surface Module

Owns rendering and interaction only.

Responsibilities:

- render landing page, Game 1 page, and Game 2 page
- render flags, names, slot labels, menus, pick cards, and board layers
- call data/rule modules rather than duplicating their authority inline
- keep tap/hit targets synchronized with pixel-native geometry

Preferred future files:

- `site/game1/index.html`
- `site/game2/index.html`
- `site/assets/js/tournament-data.js`
- `site/assets/js/qualification-rules.js`
- `site/assets/js/game1-r32-picker.js`
- `site/assets/js/game2-knockout-picker.js`
- `site/assets/js/pixel-board.js`
- `site/assets/js/pick-storage.js`

Must not:

- embed the only copy of teams, groups, slot rules, or scoring rules once module extraction begins
- make hidden tournament-rule decisions in event handlers

### 9. Persistence and Export Module

Owns local save/export/import boundaries.

Responsibilities:

- keep each game's local storage key separate
- export player picks as explicit versioned JSON
- include player identity, game id, submission timestamp, lock status, and correction history when available
- keep official data and player data separate

Must not:

- store official truth as if it were player data
- silently overwrite locked submissions

### 10. Verification Module

Owns static checks that preserve the above boundaries.

Responsibilities:

- verify required site files exist
- verify 48 teams and 12 groups of 4
- verify 32 Game 1 R32 slot rules
- verify third-place slots have explicit candidate group pools
- verify every Game 1 R32 slot has pixel bounds and a qualification rule
- verify every Game 2 R32 seed item maps to a geometry slot
- verify no root HTML page competes with `site/`

Must not:

- repair data silently
- accept placeholder official data as final authority

## Extraction rule

When a behavior is needed by more than one page or one game, move it out of inline page code and into a named module file under `site/assets/js/` or into versioned JSON under `site/data/`.

Inline HTML scripts may temporarily orchestrate modules, but they must not be the only durable place where tournament facts, qualification rules, scoring rules, or geometry rules live.

## Current-state exception

The current site still embeds significant Game 1 runtime data directly in `site/game1/index.html`. This is allowed only as a transitional implementation state. New LI should point toward extracting those embedded constants into reusable data/runtime modules without changing the current visible behavior.
