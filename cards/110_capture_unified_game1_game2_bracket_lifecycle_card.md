# Card 110 — Capture unified Game 1 to Game 2 bracket lifecycle

## Status
Reference / design intent only. No runtime behavior change.

## Why this card exists
Game 1 and Game 2 may not need to remain two separate visual surfaces. The same manifest-driven bracket board can support a longer lifecycle:

1. Predict Round of 32 slot occupants before FIFA officializes the bracket.
2. Allow knockout winner picks when both teams in a match are known.
3. Score the original Game 1 prediction layer when FIFA announces the official Round of 32.
4. Replace or overlay official FIFA Round of 32 truth while preserving the player's earlier predictions as evidence.
5. Continue servicing knockout-pick scoring as the bracket becomes Game 2.

## Design note
This card preserves the idea that Game 2 can become a later state of the same bracket board instead of an entirely independent board/page.

## Future implementation questions
- Should Game 2 remain a separate URL, or become a mode/state within Game 1?
- How should the UI show predicted R32 team vs official FIFA R32 team?
- When is a knockout pick allowed: only when both official teams are known, or also when both predicted teams are known?
- How should eliminated or invalidated pre-official picks remain visible?
- What data model preserves Game 1 evidence while allowing official truth to drive Game 2?

## Non-goals for this card
- Do not modify `site/game1/index.html`.
- Do not modify `site/game2/index.html`.
- Do not change scoring logic.
- Do not change manifests, SVG assets, or generated board geometry.
