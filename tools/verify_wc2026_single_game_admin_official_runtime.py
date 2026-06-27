#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "li/world_cup/site_owned_official_truth_rule.md",
    "li/world_cup/editable_site_official_truth_json_rule.md",
    "site/data/current/official_truth.json",
    "tools/verify_wc2026_site_official_truth_runtime_source.py",
]

missing = [rel for rel in required_files if not (ROOT / rel).exists()]
if missing:
    print("Single-game Admin_/official runtime verification superseded by site-owned official truth runtime source:")
    for rel in missing:
        print(f"- missing {rel}")
    raise SystemExit(1)

runtime = (ROOT / "tools/verify_wc2026_site_official_truth_runtime_source.py").read_text(encoding="utf-8")
if "data/current/official_truth.json" not in runtime or "player picks remain Supabase-backed" not in runtime:
    print("Single-game Admin_/official runtime verification superseded by site-owned official truth runtime source: replacement runtime verifier is not protecting site-owned official truth source")
    raise SystemExit(1)

print("OK: Single-game Admin_/official runtime verifier superseded by site-owned official truth runtime source.")
