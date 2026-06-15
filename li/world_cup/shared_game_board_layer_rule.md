# Shared Game Board Layer Rule

The bracket template is the reusable game board surface for both games.

Game 1: player chooses which team fills each official Round-of-32 slot.

Game 2: official Round of 32 is given, and the player selects winners through final champion.

The board should support multiple layers:
1. Bottom visual/background layer.
2. Gradient/readability wash.
3. Bracket board template.
4. Runtime title/banner/labels.
5. Runtime hotspots, picks, and winner state.

The board template is visual geometry. It should not own game state.
