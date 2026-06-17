# Game 1 Node knockout choice resolution tests rule

Game 1 knockout choice resolution must be runnable outside the browser.

A command-line test may use a minimal JavaScript runtime, but it must exercise the same installed resolver path that the browser page exposes for the Game 1 knockout choice menu.

Required invariant:

- R16 choice = exactly two assigned R32 contestants.
- QF choice = exactly two picked R16 winners.
- SF choice = exactly two picked QF winners.

The empty-set state is valid only when required feeder picks are actually missing. It must not appear because the app failed to resolve known contestants.
