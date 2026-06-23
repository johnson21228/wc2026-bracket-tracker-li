# Card 1004: Add Bracketeering Workflow Easter Egg Panel

## Intent

Add a visible easter egg control adjacent to the existing map-style `i` info button.

The control opens a scrollable Bracketeering Workflow panel that presents:

- the Bracketeering Workflow infographic as a JPEG site asset
- pitch copy explaining the Workbench loop behind the site
- the core insight that Bracketeering evolves because code, intent, and verification stay aligned

## Download / Apply Pattern

This feature requires the Download / Apply pattern because the approved infographic is a binary JPEG generated outside the repo.

### Download step

The operator downloads the approved Bracketeering Workflow infographic JPEG from the ChatGPT conversation and places it here:

`~/Downloads/bracketeering_workflow_infographic.jpeg`

The apply step copies it into the durable Pages asset path:

`site/assets/visuals/bracketeering_workflow/bracketeering_workflow_infographic.jpeg`

The implementation must not proceed unless the JPEG exists locally.

### Apply step

After the JPEG is in place, apply the site changes:

- add the workflow panel module
- add the `WB` button beside the existing Info button
- add panel styling
- wire the panel from `site/js/app.js`
- add verifier coverage
- run `make verify`
- run `make pack`

### Verification rule

The verifier must fail if the JPEG is missing from the expected site asset path.

## Product meaning

Bracketeering is not only a World Cup bracket game. It is also a live example of a Workbench-driven product build.

The easter egg panel should expose that story for curious visitors without interrupting gameplay.

## UX target

Add a compact visible button next to the existing `i` button.

Preferred button label: `WB`

Behavior:

- button is visible beside the Info button
- clicking opens a modal-style overlay panel
- panel is scrollable
- panel displays the JPEG infographic
- panel displays pitch copy below or around the image
- panel has a close affordance
- Escape closes the panel
- clicking backdrop closes the panel
- existing Info panel still works
- existing sign-in/profile behavior still works
- no gameplay mechanics change
- no Supabase bracket persistence change

## Core sentence

The game evolves because the Workbench keeps code, intent, and verification aligned.

## Pitch copy to include

Bracketeering is not just a World Cup bracket site. It is a live example of a Workbench-driven product build: one conversation, one repo, one evolving game system, and a verification loop that turns decisions into durable product memory.

The Bracketeering workflow uses the Workbench as the product owner and continuity layer. The human sets direction, approves changes, and decides what becomes durable. The Intelligence Interface proposes implementation steps, edits the product surface, captures decisions, and updates verifiers. The terminal executes the durable part of the loop: code changes, data updates, verification, packaging, commits, pushes, and GitHub Pages publication.

What makes this workflow different is that the repo does not merely collect code. It collects intent. Every meaningful product decision becomes language infrastructure: cards, captures, docs, rules, prompts, data contracts, and verification scripts. Those scripts become executable memory. When the product changes, the Workbench does not just patch code; it refines the rules that keep the product aligned.

The Supabase profile step shows the loop clearly. At first, the repo blocked all Supabase writes because bracket persistence was not ready. Once public player names became real, the invariant evolved: profile writes were allowed through SupabaseProfileStore, while remote bracket writes remained blocked until the future SupabaseBracketStore. The verifiers caught the stale rule, and the Workbench updated the executable LI to match the new architecture.

That is the Bracketeering advantage: product intent, implementation, verification, and continuity move together.

Bracketeering is a bracket game, but the deeper product is the workflow: a repeatable way to build adaptive, data-driven, multi-user tournament software without losing control of the architecture as the system grows.

## Implementation boundary

This is presentation-only.

Do not change:

- pick behavior
- game mechanics
- group panel behavior
- Info panel behavior except adjacency of the new button
- Supabase auth/profile behavior
- Supabase bracket persistence

Remote bracket persistence remains blocked until the dedicated SupabaseBracketStore step.

## Implementation files

- `site/index.html`
- `site/css/app.css`
- `site/js/app.js`
- `site/js/workflow/BracketeeringWorkflowPanel.js`
- `site/assets/visuals/bracketeering_workflow/bracketeering_workflow_infographic.jpeg`
- `tools/verify_wc2026_bracketeering_workflow_easter_egg_panel.py`
- `Makefile`

## Verification target

Add a verifier that checks:

- JPEG infographic exists at `site/assets/visuals/bracketeering_workflow/bracketeering_workflow_infographic.jpeg`
- visible `WB` control exists adjacent to the Info button
- workflow panel module exists
- panel includes the core sentence
- panel references the JPEG asset
- panel body is scrollable
- panel has close behavior
- no pick gating or remote bracket persistence is introduced

## Acceptance criteria

- `make verify` passes
- `make pack` passes
- local browser test shows the `WB` button beside the `i` button
- clicking `WB` opens a scrollable panel
- panel displays the JPEG infographic
- panel displays the pitch copy
- closing the panel returns to the game board
- existing Info button still works
- signed-in public player name panel still works
