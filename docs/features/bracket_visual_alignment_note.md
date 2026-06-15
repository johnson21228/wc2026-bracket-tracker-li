# Bracket Visual Alignment Note

## Requirement

The bracket should align later rounds vertically with the matches that feed them.

A Round of 16 slot should sit visually between the two Round of 32 matches that produce it.

A Quarterfinal slot should sit between the two Round of 16 slots that produce it.

This makes the bracket easier to read and more screenshot-friendly.

## Problem to avoid

Do not let later rounds float in approximate locations.

That makes it difficult to see which matches feed which slot.

## Desired behavior

```text
R32-M1 ┐
       ├─ R16-S1
R32-M2 ┘

R32-M3 ┐
       ├─ R16-S2
R32-M4 ┘

R16-S1 ┐
       ├─ QF-S1
R16-S2 ┘
```

## First implementation

The first static HTML implementation can use a fixed bracket tree layout.

It does not need animated connectors. It just needs consistent vertical centering.
