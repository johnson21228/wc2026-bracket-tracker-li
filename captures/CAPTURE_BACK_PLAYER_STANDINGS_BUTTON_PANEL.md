# Capture Back: Player Standings Button and Panel

## Target

Add a player-facing **Standings** button and panel to the Bracketeering Hub.

The primary purpose is participation visibility: players should be able to see who is in the pool before the full scoring/leaderboard model is finalized.

## Player-facing behavior

- The page chrome exposes a **Standings** button.
- Clicking **Standings** opens a floating panel above the game board.
- The panel is read-only.
- The panel shows participating players using public player names only.
- Emails are not displayed.
- The first read model may render local/mock participant rows while preserving the path to Supabase-backed participants later.

## Row fields

- Rank
- Player
- Group Points
- Knockout Points
- Tiebreaker Score
- Total

The tiebreaker score is shown next to knockout points so the late-stage comparison is easy to scan.

Example compact display:

- `KO 42 · TB 17`

## Sorting

Rows sort by:

1. Total points descending
2. Knockout points descending
3. Tiebreaker score descending
4. Public player name ascending as a stable fallback

## Empty states

- `Loading standings…`
- `No players yet`
- `Sign in to join the standings`
- `Standings unavailable`

## Architecture

Pages owns the Standings button, panel rendering, and interaction.

The standings panel is read-only and does not perform Supabase writes. A future store/repository seam may supply Supabase participant rows, but the panel itself must not scatter persistence calls through the controller.

Local anonymous play remains unchanged.
