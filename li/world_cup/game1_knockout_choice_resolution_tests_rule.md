# Game 1 knockout choice resolution test rule

Game 1 must be able to test whether a knockout winner-pick menu can resolve its choices from the bracket contestants that feed the tapped slot.

A valid knockout winner-pick menu resolves exactly two contestants:

- R16 slot → two assigned R32 teams.
- QF slot → two picked R16 winners.
- SF slot → two picked QF winners.

The test must fail closed when the resolved contestant set is empty, has only one contestant, or contains choices unrelated to the feeder match.

Group-eligibility menus are only for R32 assignment. Knockout winner-pick menus must use bracket feeder relationships.
