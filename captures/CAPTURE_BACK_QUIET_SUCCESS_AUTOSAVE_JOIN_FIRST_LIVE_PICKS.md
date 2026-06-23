# Capture Back: Quiet Success Autosave for Join-first Live Picks

## Context

Bracketeering now uses a Join-first player model:

Join → make picks → picks are live.

The old player-facing Save Picks / Load Saved model has been removed. Joined players should not need to think about manual saving.

## Product correction

Successful autosave should be quiet by default.

## Runtime rule

- Before Join:
  - Do not show autosave success copy.
  - The board may remain temporary browser play.
- After Join:
  - Picks autosave live.
  - Do not persistently show “Picks saved.”
- During active save:
  - Show “Saving…” while a save is active.
- On save failure:
  - Show “Could not save — retrying.”
  - Retry remains automatic.
- Profile/Join panel:
  - Keep stable copy such as “Picks are live after joining.”
  - Do not expose Save/Load/manual persistence language.

## Acceptance

- No Save Picks / Load Saved UI returns.
- Joined picks still autosave through the canonical BracketDocument / BracketStore seam.
- Successful autosave is quiet.
- Error autosave state remains visible.
- `make verify` and `make pack` pass.
