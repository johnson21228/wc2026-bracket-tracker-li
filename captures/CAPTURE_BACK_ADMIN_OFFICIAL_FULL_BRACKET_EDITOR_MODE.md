# Capture Back: Admin official full bracket editor mode

## Change

Added Admin official full bracket editor mode so the `Admin_/official` identity can edit all official bracket truth slots, not just R32.

## Intent preserved

- `Admin_/official` owns official bracket truth.
- Normal players own only their player bracket picks after R32.
- Player-visible R32 always mirrors `Admin_/official`.
- Normal players must not author R32.
- Normal player edits must not write into the Admin official document.

## Runtime shape

Admin official mode uses a separate official save path:

```text
Admin_/official editor selection -> officialPicks -> Supabase Admin_/official bracket document
```

Normal player mode keeps the player save path separate:

```text
normal player R16++ selection -> player picks -> signed-in player's bracket document
```

R32 remains special for normal players:

```text
playerVisibleR32 = Admin_/official R32 truth
```

## Verification

`tools/verify_wc2026_admin_official_full_bracket_editor_mode.py` verifies:

- Admin full editor mode is query-gated and passed into the model.
- Admin full editor mode requires a Supabase official save method.
- Admin picks use `officialPicks` as the editable/rendered truth source.
- Admin edits persist through `saveAdminOfficialBracketTruth`.
- Normal player R32 remains read-only.
- Normal player R16++ picks remain player-owned.
- Admin official later-round truth is distinct from normal player picks.
