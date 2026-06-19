# Capture Back: Raw Pick ID Truth Model

## Intent captured

Raw pick data must be a stable, user-owned record keyed by durable pick IDs. The board geometry and game projection model are related but must not be the storage truth.

## Decision

- `bracket_slots.json` and visual `sitePickId` values are projection/UI authorities.
- Raw persisted pick state is keyed by stable semantic `pickId` values.
- A user's raw record needs only the user/account identity, game identity, state metadata, and `picks[pickId]` values.
- The mapping from raw pick IDs to board slots is a projection layer, not the persistence authority.

## Required model split

```text
Raw pick state
  userId
  gameId
  status
  picks[pickId] = null | pickValue

Projection map
  pickId -> visual slot/sitePickId
  pickId -> candidate source
  pickId -> display/render location

UI/runtime
  reads projection map
  writes raw pick IDs through repository/storage
```

## Invariant

```text
pickId is truth.
visual slot is projection.
UI geometry may change.
pickId must not change.
```

## Commit-drift guard

This capture preserves the immediately previous CB governance/history shape. CB commits should remain discoverable by commit body sections:

```text
CB-Refs:
Cards:
Verification:
History intent:
```

The verifier added by this capture checks that the prior CB governance and empty pick-state anchors still exist and that recent commit history includes the CB history sections.

## Next implementation posture

The next implementation should introduce a canonical pick ID manifest before further localStorage/backend rewiring.

Proposed next file:

```text
site/data/model/canonical_pick_ids.json
```

The manifest should define 64 stable Game 1 pick IDs and 32 stable Game 2 pick IDs, and any projection map must reference those IDs rather than inventing storage identity from UI geometry.
