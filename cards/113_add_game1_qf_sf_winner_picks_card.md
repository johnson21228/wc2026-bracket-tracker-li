# Card 113 — Add Game 1 QF/SF winner picks

## Intent
Extend the Game 1 long-lived bracket workspace beyond R16 winner picks so the same board can support QF and SF winner picks once their feeding slots have resolved teams.

## Rule
QF and SF choice menus are governed by bracket adjacency. A slot may offer a choice menu only when both of its immediate source slots have winners.

## Runtime Scope
- Add QF winner-pick targets fed by paired R16 winner picks.
- Add SF winner-pick targets fed by paired QF winner picks.
- Store QF/SF advancement picks separately from R32 assignment picks and R16 winner picks.
- Do not change Game 2.

## Verification
- Game 1 defines QF/SF advancement source-slot rules from the uniform SVG manifest.
- QF sources are R16 slots.
- SF sources are QF slots.
- Menus show exactly two resolved source teams.
