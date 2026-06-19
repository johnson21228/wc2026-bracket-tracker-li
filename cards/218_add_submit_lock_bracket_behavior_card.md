# Card 218: Add Submit/Lock Bracket Behavior

## Intent

Make public-play picks contest-safe enough for invite use and ready for later shared pick visibility.

## Scope

- Submit bracket action
- `submitted_at` timestamp on account-backed bracket rows
- submitted state visible in UI
- normal client cannot edit a submitted bracket
- `locked_at` behavior by game cutoff
- local draft state remains distinct from account submitted/locked state

## Acceptance

- Submitted brackets are not editable through normal client flow.
- Draft brackets remain editable until submitted or locked.
- Local drafts remain clearly distinct from submitted account brackets.
- Supabase rows use `submitted_at` and `locked_at`; the site must not depend on the superseded `status`-only database target.
- Submitted or locked account rows can become readable to other signed-in users under the Card 215 RLS target when game rules allow shared views.
