# Verify Pages Review Pick Acceptance

Run:

```bash
python3 tools/verify_wc2026_pages_review_pick_acceptance_patch.py
python3 tools/verify_wc2026_bracket_tracker.py
make verify
make pack
```

Then push and re-run Pages.

Manual smoke test:

1. Open the GitHub Pages URL.
2. Tap a pickable bracket cell.
3. Choose a team.
4. Confirm the cell updates.
5. Reload the page.
6. Confirm the pick remains.
