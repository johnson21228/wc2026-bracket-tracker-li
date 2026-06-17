# Game 1 R16 Live Candidate Resolution Rule

A Game 1 R16 choice slot must resolve its candidate teams from the live upstream R32 picks.

The resolver must accept both logical ordinal feeder IDs and manifest match-leg IDs.

Example equivalence:

    L-R32-01 == R32-L-M1A
    L-R32-02 == R32-L-M1B

The UI must not show `Waiting for both R32 teams` when both upstream teams are already selected or rendered.
