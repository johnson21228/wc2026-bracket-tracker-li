# Game 2 Official Seed and Game 1 Tiebreaker

This note captures the intended product boundary between the two World Cup games.

## Product Model

Game 1 is a Round-of-32 qualification prediction game. Users predict who will occupy the Round-of-32 bracket slots.

Game 2 is a progressive knockout bracket game. It starts from a fixed Round-of-32 seed and asks users to pick the winners forward through the champion.

## Seed Sources

Game 2 may support these seed modes over time:

1. **Demo seed** — random or sample data used while building the site.
2. **Game 1 comparison seed** — user Game 1 picks translated into comparison metadata.
3. **Official seed** — FIFA/live-result Round-of-32 teams and slots, used as bracket truth.

## Game 1 as Tiebreaker

When official Round-of-32 data is available, Game 1 picks can be compared against the official slot/team data. Correct matches become visible in the Game 2 Round-of-32 rendering and may be used as a tiebreaker.

Example display:

```text
Game 1 R32 correct: 21 / 32
```

Example item annotation:

```text
🇺🇸 United States
✓ predicted in Game 1
```

or:

```text
🇩🇪 Germany
missed in Game 1
```

## Rule Boundary

Game 1 picks do not become bracket truth for Game 2 once the official/fixed Round-of-32 seed exists. They are comparison metadata only.

This keeps Game 1 valuable after qualification is known, while keeping Game 2 aligned to the real bracket.
