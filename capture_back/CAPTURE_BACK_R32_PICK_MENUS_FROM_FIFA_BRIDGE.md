# Capture Back — R32 pick menus from FIFA bridge

## Decision

Game 1 R32 pick menus should be driven by the FIFA slot logic/geometry bridge, not by hardcoded legacy menu slot rules.

## Why

The player is making a full projected Round of 32 before FIFA lock. Until group results are known, each slot should allow every team that can possibly occupy that FIFA slot.

## Rule

```text
1X      -> all teams in Group X
2X      -> all teams in Group X
3 ABCDF -> all teams from Groups A/B/C/D/F
```

## Boundary

This is pre-lock projection behavior.

It does not replace FIFA Annex C official third-place assignment after lock. That remains a later official-lock resolution layer.
