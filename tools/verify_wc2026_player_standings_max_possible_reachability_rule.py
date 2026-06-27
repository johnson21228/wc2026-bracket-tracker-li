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

li = read("li/world_cup/player_standings_max_possible_reachability_rule.md")
doc = read("docs/features/player_standings_max_possible_reachability.md")
card = read("cards/295_player_standings_max_possible_reachability_card.md")
site_rule = read("li/world_cup/site_owned_official_truth_rule.md")
combined = "\n".join([li, doc, card])

required = [
    "Max Possible",
    "site-owned official truth",
    "site-owned official results",
    "could still become site-owned official truth",
    "prior resolved site-owned official truth",
    "Score",
    "weight",
]

for token in required:
    if token not in combined:
        errors.append(f"Missing reachability rule token: {token}")

for forbidden in [
    "could still become `Admin_/official` truth",
    "prior resolved `Admin_/official` truth",
    "`Admin_/official` is the only source of elimination and scoring truth",
]:
    if forbidden in combined:
        errors.append(f"Reachability rule still depends on obsolete Admin_/official token: {forbidden}")

if "official truth in site data" not in site_rule:
    errors.append("site-owned official truth rule must define official truth in site data")

if errors:
    print("WC2026 Player Standings max possible reachability rule verification failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("OK: Player Standings Max Possible reachability uses site-owned official truth.")
