# Card 297: Site-Owned Official Truth

## Intent

Move official R32/results/scoring truth authority out of Supabase and into versioned site data.

## Acceptance

- LI states that official R32 occupants and official results are stored in the site/repo.
- Supabase is limited to player-owned identity/profile data and player bracket picks.
- Player standings are computed, not stored as standings rows.
- Admin_/official Supabase row authority is superseded.
- Conflicting LI is identified for removal or supersession.
- Runtime removal of Supabase official-truth row loading is treated as a follow-up implementation task.
