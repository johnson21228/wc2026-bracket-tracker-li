# Capture Back: Empty Pick-State Storage Model

## Intent

Refine the public multi-user play LI so every user bracket starts as a complete empty pick-state document rather than a sparse map of only completed picks.

## Decision

The canonical storage model must create complete empty documents for both games:

- Game 1: 64 explicit pick slots, all initialized empty.
- Game 2: 32 explicit pick slots, all initialized empty.

A missing slot is a storage/model defect. An empty slot is a valid draft value.

## Why

This makes local storage, export/import, future remote storage, save/load, submit validation, and eventual scoring simpler and safer:

- every expected slot always exists;
- empty means unpicked;
- completeness means no required empty slots;
- downstream UI does not need to infer missing slots;
- server storage can keep one stable JSON document per user per game.

## Site-running invariant

This CB does not introduce accounts, Supabase, submit/lock, or remote storage. It updates the LI and card plan so the next implementation keeps the current static/local site running while moving the storage foundation toward public play.
