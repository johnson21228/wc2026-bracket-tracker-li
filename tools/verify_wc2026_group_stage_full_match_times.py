#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(msg: str) -> None:
    raise SystemExit(f"WC2026 group-stage full match time verification failed:\n- {msg}")


def require(cond: bool, msg: str) -> None:
    if not cond:
        fail(msg)


def load_matches(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("matches"), list):
        return data["matches"]
    fail(f"unsupported JSON shape: {path.relative_to(ROOT)}")


def has_time(match: dict) -> bool:
    for key in ("kickoffLocal", "kickoffET", "kickoff_local", "kickoff_et"):
        if match.get(key) not in (None, "", "TBD", "Time TBD"):
            return True
    return False


def key(match: dict) -> tuple[str, str]:
    return (str(match.get("homeAbbr") or match.get("homeTeamId") or "").upper(), str(match.get("awayAbbr") or match.get("awayTeamId") or "").upper())


def verify_file(path: Path, expected_count: int = 72) -> None:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    matches = load_matches(path)
    require(len(matches) == expected_count, f"{path.relative_to(ROOT)} must contain {expected_count} group-stage matches, got {len(matches)}")
    missing = [m for m in matches if not has_time(m)]
    require(not missing, f"{path.relative_to(ROOT)} has {len(missing)} matches missing kickoff time fields")
    missing_source = [m for m in matches if not m.get("timeSourceUrl")]
    require(not missing_source, f"{path.relative_to(ROOT)} has {len(missing_source)} matches missing timeSourceUrl")


def main() -> None:
    required = [
        ROOT / "source/text/group_match_time_evidence_20260618.json",
        ROOT / "li/world_cup/group_stage_full_match_time_rule.md",
        ROOT / "docs/features/group_stage_full_match_time_model.md",
        ROOT / "cards/199_capture_group_stage_match_times_card.md",
        ROOT / "capture_back/CAPTURE_BACK_GROUP_STAGE_MATCH_TIMES.md",
    ]
    for path in required:
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    evidence = json.loads((ROOT / "source/text/group_match_time_evidence_20260618.json").read_text())
    records = evidence.get("matchTimes", [])
    require(len(records) == 72, f"group_match_time_evidence_20260618.json must contain 72 matchTimes, got {len(records)}")
    require("espn.com/soccer/schedule/_/league/fifa.world" in evidence.get("sourceUrl", ""), "evidence must cite ESPN FIFA World Cup schedule page")

    verify_file(ROOT / "site/data/current/group_matches.json")
    verify_file(ROOT / "site/data/group_stage_matches_from_poster.json")
    if (ROOT / "data/group_stage_matches_from_poster.json").exists():
        verify_file(ROOT / "data/group_stage_matches_from_poster.json")

    # Visible problem cases from the group panel screenshot / discussion.
    checks = {
        ("JOR", "ALG"): "2026-06-22T23:00:00-04:00",
        ("ALG", "AUT"): "2026-06-27T22:00:00-04:00",
        ("JOR", "ARG"): "2026-06-27T22:00:00-04:00",
    }
    current = {key(m): m for m in load_matches(ROOT / "site/data/current/group_matches.json")}
    for pair, expected in checks.items():
        require(pair in current, f"missing visible check match {pair}")
        require(current[pair].get("kickoffET") == expected or current[pair].get("kickoffLocal") == expected, f"{pair} must use {expected}")

    print("OK: WC2026 full group-stage match times are captured and verified.")


if __name__ == "__main__":
    main()
