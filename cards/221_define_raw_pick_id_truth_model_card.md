# Card 221 — Define Raw Pick ID Truth Model

## Purpose

Make raw pick storage use durable semantic pick IDs while keeping visual board slots as projection/UI identifiers.

## Problem

The current board slot authority is useful for Game Projection and UI, but it has 61 visual slots and no game identity. It should not become the final raw pick-state storage truth.

## Decision

The user pick record should be keyed by stable `pickId` values.

```text
pickId is truth.
visual slot is projection.
UI geometry may change.
pickId must not change.
```

## Scope

- Preserve current site behavior.
- Add LI/docs/verifier for raw pick ID truth.
- Require future canonical pick manifest to define 64 Game 1 and 32 Game 2 stable pick IDs.
- Guard against drift from the previous CB governance commit shape.

## Non-goals

- Do not rewire runtime localStorage yet.
- Do not add backend auth/storage yet.
- Do not replace board geometry data.

## Acceptance

- `captures/CAPTURE_BACK_PICK_ID_TRUTH_MODEL.md` exists.
- `li/world_cup/raw_pick_id_truth_rule.md` states the pick ID truth invariant.
- `docs/architecture/wc2026_raw_pick_id_truth_model.md` explains raw state vs projection state.
- `tools/verify_wc2026_raw_pick_id_truth_model.py` passes.
- Previous CB governance and empty pick-state capture anchors still exist.
- Recent commit history includes CB-Refs / Cards / Verification / History intent sections.
