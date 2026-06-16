# Capture Back — Open Apps After Apply Rule

## Summary

Captured a Workbench rule requiring the WC2026 app surfaces to be opened after Apply workflows.

## Why

The project now has two app surfaces whose visible behavior matters:

- Game 1: R32 selection game
- Game 2: seeded bracket game

Verification alone is not enough. The Workbench loop should end Apply steps by opening the app surfaces for human review.

## Added

- `li/repo/open_apps_after_apply_rule.md`
- `docs/workflows/open_apps_after_apply.md`
- `prompts/apply_overlay_terminal_workflow.md`
- `cards/056_capture_open_apps_after_apply_rule_card.md`
