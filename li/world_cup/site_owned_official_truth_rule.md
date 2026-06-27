# Rule: Site-Owned Official Truth

The WC2026 Bracketeering site owns official tournament truth as versioned site data.

## Authority

The source of truth for official tournament state is stored in the site/repo, not in a Supabase Admin_/official bracket row.

Site-owned official truth includes:

- Round of 32 team occupants
- Knockout result winners
- Champion/result truth
- Scoring comparison truth for Player Standings
- Max Possible reachability truth

## Supabase boundary

Supabase may store player-owned data:

- authenticated player identity
- public player profile/display name
- player bracket picks
- joined player state

Supabase must not be the source of official R32 occupants or official tournament results.

Player standings are not stored as standings. Standings rows, rank, Score, and Max Possible are computed at read/render time from player picks plus site-owned official truth.

## Computed standings boundary

The system must not persist standings rows as a separate authority.

The following are computed, not stored:

- standings rows
- rank
- Score
- Max Possible

The only stored inputs are:

- player-owned picks in Supabase
- official truth in site data

## Removed authority

The old Admin_/official Supabase bracket-row authority is superseded.

Runtime and LI must not require:

- a Supabase `Admin_/official` row
- an Admin_ physical user ID as official truth authority
- `bracket_kind = official` as the canonical official-truth source
- official R32/results hydration from a Supabase row

## Site data rule

Official truth must be loaded from versioned site data under `site/data/current/`.

A later runtime implementation should introduce a clear site-owned official-truth data file and loader, then remove Supabase official-truth row loading.
