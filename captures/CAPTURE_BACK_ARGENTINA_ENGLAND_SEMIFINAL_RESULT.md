# Capture Back — Argentina 2–1 England Semifinal Result

## Result

The official knockout-results history now records:

- Round: Semi-final
- Match number: 102
- Date: July 15, 2026
- England 1–2 Argentina
- Winner: Argentina

## Advancement

- Argentina advances into `FINAL-RIGHT` and will face Spain in the World Cup Final.
- England becomes the right-side participant in the third-place playoff against France.

## Truth handling

The result was appended to:

`site/data/official_knockout_results.json`

No earlier knockout result was replaced or rewritten.

## Verification

A focused verifier confirms:

- the score and winner;
- the semifinal slot pairing;
- Argentina’s advancement into `FINAL-RIGHT`;
- the existence of both quarterfinal feeder results and Spain’s semifinal result;
- the result remains the newest append-only entry.

## Capture fields

- WB_SESSION: 2026-07-15 Argentina–England semifinal result
- Changed: appended Argentina 2–1 England and advanced Argentina to the Final
- Sources: user-supplied result in the current Codex task
- Data affected: official knockout results and derived Final/third-place participants
- Scores affected: player semifinal, finalist, and reachability scoring derived at runtime
- Release: source workbench and distributable pack refreshed
- Unresolved: none
- Next: record the third-place playoff and Final when supplied
