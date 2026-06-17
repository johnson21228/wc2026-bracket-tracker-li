# Bracket Pick Finality Validation Rule

A stored bracket pick is not automatically valid simply because it exists.

A pick can remain final only if:

1. The stored team appears in no more than one independent R32 source slot.
2. Every downstream pick has all required upstream source picks.
3. A downstream pick is reachable from one of its immediate feeder picks.
4. Repeated appearances of a team are allowed only along a single advancement path.

The rendering layer should expose this as observed card state rather than silently assuming validity.
