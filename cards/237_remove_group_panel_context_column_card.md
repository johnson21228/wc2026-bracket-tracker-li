# Card 237 — Remove group panel Context column

## Intent
Remove the player-facing `Context` column from the group standings panel while preserving the underlying standings model and completed-match evidence.

## Rationale
The standings rank, points, and stat columns already communicate the table state. The `Context` badges such as `Group Winner`, `Runner Up`, `Third Place Candidate`, and `Fourth Place` add visual noise in the player-facing panel.

## Scope
- View-only cleanup of the group standings table render path.
- Keep model data and ranking logic unchanged.
- Keep completed matches and highlight links unchanged.
- Do not change pick menus, storage, Supabase, or Game 1 pick validity.

## Acceptance
- Group panel no longer renders `Context` header.
- Group panel no longer renders qualification/context badge cells.
- Rank, Team, MP, W, D, L, GF, GA, GD, and Pts remain visible.
- Completed matches and highlight links remain visible.
- `tools/verify_wc2026_group_panel_no_context_column.py` passes.
- `make verify` and `make pack` pass.
