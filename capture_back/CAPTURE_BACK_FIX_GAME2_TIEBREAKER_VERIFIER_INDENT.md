# Capture Back — Fix Game 2 Tiebreaker Verifier Indentation

## Issue

The Game 2 official seed/tiebreaker LI overlay inserted verifier code at the wrong indentation level, causing:

```text
IndentationError: unexpected indent
```

## Fix

The verifier block is now reinserted inside `main()` using the same indentation as the success print, and the verifier is compiled as part of this repair script before returning.
