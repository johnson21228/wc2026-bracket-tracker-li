# Card 1018: Admin official full bracket editor mode

## Goal

Allow the `Admin_/official` identity to edit all official bracket truth slots while preserving player ownership rules.

## Scope

- Admin official full bracket editor mode.
- Official BracketDocument persistence through Supabase.
- R32 mirror/read-only behavior for normal players.
- R16++ player editability for normal players.

## Invariant

`Admin_/official` owns official bracket truth.
Normal players own only their player bracket picks after R32.
Player-visible R32 always mirrors `Admin_/official`.

## Verification

Run:

```bash
python3 tools/verify_wc2026_admin_official_full_bracket_editor_mode.py
```
