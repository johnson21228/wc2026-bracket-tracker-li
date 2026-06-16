# Capture Back — Repair R32 Pick Card Display Label Language

## Problem

The R32 pick-card abbreviation rule was conceptually correct, but the UI still blurred the compact display value with a generic `Code` label in tooltip/details copy.

## Decision

Call the compact R32 pick-card value the `Card label` / `3-letter label` in user-visible UI. Continue using the data field `abbr` as the source for the compact card face.

## Result

- Compact card face is team-first but compact: flag + three-letter label.
- Tooltip/details gives the user the full name and explains the displayed label.
- The LI now separates full name, card label, and source/data code terminology.
