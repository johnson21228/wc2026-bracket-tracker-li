# Card 048 — Capture Game 2 Official Seed + Game 1 Tiebreaker Rule

## Intent

Preserve the rule that Game 2 starts from a fixed Round-of-32 seed, while Game 1 picks can still travel forward as comparison and tiebreaker evidence.

## Decision

Game 2 bracket truth comes from fixed seed data. Game 1 picks may be imported only as metadata showing which Round-of-32 slot/team predictions were correct.

## Acceptance

- LI rule exists under `li/world_cup/`.
- Product note exists under `docs/rules/`.
- Capture Back exists under `capture_back/`.
- Verifier requires these milestone files.
- Rule states that Game 1 picks do not mutate Game 2 official/fixed bracket truth.
