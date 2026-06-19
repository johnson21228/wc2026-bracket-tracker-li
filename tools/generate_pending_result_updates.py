#!/usr/bin/env python3
"""Generate a research queue for likely completed matches with missing results.

This tool reads the repo's checked-in group match data and writes a JSON artifact
under outputs/research/. It does not patch match data.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

DEFAULT_TIMEZONE = "America/New_York"
DEFAULT_SOURCE = Path("site/data/current/group_matches.json")
DEFAULT_OUTDIR = Path("outputs/research")
DEFAULT_LIKELY_COMPLETE_MINUTES = 150

FINAL_STATUSES = {"final", "ft", "fulltime", "full-time", "completed"}
MISSING_STATUSES = {"", "scheduled", "tbd", "postponed", "pending", "not_started", "pre"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write pending_result_updates_*.json for past likely-completed matches missing final results."
    )
    parser.add_argument("--source", default=str(DEFAULT_SOURCE), help="Path to group_matches.json")
    parser.add_argument("--outdir", default=str(DEFAULT_OUTDIR), help="Directory for generated JSON")
    parser.add_argument("--timezone", default=DEFAULT_TIMEZONE, help="IANA timezone for generatedAt and naive dates")
    parser.add_argument(
        "--likely-complete-minutes",
        type=int,
        default=DEFAULT_LIKELY_COMPLETE_MINUTES,
        help="Only include matches whose kickoff is at least this many minutes before now.",
    )
    parser.add_argument(
        "--now",
        default=None,
        help="Override current time for repeatable output, e.g. 2026-06-19T08:00:00-04:00",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Also print generated JSON to stdout.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing source file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def parse_now(value: str | None, timezone_name: str) -> datetime:
    tz = ZoneInfo(timezone_name)
    if value:
        parsed = datetime.fromisoformat(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=tz)
        return parsed.astimezone(tz)
    return datetime.now(tz)


def parse_kickoff(match: dict, timezone_name: str) -> datetime | None:
    tz = ZoneInfo(timezone_name)
    raw = match.get("kickoffLocal") or match.get("kickoffET")
    if raw:
        try:
            parsed = datetime.fromisoformat(str(raw))
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=tz)
            return parsed.astimezone(tz)
        except ValueError:
            pass

    date_value = match.get("kickoffDate")
    if date_value:
        try:
            return datetime.fromisoformat(f"{date_value}T00:00:00").replace(tzinfo=tz)
        except ValueError:
            return None
    return None


def has_final_score(match: dict) -> bool:
    status = str(match.get("status") or "").strip().lower()
    return status in FINAL_STATUSES and match.get("homeScore") is not None and match.get("awayScore") is not None


def is_missing_result(match: dict) -> bool:
    if has_final_score(match):
        return False
    status = str(match.get("status") or "").strip().lower()
    return (
        status in MISSING_STATUSES
        or match.get("homeScore") is None
        or match.get("awayScore") is None
        or status not in FINAL_STATUSES
    )


def missing_fields(match: dict) -> list[str]:
    fields: list[str] = []
    if match.get("homeScore") is None:
        fields.append("homeScore")
    if match.get("awayScore") is None:
        fields.append("awayScore")
    if str(match.get("status") or "").strip().lower() not in FINAL_STATUSES:
        fields.append("finalStatus")
    if not match.get("summary"):
        fields.append("summary")
    return fields


def scan_guardrail_hits(repo_root: Path, match_id: str) -> list[dict]:
    hits: list[dict] = []
    if not match_id:
        return hits

    candidate_paths = sorted((repo_root / "tools").glob("verify_wc2026*.py"))
    blocking_terms = (
        "should not be patched",
        "must not be patched",
        "should not be final",
        "must not be final",
        "blocked",
        "guardrail",
        "failed",
    )

    for path in candidate_paths:
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        if match_id not in text:
            continue

        lines = text.splitlines()
        contexts = []
        for index, line in enumerate(lines):
            if match_id in line:
                start = max(0, index - 2)
                end = min(len(lines), index + 3)
                contexts.append({
                    "line": index + 1,
                    "text": "\\n".join(lines[start:end]).strip(),
                })
        lower_text = text.lower()
        likely_blocking = any(term in lower_text for term in blocking_terms)
        hits.append({
            "path": str(path.relative_to(repo_root)),
            "likelyBlocking": likely_blocking,
            "contexts": contexts[:3],
        })
    return hits


def search_terms(home: str, away: str) -> list[str]:
    return [
        f"site:fifa.com World Cup 2026 {home} {away} result",
        f"site:espn.com 2026 FIFA World Cup {home} {away} result",
        f"site:foxsports.com/watch {home} {away} Extended Highlights 2026 FIFA World Cup",
        f"site:youtube.com {home} {away} highlights 2026 FIFA World Cup",
    ]


def make_candidate(match: dict, kickoff: datetime, repo_root: Path) -> dict:
    home = match.get("homeTeamName") or match.get("homeTeamId") or "home team"
    away = match.get("awayTeamName") or match.get("awayTeamId") or "away team"
    match_id = str(match.get("matchId") or "")
    guardrail_hits = scan_guardrail_hits(repo_root, match_id)
    classification = "RESEARCH_REQUIRED"
    if any(hit.get("likelyBlocking") for hit in guardrail_hits):
        classification = "GUARDRAIL_REVIEW_REQUIRED"

    return {
        "matchId": match.get("matchId"),
        "groupId": match.get("groupId") or match.get("group"),
        "kickoffLocal": match.get("kickoffLocal") or match.get("kickoffET"),
        "kickoffDate": match.get("kickoffDate"),
        "likelyCompletedBecause": f"Kickoff is before the research cutoff and at least {DEFAULT_LIKELY_COMPLETE_MINUTES} minutes before generatedAt unless overridden.",
        "homeTeamId": match.get("homeTeamId") or match.get("homeAbbr"),
        "homeTeamName": match.get("homeTeamName"),
        "awayTeamId": match.get("awayTeamId") or match.get("awayAbbr"),
        "awayTeamName": match.get("awayTeamName"),
        "currentStatus": match.get("status"),
        "currentHomeScore": match.get("homeScore"),
        "currentAwayScore": match.get("awayScore"),
        "currentSummary": match.get("summary"),
        "currentSourceProvider": match.get("sourceProvider"),
        "posterMatchId": match.get("posterMatchId"),
        "espnMatchId": match.get("espnMatchId"),
        "missingFields": missing_fields(match),
        "classification": classification,
        "guardrailNotes": [
            "Inspect result-specific verifier guardrails before patching.",
            "If any verifier blocks this matchId, classify WATCH or CONFLICT unless the task is to revise the guardrail.",
        ],
        "guardrailHits": guardrail_hits,
        "suggestedSearches": search_terms(str(home), str(away)),
        "evidence": [],
        "proposedPatch": None,
    }


def main() -> None:
    args = parse_args()
    repo_root = Path.cwd()
    source = Path(args.source)
    outdir = Path(args.outdir)
    tz_name = args.timezone
    now = parse_now(args.now, tz_name)
    cutoff = now - timedelta(minutes=args.likely_complete_minutes)

    data = load_json(source)
    matches = data.get("matches")
    if not isinstance(matches, list):
        raise SystemExit(f"Expected {source} to contain a top-level matches list")

    candidates = []
    skipped = {"futureOrInProgress": 0, "alreadyFinal": 0, "missingKickoff": 0}

    for match in matches:
        kickoff = parse_kickoff(match, tz_name)
        if not kickoff:
            skipped["missingKickoff"] += 1
            continue
        if kickoff > cutoff:
            skipped["futureOrInProgress"] += 1
            continue
        if not is_missing_result(match):
            skipped["alreadyFinal"] += 1
            continue
        candidates.append(make_candidate(match, kickoff, repo_root))

    payload = {
        "schemaVersion": 1,
        "generatedAt": now.isoformat(),
        "timezone": tz_name,
        "repo": "wc2026-bracket-tracker-li",
        "sourceFile": str(source),
        "purpose": "Research only matches that are likely completed but missing final results.",
        "rules": {
            "includeOnlyPastKickoffs": True,
            "likelyCompleteMinutesAfterKickoff": args.likely_complete_minutes,
            "includeOnlyMissingResults": True,
            "doNotPatchDirectly": True,
            "guardrailVerifiersWin": True,
        },
        "candidateCount": len(candidates),
        "skipped": skipped,
        "candidates": candidates,
    }

    outdir.mkdir(parents=True, exist_ok=True)
    out_path = outdir / f"pending_result_updates_{now.strftime('%Y%m%d_%H%M%S')}.json"
    serialized = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    out_path.write_text(serialized)
    if args.stdout:
        print(serialized)
    print(out_path)
    print(f"candidateCount={len(candidates)}")


if __name__ == "__main__":
    main()
