# Define WC2026 App Modules

Inspect the current WC2026 Bracket Tracker LI repo and evolve it toward clear app modules.

Focus on these boundaries:

- source evidence and provenance
- tournament data: 48 teams, 12 groups, flags, matches, standings, official results
- qualification rules: group winners, runners-up, best third-place ranking, R32 slot assignment
- Game 1: pre-knockout R32 qualifier prediction
- Game 2: fixed-seed knockout bracket prediction
- scoring and tiebreakers
- pixel-native board geometry
- UI surfaces and rendering
- local persistence/export/import
- verification and schema checks

Preserve current visible behavior while moving durable facts and rules out of inline page code.
