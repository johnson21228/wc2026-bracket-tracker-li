# Game 1 R32 pick controller

## Overview

Legacy note: this controller described the old player-authored R32 projection model. Current Bracketeering rules supersede that behavior: Admin_/official owns R32 occupant truth, and normal players do not project or assign R32 occupants.

The controller decides what is possible.

```text
site/js/controllers/Game1R32PickController.js
```

The board layer renders what the controller provides.

```text
site/js/board/R32PickMenuLayer.js
```

## Controller responsibilities

The controller owns:

- lifecycle gating
- slot candidate generation
- selection validation
- duplicate-team prevention
- legacy local persistence; current public R32 occupant truth must come only from Supabase Admin_/official
- pick-change events

## Candidate generation

```text
group-winner:
  all teams from the listed group

group-runner-up:
  all teams from the listed group

third-place-candidate-set:
  all teams from every listed candidate group
```

## Validation

A pick is valid only if:

- the slot is enabled
- the team is one of the slot candidates
- the team is not already picked in another R32 slot

## Persistence

The controller persists to:

```text
wc2026.game1.r32ProjectionPicks.v1
```

The persisted record includes:

```text
fifaSlotId
fifaLabel
qualifierKind
eligibleGroups
teamId
abbr
name
group
pickedAt
```
