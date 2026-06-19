# Card 215: Add Supabase Backend Schema and RLS Setup

## Intent

Capture the inexpensive hosted backend setup for public play.

## Scope

- Supabase project setup notes
- `user_brackets` table SQL
- Row Level Security policies
- public anon key config pattern
- explicit warning to never commit service role keys

## Acceptance

- Backend setup docs are sufficient to create a test Supabase project.
- No secret keys are committed.
- Static frontend hosting remains the frontend posture.
