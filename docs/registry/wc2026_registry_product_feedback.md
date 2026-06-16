# WC2026 Registry Product Feedback

## Source Workbench

`wc2026-bracket-tracker-li`

## Feedback type

Workbench Registry / Workbench Product improvement signal.

## Observed issue

Accepted behaviors regressed when later CB overlays replaced site pages or patched JavaScript without checking previously accepted behavior contracts.

## Product requirement

The Registry should track accepted capabilities for each Workbench and report impacted capabilities before a CB mutates files.

## Proposed Registry behavior

For each Workbench, maintain a list of accepted capabilities such as:

- `game1.layered_board_surface`
- `game1.visible_hit_targets`
- `game1.group_filtered_tap_menu`
- `game1.local_draft_storage`
- `game2.foundation_layers`
- `game2.official_seed_tiebreaker_rule`
- `repo.site_surface`
- `repo.hygiene_cleanup`

When a CB touches files associated with those capabilities, the Registry or verifier should require preservation evidence.

## Product Builder follow-up

Update the Workbench Product Builder and/or Registry dashboard roadmap to include:

1. accepted behavior contract files;
2. accepted capability registry entries;
3. CB impact analysis;
4. behavior-preservation verifier hooks;
5. cross-repo product feedback aggregation.
