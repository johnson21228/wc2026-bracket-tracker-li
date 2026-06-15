# Game 1 Tap Chooser Playfield Rule

## Purpose

Game 1 should use the single-frame playfield as the main UI surface.

## Rule

Each Round-of-32 cell on the image should be a hit-testable tap/click target.

On tap:

```text
slot rule appears
allowed group choices appear
player selects one team
flag is placed into the slot
```

## Choice rule

Choices are constrained by the official slot label:

- `1A` means choose one team from Group A.
- `2B` means choose one team from Group B.
- `3 C/E/F/H/I` means choose one team from Groups C/E/F/H/I.

## Data rule

Each pick stores:

- slot id
- official rule
- team name
- abbreviation
- flag
- group
