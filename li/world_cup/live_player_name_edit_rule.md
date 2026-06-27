# Live player name edit rule

Signed-in Profile UI must render player-name editing as a live input field. The current display name is shown in the field. Player edits debounce and write directly to Supabase through `profileStore.saveProfile({ userId, displayName })`.

The Profile dialog must still allow log out. It must not require a separate Save button for player-name edits.
