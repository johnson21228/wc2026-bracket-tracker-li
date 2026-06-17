# Card 126: Repair Canonical Knockout Assignment Render

## Claim

The knockout choice menu must apply the selected team to the bracket cell that opened the menu.

## Acceptance Criteria

- Opening a knockout menu records the assignment target slot id.
- Opening a knockout menu records the assignment round.
- Clicking a team tile writes the selected team to the correct round-specific store.
- The selected team is rendered into the same bracket cell.
- The menu closes after assignment.
- The repair does not add another competing assignment wrapper.

## Verification

Run:

```bash
python3 tools/verify_wc2026_canonical_assignment_render_repair_patch.py
make verify
make pack
```
