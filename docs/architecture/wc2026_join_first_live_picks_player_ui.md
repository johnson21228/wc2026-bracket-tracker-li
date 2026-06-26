# Join-first live picks player UI

## Intent

Bracketeering’s player-facing account and persistence UI should be simplified.

The game is not presented as a login/save/load system.

The player model is:

Join the game → picks are live → standings are available → player name can be edited.

## Primary UI rule

The player-facing account/persistence surface has only three simple concepts:

1. Join
2. Standings
3. Profile

Controls:

- Join button
- Standings button
- Profile button

## Join button

Purpose:

- lets the player join the game
- establishes persistent player identity
- enables live pick persistence
- enables standings participation

Player-facing states:

- Join
- Joining…
- Joined
- Joined as {public player name}

After joining:

- no Save Picks button
- no Load Saved button
- no storage mode UI
- no login/auth language
- picks are live automatically

## Standings button

Purpose:

- opens the standings panel
- shows joined players
- uses public player names
- does not expose raw email

Before joining:

- the Standings button may be disabled, visually secondary, or show a join prompt
- copy should say: “Join to enter standings.”

After joining:

- the Standings button is enabled as a normal game feature

## Profile button

Purpose:

- lets the joined player edit their public player name
- does not expose raw email as player identity
- does not expose Supabase/Auth/storage implementation details

Profile panel focuses on:

- public player name
- joined status
- optional private account note only if needed

## Avoid

The normal player UI must avoid:

- Login
- Auth
- Save Picks
- Load Saved
- Remote store
- Local/remote
- Storage mode
- Manual persistence language

## Live picks rule

Once joined, picks are always live.

Every pick change autosaves through the canonical persistence boundary:

- canonical BracketDocument
- BracketStore seam
- SupabaseBracketStore for joined play

Autosave should be debounced.

Allowed status copy:

- Saving…
- Picks saved
- Could not save — retrying

These are status messages, not player commands.

## Conflict rule

If the player joins and an existing saved joined bracket conflicts with temporary browser picks, show one player-facing choice:

“Your saved joined bracket was loaded. Local draft picks are ignored for joined play.”

After that choice:

- picks return to live autosave behavior
- no ongoing save/load UI is shown

## Implementation targets

Likely implementation targets:

- `site/js/identity/SupabaseIdentitySurface.js`
- `site/js/identity/AccountSaveActionSurface.js`
- `site/js/standings/PlayerStandingsSurface.js`
- `site/js/services/SupabaseProfileStore.js`
- `site/js/mvc/controller.js`
- `site/js/mvc/model.js`
- related CSS and verifiers

## Acceptance criteria

1. Player-facing UI exposes Join, Standings, and Profile as the account/game participation controls.
2. Save Picks and Load Saved are removed from the normal player flow.
3. Joined players’ picks autosave.
4. Standings participation is tied to joined status.
5. Profile edits only the public player name.
6. Raw email is not used as public player identity.
7. Supabase/Auth/storage language is hidden from normal player UI.
8. Anonymous local exploration remains possible before joining.
9. Existing saved bracket conflicts are handled once with a clear player choice.
10. Verification proves this is a Join-first player UI rule and not a persistence-contract rewrite.


## Supersession note

The old saved-picks/current-board conflict choice is superseded. Joined play uses the Supabase saved bracket as authority. Local draft picks are ignored for joined play and must not be offered as an alternate board source.
