# Verify Canonical Knockout Assignment Render Repair

Check Game 1 manually:

1. Pick two upstream R32 teams.
2. Tap `L-R16-01`.
3. Confirm the choice menu appears beside the cell.
4. Select one team.
5. Confirm that exact team appears in `L-R16-01`.
6. Refresh the page.
7. Confirm the team remains in `L-R16-01`.

Run:

```bash
python3 tools/verify_wc2026_canonical_assignment_render_repair_patch.py
make verify
make pack
```
