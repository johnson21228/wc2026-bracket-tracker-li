# Game 1 R32 pick menu from FIFA bridge rule

Game 1 R32 pick menus must derive slot meaning from the FIFA logical slot order and the FIFA-to-board geometry bridge.

Rules:

- Do not hardcode playable R32 slot meaning in DOM order.
- Use `site/data/model/fifa_r32_logical_slot_order.json` for slot meaning.
- Use `site/data/geometry/game1_fifa_slot_geometry_map.json` to resolve board geometry.
- Use group/team data to populate pre-lock candidates.
- In pre-lock projection mode:
  - `group-winner` slots show all teams from the listed group.
  - `group-runner-up` slots show all teams from the listed group.
  - `third-place-candidate-set` slots show all teams from every listed group.
- Menus should only be enabled while Game 1 projection picking can be changed.
- Official post-lock third-place assignment remains governed by FIFA Annex C and is a separate layer.
