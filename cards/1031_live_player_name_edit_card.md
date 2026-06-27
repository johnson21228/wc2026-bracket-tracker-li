# Card 1031: Live player name edit

## Change

Make signed-in Profile player-name editing a live edit box backed by Supabase.

## Acceptance

- Current player name is shown in the text field.
- Edits debounce and call `profileStore.saveProfile`.
- No `data-profile-save` button is required.
- Log out remains available.
