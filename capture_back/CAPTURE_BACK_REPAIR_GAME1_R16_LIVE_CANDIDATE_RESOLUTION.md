# Capture Back: Repair Game 1 R16 Live Candidate Resolution

## Summary

Game 1 R16 slots must resolve their candidate teams from the live upstream R32 picks.

The observed failure was `L-R16-01` showing `Waiting for both R32 teams` even when upstream visual pick cards were already present.

## Cause

The R16 source slots were expressed as `L-R32-01` / `L-R32-02`, while the rendered R32 pick cards may use manifest-style identifiers such as `R32-L-M1A` / `R32-L-M1B`.

## Decision

Add a live candidate resolver that maps between logical R32 ordinal slots and manifest R32 match-leg slots.

## Boundary

This patch repairs candidate resolution. It does not change scoring or the underlying bracket lifecycle model.
