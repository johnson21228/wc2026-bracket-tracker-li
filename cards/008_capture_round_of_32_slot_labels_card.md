# Card 008 — Capture Round-of-32 Slot Labels

## Intent

Update the bracket data model and HTML so Round-of-32 slots show what kind of team belongs there before the official teams are known.

## Why

A slot is not just empty space.

It may mean:

- winner of a group
- runner-up of a group
- best third-place team from a defined group pool
- later official assignment

## Acceptance

- Add `li/world_cup/round_of_32_slot_label_rule.md`.
- Add `data/official_round_of_32_slot_rules.json`.
- Add slot schema.
- HTML bracket can display slot label before team is known.
- Once resolved, HTML displays team plus slot label.
- Slot labels and team assignments are captured back when changed.
