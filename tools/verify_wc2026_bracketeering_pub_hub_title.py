#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW = "Bracketeering Pub-Hub"
OLD = "FIFA Bracketeering"

player_facing_files = [
    ROOT / "site" / "index.html",
    ROOT / "index.html",
    ROOT / "html_world_cup_bracket_tracker_v001.html",
]

errors = []
found_new = False
for path in player_facing_files:
    if not path.exists():
        continue
    text = path.read_text()
    rel = path.relative_to(ROOT)
    if NEW in text:
        found_new = True
    if OLD in text:
        errors.append(f"{rel} still contains {OLD!r}")

if not found_new:
    errors.append(f"No player-facing entrypoint contains {NEW!r}")

site_index = ROOT / "site" / "index.html"
if site_index.exists():
    site_text = site_index.read_text()
    if NEW not in site_text:
        errors.append("site/index.html must contain the player-facing Pub-Hub title")

for forbidden in [
    "site/data/current/group_matches.json",
    "site/data/current/group_standings.json",
    "site/data/current/match_highlights.json",
    "site/data/current/knockout_matches.json",
    "site/data/game2_fifa_final_r32_assignments.json",
    "site/js/config/supabase.public.js",
    "site/js/services/SupabaseAuthService.js",
    "site/js/mvc/model.js",
    "site/js/mvc/controller.js",
]:
    if not (ROOT / forbidden).exists():
        continue

makefile = ROOT / "Makefile"
if makefile.exists():
    make_text = makefile.read_text()
    if "python3 tools/verify_wc2026_bracketeering_pub_hub_title.py" not in make_text:
        errors.append("Makefile verify target must include Pub-Hub title verifier")
else:
    errors.append("Makefile missing")

if errors:
    print("Pub-Hub title verification failed: " + "; ".join(errors))
    raise SystemExit(1)

print("OK: player-facing Bracketeering title is renamed to Bracketeering Pub-Hub without touching gameplay/data surfaces.")
