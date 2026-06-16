# Middle Layer Image Geometry Source

The WC2026 gameboard currently uses a layered board model:

1. background atmosphere layer
2. shared middle-layer bracket geometry PNG
3. DOM slot/item/hit-target layer
4. interaction and pick state layer

The important product decision is that the middle-layer PNG currently defines the bracket geometry for both games.

## Why this matters
The PNG gives the player a stable visual gameboard. Game 2 bracket items should not float in a loose list; they should occupy the visible bracket boxes implied by the image.

## Current direction
Current source direction:

```text
shared bracket PNG
  -> captured slot geometry JSON
  -> bracket items and hit targets placed into slots
  -> pick and advancement logic
```

## Future direction
Future desired source direction:

```text
truth geometry JSON
  -> generated bracket PNG/SVG
  -> bracket items and hit targets placed into slots
  -> pick and advancement logic
```

## Required concepts

### boardAsset
The image asset currently defining visible board geometry.

### bracketSlot
A measured rectangular region on the board where a bracket item or hit target belongs.

### connectorEdge
A visual/logical connection from one or more source slots to a destination slot.

### bracketItem
The team/pick object occupying a bracket slot.

### advancement edge
The logical relationship that allows a selected bracket item to advance into a later slot.

## Game 2 implication
Game 2 should seed R32 teams by creating bracket items and placing them into R32 bracket slots measured from the shared middle-layer image.

The board should not render the seed as an unrelated list once slot geometry exists.
