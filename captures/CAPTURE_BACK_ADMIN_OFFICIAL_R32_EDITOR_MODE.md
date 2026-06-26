# CAPTURE BACK: Admin official R32 editor mode

## Capture

Only Admin_/official may edit R32 occupant slots.
All players mirror Admin_/official R32 occupant truth.

This capture adds an explicit Admin_/official R32 editor mode. The normal public/player runtime remains read-only for R32 and continues to force player-visible R32 from Supabase `Admin_/official`.

## Runtime rule

- Normal player mode: R32 is read-only and mirrors Admin_/official.
- Admin_/official editor mode: R32 slots become editable and save back to the Supabase `Admin_/official` official bracket document.
- R16++ player picks remain player-owned.

## Guardrail

The editor is explicit and separate. It does not reintroduce player-owned R32 picks. It only gives the official row a way to author the truth that players later mirror.
