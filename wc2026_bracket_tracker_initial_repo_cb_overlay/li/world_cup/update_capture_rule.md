# Update Capture Rule

## Purpose

Capture Back is required after meaningful state changes.

Use CB after:

- results are entered
- standings change
- teams advance or are eliminated
- Game 1 scores change
- Game 2 scores change
- scoring rules change
- a new HTML release is created
- source data is corrected

## Required Capture Back fields

```text
WB_SESSION:
Changed:
Sources:
Data affected:
Scores affected:
Release:
Unresolved:
Next:
```

## Anti-drift rule

If the II is unsure which state is current, ask for the latest exported JSON, latest HTML release, or latest repo pack before updating.
