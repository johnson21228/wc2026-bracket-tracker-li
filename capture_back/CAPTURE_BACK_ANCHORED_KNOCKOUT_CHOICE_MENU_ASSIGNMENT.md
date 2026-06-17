# Capture Back: Anchored Knockout Choice Menu Assignment

## Summary

The knockout choice menu must be understood as an assignment surface for the bracket cell that opened it.

It is not a free-floating team menu.

## Decision

When a bracket cell opens a knockout choice menu:

- all tooltip surfaces close
- the menu appears adjacent to the opening bracket cell
- the menu records the opening cell as its assignment target
- selecting a team writes that team into the opening bracket cell
- the menu closes after assignment

## Product Rule

The choice menu is visually and logically attached to the bracket cell it will fill.

## Boundary

This patch repairs Game 1 knockout choice menu behavior. It does not change source data, scoring rules, or official bracket results.
