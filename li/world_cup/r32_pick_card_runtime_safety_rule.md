# R32 Pick Card Runtime Safety Rule

R32 pick-card rendering is a visual layer over an already-valid pick state. A typography, tooltip, or card-fit change must not break pick loading, slot mapping, or filled-card rendering.

## Canonical term

The thing displayed in a filled Round of 32 bracket slot is an **R32 pick card**. More precisely, it is a **slot occupant card**: a team-first visual occupant for a board-defined R32 slot.

## Runtime boundary

The board slot rectangle remains the geometry authority. The pick card must fit that rectangle. But CSS/font changes must not mutate:

- pick state
- slot ids
- slot rules
- menu eligibility
- team data
- data bundle loading
- click/tap handlers

## JavaScript safety

Generated display helpers must not insert raw newline characters inside JavaScript string literals. Team-name line breaking should be handled by CSS wrapping, soft break characters, or escaped strings that preserve valid JavaScript syntax.

A card typography patch must preserve a valid Game 1 page script. If the page script breaks, picks disappear and the app is considered failed even if static verification passes.

## Verification expectation

A verifier for R32 pick-card rendering should check that:

- the Game 1 page still contains the pick rendering function/path
- pick-card DOM construction still occurs
- no raw newline-bearing JavaScript display-name literals were introduced
- card CSS can change card appearance without removing pick rendering
