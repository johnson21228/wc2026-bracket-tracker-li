# Capture Back: Group Standings Panel LI

## Captured decision

Add Living Infrastructure for a group standings panel that can support current group tables, group matches, scores, match status, and optional highlight links.

## Important boundary

This CB defines the LI contract only. It does not implement the panel UI yet.

## Runtime direction

The site should consume normalized checked-in data, updated by WB/CB as games are played. The browser runtime should not depend on scraping ESPN, YouTube, or other third-party sources.

## Files added

- `cards/183_define_group_standings_panel_li_card.md`
- `li/world_cup/group_standings_panel_rule.md`
- `docs/features/group_standings_panel.md`
- `tools/verify_wc2026_group_standings_panel_li.py`
