WB_SESSION:
Capture Groups And Flags From Images

Changed:
- Preserved uploaded images showing Groups A-F and Groups G-L with flags and team names.
- Derived normalized group/team data from the images.
- Added data files for groups and teams derived from the flag images.
- Added LI rule requiring a visible Groups section on the static HTML site.
- Added feature note, card, and prompt for implementing the Groups section.

Source artifacts:
- `source/images/group_draw_A_to_F_flags.png`
- `source/images/group_draw_G_to_L_flags.png`

Data added:
- `data/groups_from_flags_images.json`
- `data/teams_from_flags_images.json`

Decision captured:
- The site should have a Groups section.
- Groups should show flags and team names.
- The Groups section should support Game 1 picking, future standings, screenshots, and review.
- Image-derived data should be marked pending official verification.

Naming notes:
- South Korea normalized to Korea Republic.
- Ivory Coast normalized to Côte d’Ivoire.
- Iran normalized to IR Iran.
- Cape Verde normalized to Cabo Verde.
- DR Congo normalized to Congo DR.
- Turkiye normalized to Türkiye.
- Curacao normalized to Curaçao.

Files added:
- `li/world_cup/group_display_rule.md`
- `docs/features/groups_section_feature_note.md`
- `cards/009_capture_groups_and_flags_from_images_card.md`
- `prompts/add_groups_section_to_static_html.md`

Next:
- Apply this overlay.
- Later update the static HTML so Groups A-L appear as a first-class site section.
- Use this as part of Card 002 Game 1 picker.
