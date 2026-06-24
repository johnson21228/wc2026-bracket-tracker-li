# Rule: Player Standings Pick Viewer Is Read-only Public Bracket Inspection

The Standings panel may let joined players inspect other players' bracket picks only through public standings data.

Required invariant:
- Public player names are display-only identity labels sourced through `profiles.display_name`.
- The picks viewer renders from `picksBySlot` already present on the standings row.
- Empty picks render as `Unpicked` or equivalent player-facing copy.
- The viewer must be keyboard-accessible and closable.

Forbidden:
- Do not expose raw email, auth IDs, or private account identifiers.
- Do not add write behavior from the standings viewer.
- Do not insert, update, upsert, delete, save, or mutate bracket storage.
- Do not bypass the Join-first player model or existing read-only standings preflight.
