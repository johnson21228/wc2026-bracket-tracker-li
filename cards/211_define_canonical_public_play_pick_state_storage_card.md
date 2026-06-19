# Card 211: Define Canonical Public-Play Pick-State Storage

## Intent

Define the canonical user bracket storage document that supports invite-ready public play while preserving local-only play.

## Scope

- Game 1 stores 64 picks.
- Game 2 stores 32 picks.
- Champion and third-place winner are explicit slots.
- Third-place winner is derived from the semifinal losers but stored as its own pick.
- The canonical shape is shared by localStorage, export/import, and future remote storage.

## Acceptance

- LI and architecture docs define the canonical shape.
- A verifier checks that public-play storage docs exist and mention 64/32 pick counts, third-place winner, local fallback, and site-running invariant.
- No runtime behavior changes are required by this card.
