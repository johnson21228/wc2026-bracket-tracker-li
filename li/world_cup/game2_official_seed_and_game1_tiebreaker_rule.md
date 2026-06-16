# Game 2 Official Seed and Game 1 Tiebreaker Rule

Game 2 is the progressive knockout bracket game. Its bracket truth comes from a fixed Round-of-32 seed, not from mutable Game 1 picks.

## Rule

Game 2 MUST treat the Round of 32 as fixed seed data. During development this seed MAY be demo/random data. In production it SHOULD be official FIFA/live-result Round-of-32 data.

Game 1 picks MAY be translated into Game 2 only as comparison metadata. They MAY annotate the fixed Round-of-32 rendering and MAY contribute to a tiebreaker score.

Game 1 picks MUST NOT mutate the Game 2 bracket structure once an official or fixed Round-of-32 seed exists.

## Rendering Contract

Each fixed Round-of-32 item in Game 2 SHOULD render:

- team flag
- country/team name
- bracket slot
- optional Game 1 comparison status

The Game 1 comparison status SHOULD distinguish at least:

- correct slot/team match
- missed or different team
- no Game 1 pick available

## Tiebreaker Contract

Game 2 MAY compute a Game 1 tiebreaker score as the number of fixed Round-of-32 slot/team matches that were correctly predicted in Game 1.

The score SHOULD be rendered as:

```text
Game 1 R32 correct: N / 32
```

## Progressive Bracket Relationship

Game 2 winner picks proceed from the fixed Round-of-32 seed:

- R32 items are fixed inputs.
- R16/QF/SF/Final/Champion nodes are user winner picks.
- Future nodes become logically hot only when their feeder teams are known.
- Clearing or changing an upstream pick invalidates dependent downstream picks.

## Boundary

Game 1 remains its own prediction game: pick the 32.
Game 2 remains its own knockout game: pick the bracket from the fixed 32.
Game 1 correctness can travel into Game 2 as evidence and tiebreaker metadata, not as bracket authority.
