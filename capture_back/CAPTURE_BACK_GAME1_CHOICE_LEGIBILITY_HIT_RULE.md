# Capture Back — Game 1 Choice Legibility and Hit-Rule Integrity

This capture adds Living Intent and implementation changes so Game 1 chooser rows are readable and R32 hit targets continue to show the correct rules.

## Captured decisions

- Player-facing chooser rows must not concatenate country name and metadata.
- Team name, abbreviation, and group label are separate UI parts.
- Hidden implementation labels may remain available for verification, but should not be relied on as player-facing UI.
- R32 menu choices must be derived from the selected slot rule.
- Third-place slots must use their explicit group pools.

## Verification

Adds a verifier for chooser markup/CSS and representative R32 rule-to-group mappings.
