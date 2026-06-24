# Card 1008: Capture Player Join Experience

## Purpose

Capture the intended Bracketeering player join experience after the first real-world email-link delivery failure.

## Decision

Google becomes the preferred player sign-in path.

Email remains as a fallback.

Local/browser play remains as the no-account escape hatch.

## Scope

This card captures the player-facing experience and architecture boundary. It does not redesign the database.

## Files

- `captures/CAPTURE_BACK_PLAYER_JOIN_EXPERIENCE.md`
- `docs/features/player_join_experience.md`
- `li/world_cup/player_join_experience_rule.md`
- `tools/verify_wc2026_player_join_experience.py`

## Acceptance

- Player-facing join copy is captured.
- Google, email, and local play paths are all preserved.
- Technical auth vocabulary is kept out of the player-facing join panel.
- Google-specific provider logic is not allowed to leak into pick-selection logic.
