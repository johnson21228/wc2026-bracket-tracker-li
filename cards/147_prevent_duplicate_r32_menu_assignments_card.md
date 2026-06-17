# Card 147 — Prevent Duplicate R32 Menu Assignments

## Intent
The R32 board must not allow the same team to be assigned to more than one R32 slot.

## User-visible behavior
- When a choice menu opens, teams already assigned to other R32 slots are not offered.
- The current value of the slot being edited remains available so the user can reopen a slot without losing the existing choice.
- Third-place menus use the same duplicate prevention rule.
- If a duplicate choice is somehow tapped, the save path is blocked defensively.

## Verification
Run:

```bash
python3 tools/verify_wc2026_prevent_duplicate_r32_menu_assignments_patch.py
python3 tools/verify_wc2026_bracket_tracker.py
make verify
```
