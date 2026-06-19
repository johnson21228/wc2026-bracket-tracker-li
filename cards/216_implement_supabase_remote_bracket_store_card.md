# Card 216: Implement Supabase Remote Bracket Store

## Intent

Connect signed-in users to hosted bracket storage using the canonical pick-state document.

## Scope

- Supabase client setup
- auth session read/write
- save/load `game1` and `game2` bracket documents
- keep localStorage fallback
- no custom server

## Acceptance

- A signed-in user can save Game 1 and Game 2 pick states.
- A signed-in user can reload from another browser/device and recover picks.
- Anonymous local play still works.
