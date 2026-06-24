# Capture Back: Bracketeering Player Join Experience

## Context

A real-world Bracketeering join test failed because a player did not receive the email sign-in link, even after checking spam.

This exposed that an email-first player experience is too fragile for normal users because it depends on the Supabase → SMTP/Postmark → DNS → recipient mail-provider chain.

## Product decision

Define the intended player experience around a simple join flow:

1. Primary: Continue with Google
2. Fallback: Email me a sign-in link
3. Escape hatch: Play locally on this browser

This is a player-experience decision, not a database redesign.

## Desired first-visit experience

When a player opens the Bracketeering Pages link, they should see the game board and a clear join panel.

Target copy:

- Join Bracketeering
- Continue with Google
- or
- Email me a sign-in link
- Play locally on this browser

## Google path experience

The player clicks “Continue with Google”.

Expected flow:

1. Player is redirected to Google.
2. Player chooses their Google account.
3. Google returns the player to the Bracketeering site.
4. Bracketeering detects the Supabase session.
5. The board shows that the player is signed in.
6. Picks can now be saved under that player identity.

The player should experience this as:

Open link → Continue with Google → return to board → make picks

The player should not need to understand Supabase, Postmark, DNS, OAuth, callback URLs, or database persistence.

## Signed-in board state

After sign-in, the board should show simple player-facing status such as:

- Signed in
- Picks will be saved

or:

- Welcome back
- Loaded your bracket

The board interaction should remain the same:

Click a slot → choose a team → pick advances → board updates

The only difference is that the player now has a durable identity behind the bracket.

## Returning player experience

When the player returns later to:

https://johnson21228.github.io/wc2026-bracket-tracker-li/

The site should check for an active Supabase session.

If a session exists:

- show the board
- show signed-in state
- load that player’s bracket when remote persistence is active

If no session exists:

- show the join panel again
- offer Continue with Google
- offer email fallback
- offer local/browser play

## Email fallback experience

Email sign-in remains available for players who do not want to use Google.

However, email should no longer be the primary path because it is vulnerable to delivery failures, spam filtering, Postmark approval limits, domain authentication issues, and recipient-provider blocking.

## Local play experience

“Play locally on this browser” remains available.

Expected local-play copy:

No account needed.
Your picks are saved only on this browser.
Use Google if you want saved play across visits/devices.

This path is useful for:

- demos
- cautious users
- early testing
- players who do not want to authenticate yet

## Architecture boundary

The join experience must preserve the existing Bracketeering architecture:

- GitHub Pages owns View and Controller behavior.
- Supabase Auth proves identity.
- Supabase/Postgres provides durable Model persistence later.
- The game board should not contain Google-specific pick logic.
- Game logic should consume a generic signed-in user/session state.
- The auth method should remain behind the site-owned auth/store seam.

## Player-facing language

Use simple game language.

Prefer:

- Continue with Google
- Email me a sign-in link
- Play locally on this browser
- Picks will be saved
- Loaded your bracket

Avoid exposing technical language such as:

- OAuth provider
- Supabase session
- Postmark delivery
- callback URL
- RLS
- JWT
- auth metadata

## Acceptance criteria

- The player can see Google as the first sign-in option.
- The player can still use email as a fallback.
- The player can still play locally without signing in.
- The player can return from Google sign-in to the Bracketeering board.
- The board clearly indicates signed-in or local-play state.
- Player-facing copy explains whether picks are saved remotely or only locally.
- No Google-specific code is embedded directly in pick-selection logic.
- The game board interaction remains unchanged after sign-in.
- The experience feels like joining a bracket game, not configuring an account.
