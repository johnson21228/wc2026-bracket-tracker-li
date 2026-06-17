# Verify Anchored Knockout Choice Menu Assignment

Manual test:

1. Open Game 1.
2. Tap `L-R16-01` after its upstream R32 picks are available.
3. Confirm all tooltips close.
4. Confirm the menu appears beside `L-R16-01`.
5. Confirm the menu text indicates it assigns the bracket cell.
6. Choose one candidate team.
7. Confirm the chosen team appears in `L-R16-01`.
8. Repeat for another knockout cell if available.

Terminal verification:

    python3 tools/verify_wc2026_anchored_knockout_choice_menu_patch.py
    make verify
    make pack
