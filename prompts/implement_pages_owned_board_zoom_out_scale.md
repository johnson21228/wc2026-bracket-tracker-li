# Prompt: Implement Pages-Owned Board Zoom-Out Scale

Use this prompt after Card 223 is accepted.

## Task

Implement board zoom-out support in the Pages site while preserving native board geometry and durable pick data.

## Constraints

- Keep all View and Controller work inside the Pages site.
- Do not change Supabase SQL, RLS, or durable model contracts.
- Do not rewrite geometry manifests into scaled coordinates.
- Do not change slot IDs or pick IDs.
- Keep the change isolated and easy to revert.

## Required behavior

- Support board render scales below 100%, at least 75% and 50%.
- Keep pick buttons aligned with native board slots.
- Keep pick menus anchored correctly.
- Keep group panels anchored/clamped correctly.
- Convert pointer coordinates through the current render scale before controller use.

## Verification

Run:

```bash
cd /Users/stevejohnson/Developer/wc2026-bracket-tracker-li

python3 tools/verify_wc2026_pages_owned_board_zoom_out_scale.py
make verify
make pack
```
