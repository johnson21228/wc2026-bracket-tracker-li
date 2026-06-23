# Card 1007: Add player Standings button and panel target

## Intent

Add a player-facing **Standings** button and floating panel so the Bracketeering Hub reflects participation.

This is not the final scoring engine. The first version should show who is participating and preserve the path to a Supabase-backed read model.

## Runtime target

- Add a **Standings** button to fixed browser chrome.
- Open a read-only floating standings panel.
- Render public player names only.
- Do not expose email addresses.
- Show Group Points, Knockout Points, Tiebreaker Score, and Total.
- Show tiebreaker score next to knockout points as `KO n · TB n`.
- Sort by total, knockout, tiebreaker, then public player name.
- Provide loading, empty, signed-out, and unavailable states.

## Architecture target

- Pages owns rendering and interaction.
- The panel is read-only.
- No Supabase write calls are allowed inside the standings panel.
- Local anonymous gameplay remains unchanged.
- Supabase-backed participant rows can be added behind a read seam later.

## Verification

Add a verifier that confirms:

- **Standings** button exists in player-facing chrome.
- Standings panel opens/closes independently.
- Public player name is used instead of email.
- Tiebreaker score appears next to knockout points.
- Sorting is total, knockout, tiebreaker, name.
- Surface is read-only.
- No Supabase write calls exist inside the standings panel.
- `make verify` and `make pack` pass.
