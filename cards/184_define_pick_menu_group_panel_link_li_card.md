# Card 184 — Define pick-menu group panel link LI

## Intent

Make the pick menu a bridge from bracket picks to group context.

Any pick menu surface that presents group-qualified choices must collect group references together, show the group label for every grouped set of choices, and make that group label clickable/tappable so the user can open the group standings panel for that group.

## Why

Round-of-32 picking depends on group context. A user should not have to leave the pick flow to understand why a team is eligible, where it stands, or which group produced it.

The group standings panel becomes a reusable context surface that can be opened from any group label in the site, not just from one dedicated standings section.

## Files

- `li/world_cup/pick_menu_group_panel_link_rule.md`
- `docs/features/pick_menu_group_panel_link.md`
- `capture_back/CAPTURE_BACK_PICK_MENU_GROUP_PANEL_LINK_LI.md`
- `tools/verify_wc2026_pick_menu_group_panel_link_li.py`

## Verification

Run:

```bash
make verify
```

The verifier confirms that the LI rule, feature note, capture-back note, and Makefile verifier hook are present.
