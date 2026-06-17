# Game 1 R16 Choice Menu Rules

Game 1 can grow from a Round of 32 slot-assignment game into a long-lived bracket workspace. In that lifecycle, R16 choices should be available once both teams feeding a Round of 16 match are known.

## Core rule

Each R16 slot is fed by exactly two R32 slots. The R16 menu must offer only those two teams.

Example:

```text
R32 slot A + R32 slot B -> R16 slot X
R16 slot X menu choices = [team in R32 slot A, team in R32 slot B]
```

This means the R16 menu is different from the R32 assignment menu.

- R32 menu: shows eligible teams based on group/third-place qualification rule.
- R16 menu: shows the two already-picked teams that lead into that R16 match.

## Locked condition

If either source R32 slot is empty, the R16 destination should not offer a winner menu. It may show a helpful status such as:

```text
Set both Round of 32 teams first.
```

## Storage separation

R16 picks must not overwrite the R32 assignment picks. They should live in a separate bracket-pick record keyed by R16 slot ID.

## Future extension

The same pattern should later apply to QF, SF, and Final Four picks:

```text
round N destination choices = two resolved winners from previous-round source slots
```

For now, this card only establishes R16 menu authority.
