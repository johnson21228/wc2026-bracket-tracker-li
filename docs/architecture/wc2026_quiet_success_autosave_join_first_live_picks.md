# WC2026 Quiet Success Autosave for Join-first Live Picks

Joined players should experience persistence as live gameplay, not as a save workflow.

The player-facing model is:

Join → make picks → picks are live.

Successful autosaves are quiet by default. The UI may show “Saving…” while work is active and must show “Could not save — retrying” when a save fails. It should not persistently show “Picks saved,” because that reintroduces save-state thinking after the Save Picks / Load Saved controls were removed.
