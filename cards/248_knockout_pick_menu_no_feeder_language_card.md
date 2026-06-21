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
