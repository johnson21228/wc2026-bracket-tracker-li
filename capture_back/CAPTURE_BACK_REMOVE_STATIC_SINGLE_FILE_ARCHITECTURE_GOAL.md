# Capture Back: Remove Static Single-File Architecture Goal

## Summary

The user corrected the previous bridge framing. The goal is not to keep a monolithic HTML property while modularizing. The goal is to remove that property and follow the modular MVC/TDD design identified in the inventory review.

## Decision

The WC2026 app may remain static-hostable, but no current LI should encourage the app to remain a page-concentrated implementation.

## Changes

- Add `li/world_cup/modular_mvc_tdd_source_rule.md`.
- Rewrite `li/world_cup/static_html_release_rule.md` as a static-hostable site release rule.
- Add `docs/architecture/wc2026_modular_mvc_tdd_source_boundary.md`.
- Add `cards/151_remove_static_single_file_architecture_goal_card.md`.
- Add `prompts/remove_static_single_file_architecture_goal.md`.
- Add `tools/verify_wc2026_modular_source_boundary.py`.
- Patch README/MAP/current-solution language away from static-first and monolithic HTML framing.
- Remove the prior `mvc_tdd_static_html_bridge_rule.md` if it exists.

## Lesson

Portability should not be allowed to become an architectural excuse for monolithic source.

The Workbench should preserve deployability and reviewability while making modular source, behavior tests, and clean boundaries the default path.
