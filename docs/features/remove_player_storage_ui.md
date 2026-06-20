# Remove player-facing storage plumbing UI

Bracketeering Pub should present gameplay controls to players. Storage/debug plumbing belongs behind the runtime model and developer seams, not in the normal player header.

## Removed from normal UI

- Capture Picks
- Export Picks
- Import Picks
- JSON import file picker controls

## Preserved internally

The removal is intentionally UI-facing only. The model may continue to expose serialization helpers while Supabase persistence and migration paths stabilize. The localStorage bracket store and canonical BracketDocument save seam remain the runtime persistence authority for anonymous play.

## Verification

`tools/verify_wc2026_remove_player_storage_ui.py` checks that the normal site entrypoint does not render storage plumbing controls while localStorage and internal model helpers remain present.
