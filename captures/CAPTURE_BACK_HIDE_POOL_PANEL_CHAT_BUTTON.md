# CAPTURE_BACK_HIDE_POOL_PANEL_CHAT_BUTTON.md

# Capture Back: Hide Pool Panel Chat Button

## Intent

The pool panel should not present a player-visible chat entry point until the chat behavior, broadcast path, storage boundary, and public-visibility rules are explicitly governed.

## Why this matters

Pool-chat is a different truth boundary than bracket picks, official results, group standings, and highlight links.  If a chat button is visible to players, the site implies that chat is supported, transmitted, and perhaps saved or shared.

That is not yet the intended public surface.


## Decision

Hide the chat button from the pool panel for now.

This is a surface-hygiene change, not a real-time chat implementation.


## Intended behavior

- Pool panel remains visible and usable.
- Players can still use the pool/bracket features that are already governed.
- The chat button is not shown.
- No new chat event broadcast, subscription, persistence, or Supabase write path is implied.
- If chat returns later, it should return behind an explicit contract for who can see messages, what is stored, how it is broadcast, and whether it is pool-only, public, or private.

## Safety boundary

The button should be treated as hidden, not as disabled-but-promised.  Hiding it keeps the public site from over-signaling a communication feature that is not yet part of the governed model.

## Verification expectation

After the runtime change is applied:

- `make verify` should pass.
- The pool panel should not show a chat button.
- There should be no new chat-storage or chat-broadcast behavior added as part of this change.

## Next safe patch

If the chat button already exists in the runtime markup, the preferred next patch is to remove or conditionally suppress the button at the pool panel render boundary, with a feature-test or verifier that chat does not appear in the pool panel.
