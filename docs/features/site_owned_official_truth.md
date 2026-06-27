# Site-Owned Official Truth

Official World Cup tournament truth is stored in the site/repo as versioned data.

This includes:

- R32 occupants
- official knockout winners
- final champion/result truth
- official truth used by standings scoring
- official truth used by Max Possible reachability

Supabase remains useful for player-owned data, but it is no longer the authority for official tournament truth.

Supabase stores player identity/profile and player bracket picks.

Player standings are computed, not stored. The site computes standings rows, rank, Score, and Max Possible from Supabase player picks and site-owned official truth.

The prior Admin_/official Supabase row model is superseded. The site should not depend on an Admin_ physical account or a special Supabase bracket row to know official R32 occupants or results.
