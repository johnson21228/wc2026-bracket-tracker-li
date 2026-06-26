# Single Game Admin_/official Runtime Rule

Bracketeering is one connected game, persisted as `game1`.

`game-1` and `game-2` are not separate player game authorities. If legacy `game-2` appears in the UI/runtime, it is only a bracket-board presentation alias.

Admin_/official owns Round-of-32 occupants. Player-owned picks begin with winners after the official R32 field is supplied. Players may render R32 occupants but may not author them.

Supabase is required for connected play. The site may not silently fall back to disconnected authority. If the public locked/submitted Admin_/official row is missing, normal players fail closed. A signed-in Admin_/official editor may still render the bracket board while connected so the missing official row can be created.
