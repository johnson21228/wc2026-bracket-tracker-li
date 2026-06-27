#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

def read(rel):
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")

li = read("li/world_cup/site_owned_official_truth_rule.md")
doc = read("docs/features/site_owned_official_truth.md")
card = read("cards/297_site_owned_official_truth_card.md")
capture = read("captures/CAPTURE_BACK_SITE_OWNED_OFFICIAL_TRUTH.md")
makefile = read("Makefile")
combined = "\n".join([li, doc, card, capture])

required = [
    "source of truth for official tournament state is stored in the site/repo",
    "Round of 32 team occupants",
    "Knockout result winners",
    "Supabase may store player-owned data",
    "Supabase must not be the source of official R32 occupants or official tournament results",
    "Player standings are not stored as standings",
    "Standings rows, rank, Score, and Max Possible are computed",
    "The system must not persist standings rows as a separate authority",
    "player-owned picks in Supabase",
    "official truth in site data",
    "Admin_/official Supabase bracket-row authority is superseded",
    "Official truth must be loaded from versioned site data under `site/data/current/`",
]

for token in required:
    if token not in combined:
        errors.append(f"missing site-owned official truth token: {token}")

if "python3 tools/verify_wc2026_site_owned_official_truth_li.py" not in makefile:
    errors.append("Makefile verify must include site-owned official truth LI verifier")

if errors:
    print("WC2026 site-owned official truth LI verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Site-owned official truth LI supersedes Supabase Admin_/official truth authority and keeps standings computed.")
