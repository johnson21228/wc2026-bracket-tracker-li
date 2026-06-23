# Quiet Success Autosave Rule

For Join-first Bracketeering play, successful autosave is not a player-facing state.

Joined players make picks and those picks are live. The UI may expose active save and failure states, but successful saves should clear quietly rather than persistently showing “Picks saved.”

Allowed player-facing autosave states:
- Saving…
- Could not save — retrying

Forbidden persistent success state:
- Picks saved
