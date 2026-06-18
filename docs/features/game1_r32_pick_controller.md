# Game 1 R32 pick controller

## Overview

Game 1 asks the player to project every Round of 32 slot before FIFA locks the official R32 board.

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
- local persistence
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
