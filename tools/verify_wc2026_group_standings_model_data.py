#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path.cwd()


def read_json(rel: str):
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"Missing required current data file: {rel}")
    return json.loads(path.read_text())


def require_contains(rel: str, text: str) -> None:
    path = ROOT / rel
    body = path.read_text()
    if text not in body:
        raise SystemExit(f"Missing required text in {rel}: {text}")


def main() -> int:
    standings = read_json("site/data/current/group_standings.json")
    matches = read_json("site/data/current/group_matches.json")
    highlights = read_json("site/data/current/match_highlights.json")

    groups = standings.get("groups", {})
    expected_groups = list("ABCDEFGHIJKL")
    if sorted(groups.keys()) != expected_groups:
        raise SystemExit(f"Expected groups A-L in group_standings.json, found {sorted(groups.keys())}")

    for group_id in expected_groups:
        entries = groups[group_id].get("entries", [])
        if len(entries) != 4:
            raise SystemExit(f"Group {group_id} should have 4 standings entries")
        ranks = [entry.get("rank") for entry in entries]
        if ranks != [1, 2, 3, 4]:
            raise SystemExit(f"Group {group_id} ranks should be [1, 2, 3, 4], found {ranks}")
        for entry in entries:
            for key in ["teamId", "abbr", "name", "played", "wins", "draws", "losses", "goalsFor", "goalsAgainst", "goalDifference", "points", "qualificationContext"]:
                if key not in entry:
                    raise SystemExit(f"Group {group_id} entry missing {key}: {entry}")

    third_place = standings.get("thirdPlaceTable", [])
    if len(third_place) != 12:
        raise SystemExit("thirdPlaceTable should contain one third-place row for each group A-L")
    if [entry.get("thirdPlaceRank") for entry in third_place] != list(range(1, 13)):
        raise SystemExit("thirdPlaceTable should have thirdPlaceRank 1 through 12")

    if standings.get("source", {}).get("provider") != "ESPN":
        raise SystemExit("group_standings.json source.provider should be ESPN")
    if "espn.com/soccer/standings/_/league/fifa.world" not in standings.get("source", {}).get("url", ""):
        raise SystemExit("group_standings.json should preserve the ESPN standings source URL")

    if not matches.get("matches"):
        raise SystemExit("group_matches.json should contain match rows")
    if highlights.get("highlights") != {}:
        raise SystemExit("match_highlights.json should start with an empty highlights map unless links are verified")

    require_contains("site/js/mvc/model.js", "currentStandings: \"data/current/group_standings.json\"")
    require_contains("site/js/mvc/model.js", "function getGroupStandings(groupId)")
    require_contains("site/js/mvc/model.js", "function getGroupContext(groupId)")
    require_contains("site/js/mvc/model.js", "function getThirdPlaceTable()")
    require_contains("site/js/mvc/model.js", "getMatchHighlights")
    require_contains("docs/features/group_standings_model_data.md", "A later CB can refresh these files")
    require_contains("capture_back/CAPTURE_BACK_GROUP_STANDINGS_MODEL_DATA.md", "browser runtime must not scrape ESPN")

    print("WC2026 group standings model data verification passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
