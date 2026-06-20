#!/usr/bin/env python3
"""Verify fail-closed Pages publish commands and live-data checks are wired."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(path: str, needles: list[str]) -> list[str]:
    text = (ROOT / path).read_text(encoding="utf-8")
    return [f"{path} missing {needle!r}" for needle in needles if needle not in text]


def main() -> int:
    errors: list[str] = []
    errors += require("Makefile", [
        "publish-pages:",
        "python3 tools/publish_pages_snapshot.py --strict --verify-live",
        "publish-pages-force:",
        "--force-redeploy",
        "check-pages:",
        "python3 tools/check_pages_publish_freshness.py",
        "verify_wc2026_fail_closed_pages_publish.py",
    ])
    errors += require("tools/publish_pages_snapshot.py", [
        "--verify-live",
        "--force-redeploy",
        "require_source_head_pushed",
        "assert_projected_files_match",
        "verify_live_data",
        "group_matches.json",
        "group_standings.json",
        "match_highlights.json",
        "Pages publish complete.",
    ])
    errors += require("tools/check_pages_publish_freshness.py", [
        "CRITICAL_JSON_PATHS",
        "canonical_hash",
        "check_canaries",
        "United States 2-0 Australia",
        "FAIL: live Pages critical JSON is stale or mismatched.",
    ])
    errors += require("li/repo/pages_publish_fail_closed_rule.md", [
        "main is the source of truth",
        "fail-closed",
        "live deployed JSON",
    ])
    errors += require("docs/dev/pages_publish_fail_closed_live_data.md", [
        "make publish-pages",
        "make check-pages",
        "make publish-pages-force",
    ])

    if errors:
        print("WC2026 fail-closed Pages publish verification failed:")
        for error in errors:
            print("-", error)
        return 1
    print("OK: WC2026 Pages publish is fail-closed and live-data verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
