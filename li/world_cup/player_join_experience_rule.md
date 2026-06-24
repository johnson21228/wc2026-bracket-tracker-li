# Bracketeering Player Join Experience Rule

The Bracketeering join experience must present Google as the preferred real-user sign-in path, email as fallback, and local/browser play as the no-account escape hatch.

## Rule

Player-facing auth language must be simple game language.

Use:

- Continue with Google
- Email me a sign-in link
- Play locally on this browser
- Picks will be saved
- Loaded your bracket

Avoid exposing implementation language in the player join panel:

- OAuth provider
- Supabase session
- Postmark delivery
- callback URL
- RLS
- JWT
- auth metadata

## Boundary

Google-specific provider code belongs behind the site-owned auth/store seam.

Pick-selection controller code must not directly reference Google-specific provider behavior.
