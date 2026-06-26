# Game 1 Data-Driven Slot Menu

This feature moves Game 1 R32 chooser data out of the HTML runtime and into module-owned data.

## Problem

Game 1 was already behaving closer to the desired surface: tapping an R32 slot opened a menu of eligible teams, with flags and group options. But the page still carried large embedded JavaScript arrays for the slot rules and group/team data. That made the UI file a second source of truth.

## Decision

Game 1 now loads a browser-ready data bundle:

```text
site/data/game1_data_bundle.js
```

The bundle is generated from existing JSON data files:

```text
site/data/game1_r32_slot_menu_rules.json
site/data/teams_from_flags_images.json
site/data/groups_from_flags_images.json
```

This keeps the page easy to open locally while preserving the boundary that data and rules live outside the UI surface.

## Responsibilities

### Tournament Data

Owns the 48 teams, their group assignment, display names, abbreviations, and flags.

### Qualification Rules

Owns the 32 Round of 32 slot rules, including winners, runners-up, and third-place eligible group pools.

### Game 1

Maps a tapped R32 slot to its eligible teams only for Admin_/official R32 editing. Normal players do not store player-authored R32 occupant picks.

### UI Surface

Renders the board, hit targets, chooser menu, flags, and picked cards. It does not own the data itself.

## Verification

The verifier checks that:

- the Game 1 page loads `../data/game1_data_bundle.js`,
- the page no longer embeds full `SLOT_RULES` or `GROUPS` data literals,
- the bundle exposes `window.WC2026_GAME1_DATA`,
- the source JSON has 32 R32 slots, 12 groups, and 48 teams,
- every slot's eligible groups exist in the group data.
