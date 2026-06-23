#!/usr/bin/env python3
from pathlib import Path

targets = [
    Path("cards/279_join_first_live_picks_player_ui_card.md"),
    Path("captures/CAPTURE_BACK_JOIN_FIRST_LIVE_PICKS_PLAYER_UI.md"),
    Path("docs/architecture/wc2026_join_first_live_picks_player_ui.md"),
    Path("li/world_cup/join_first_live_picks_player_ui_rule.md"),
]

required_tokens = [
    "Join the game → picks are live → standings are available → player name can be edited",
    "Join button",
    "Standings button",
    "Profile button",
    "no Save Picks button",
    "no Load Saved button",
    "no storage mode UI",
    "no login/auth language",
    "picks are live automatically",
    "Join to enter standings.",
    "public player name",
    "canonical BracketDocument",
    "BracketStore seam",
    "SupabaseBracketStore",
    "Autosave should be debounced.",
    "Saving…",
    "Picks saved",
    "Could not save — retrying",
    "You already have picks saved. Use saved picks or keep this board?",
    "Anonymous local exploration remains possible before joining.",
]

errors = []

for target in targets:
    if not target.exists():
        errors.append(f"missing file: {target}")
        continue
    text = target.read_text()
    for token in required_tokens:
        if token not in text:
            errors.append(f"{target}: missing token: {token}")

for target in targets:
    text = target.read_text() if target.exists() else ""
    if "Save Picks and Load Saved are removed from the normal player flow." not in text:
        errors.append(f"{target}: missing explicit save/load removal acceptance criterion")
    if "Verification proves this is a Join-first player UI rule and not a persistence-contract rewrite." not in text:
        errors.append(f"{target}: missing non-rewrite verification boundary")

if errors:
    raise SystemExit("WC2026 Join-first live picks player UI verification failed: " + "; ".join(errors))

print("OK: WC2026 Join-first live picks LI captures Join, Standings, Profile, live autosave, and no save/load player UI.")
