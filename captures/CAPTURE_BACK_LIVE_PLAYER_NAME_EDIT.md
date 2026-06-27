# Capture Back: Live Player Name Edit

## Intent

The signed-in Profile dialog should let a player edit their player name directly in a live text field.

## Runtime rule

When signed in, the Profile dialog shows the current player name in an input box. The player does not need a Save button. Edits debounce and write directly to Supabase through `profileStore.saveProfile`.

## Boundary

The signed-in Profile dialog should support only player-name editing and log out. It should not reintroduce local/exploration copy.
