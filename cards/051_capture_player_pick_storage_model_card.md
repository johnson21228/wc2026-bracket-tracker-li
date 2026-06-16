# Card 051 — Capture player pick storage model

## Intent

Capture the durable storage model needed before introducing user picks, multiplayer records, Game 1 scoring, and Game 2 tiebreaker comparison.

## Outcome

- Adds LI rule for separating draft state, durable player records, and official data.
- Adds storage model documentation.
- Adds a JSON schema for future pick records.
- Keeps current browser localStorage as draft state only.
