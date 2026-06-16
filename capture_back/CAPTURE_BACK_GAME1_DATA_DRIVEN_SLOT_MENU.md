# Capture Back — Game 1 Data-Driven Slot Menu

Game 1 now has a clearer boundary between data/rules and UI.

The chooser menu must be driven by module-owned data:

- 32 R32 slot rules from `site/data/game1_r32_slot_menu_rules.json`
- 48 teams and flags from `site/data/teams_from_flags_images.json`
- group structure from `site/data/groups_from_flags_images.json`

The browser page loads a generated bundle:

```text
site/data/game1_data_bundle.js
```

This avoids browser `fetch()` problems when reviewing locally with `open site/game1/index.html`, while removing the large hidden `SLOT_RULES` and `GROUPS` literals from the HTML page.

The LI boundary is:

```text
Tournament Data owns teams/groups/flags.
Qualification Rules owns R32 slot eligibility.
Game 1 owns applying the rules to player picks.
UI Surface owns rendering and interaction only.
```
