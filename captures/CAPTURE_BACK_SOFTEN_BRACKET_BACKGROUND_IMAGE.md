# Capture Back: Soften Bracket Background Image

## Intent

Make the Bracketeering background image more transparent so it is less busy behind the bracket.

## Why this matters

The knockout pub background image adds atmosphere, but it should not compete with the bracket as the primary reading surface. The bracket lines, team labels, pick states, result states, standings surfaces, and floating controls need to remain visually dominant.

## Decision

Soften the background image by lowering its visual opacity behind the bracket.

This should be a presentation-only change. It should not change bracket geometry, pick logic, data loading, standings, official results, Supabase behavior, or interaction rules.

## Intended behavior

- The same background image remains in use.
- The background appears more transparent / subdued.
- The bracket is easier to read.
- The board still has the pub atmosphere.
- No gameplay or data behavior changes.

## Suggested implementation boundary

Prefer changing the shared background presentation layer opacity in CSS, rather than editing the image asset itself.

A likely safe patch is to reduce the opacity of the knockout/pub background layer or its pseudo-element, then add or update a verifier that protects the lower-opacity presentation rule.

## Verification expectation

After the runtime patch is applied:

- `make verify` should pass.
- The bracket background image should still be present.
- The background should be visibly less busy behind the bracket.
- The change should be CSS/presentation-only.
