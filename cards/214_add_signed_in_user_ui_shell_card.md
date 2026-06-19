# Card 214: Add Signed-In User UI Shell

## Intent

Add the user-facing location for account and save-state presentation without requiring backend connectivity yet.

## Scope

- Signed-out state
- Anonymous local draft state
- Future signed-in user label
- Future save/load/submit controls
- Clear indication that local mode remains active until backend is configured

## Acceptance

- The account UI shell does not block local play.
- The site remains usable without backend config.
- The UI provides a stable place for later Supabase auth wiring.
