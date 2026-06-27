#!/usr/bin/env python3
from pathlib import Path
import json


def main() -> int:
    errors = []

    truth_path = Path("site/data/current/official_truth.json")
    truth = json.loads(truth_path.read_text())
    picks = truth.get("picksBySlot", {})

    if not isinstance(picks, dict):
        errors.append("official_truth.json picksBySlot must be an object")
    else:
        non_r32_slots = sorted(slot_id for slot_id in picks if "-R32-" not in slot_id)
        if non_r32_slots:
            errors.append("official_truth.json contains non-R32 truth picks: " + ", ".join(non_r32_slots))

        r32_slots = sorted(slot_id for slot_id in picks if "-R32-" in slot_id)
        if not r32_slots:
            errors.append("official_truth.json should keep known R32 occupant truth picks")

    capture = Path("captures/CAPTURE_BACK_OFFICIAL_TRUTH_R32_ONLY_SEED.md").read_text()
    rule = Path("li/world_cup/official_truth_r32_only_seed_rule.md").read_text()
    makefile = Path("Makefile").read_text()

    for token, label in [
        ("Official Truth R32-Only Seed", "capture title"),
        ("Round of 32 team occupants", "capture intent"),
        ("must not prefill winners", "rule prefill guard"),
    ]:
        if token not in capture and token not in rule:
            errors.append(f"missing {label}: {token}")

    if "python3 tools/verify_wc2026_official_truth_r32_only_seed.py" not in makefile:
        errors.append("Makefile verify target must run official truth R32-only seed verifier")

    if errors:
        print("Official truth R32-only seed verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: official truth currently contains only R32 occupant seed picks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
