# Pub hero header rule

The Game 1 hero header is product language, not runtime implementation copy.

The hero header must present the app as the pub game experience:

- eyebrow: `Footie FÜHN`
- main title: `Braketeering Pub`
- subtitle: `Scroll the game board below and make your picks.`
- utility actions: `Clear picks`, `Export picks`, and `Import picks`

The header may offer utility actions, but it must not own pick-state rules. Pick-state mutation remains model/controller-owned. Export/import must use an explicit JSON snapshot of the current pick state and must preserve validation/cascade behavior on import.
