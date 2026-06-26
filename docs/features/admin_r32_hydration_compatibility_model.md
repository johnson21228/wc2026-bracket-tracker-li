# Admin R32 hydration compatibility model

This feature note aligns the LI with the current knockout-only game model.

Admin_/official owns the R32 occupant field. Normal players do not author R32 occupants, but their BracketDocuments may store R32 entries copied from Supabase Admin_/official so existing rendering, standings, scoring, and R16++ preselection paths continue to work.

The copy rule is narrow:

- Copy ONLY R32 entrant slots.
- Copy ONLY from Supabase Admin_/official.
- Mark copied R32 entries with Admin_/official source/authority metadata and `playerAuthored: false`.
- Do not copy Admin_/official R16, QF, SF, Final, Champion, or third-place truth into player documents.
- Preserve existing player R16++ picks.

This supersedes older language that described player-authored R32 occupant prediction.
