#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import sys
import time
import urllib.parse
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SVG = "assets/playfield/uniform_pick_card_gameboard.svg"
LIVE_URL = "https://johnson21228.github.io/wc2026-bracket-tracker-li/"


def run(cmd: list[str], *, check: bool = True, capture: bool = False) -> str:
    print("$ " + " ".join(cmd), flush=True)
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    if capture:
        output = result.stdout or ""
        if output.strip():
            print(output, end="" if output.endswith("\n") else "\n")
    if check and result.returncode != 0:
        raise SystemExit(result.returncode)
    return result.stdout or ""


def changed_paths() -> list[str]:
    out = run(["git", "ls-files", "-m", "-o", "--exclude-standard"], capture=True)
    return [line.strip() for line in out.splitlines() if line.strip()]


def commit_if_needed(message: str) -> None:
    paths = changed_paths()
    if not paths:
        print("No source changes to commit.")
        return

    run(["git", "add", "--", *paths])
    run(["git", "commit", "-m", message])


def show_from_gh_pages(path: str) -> str:
    return run(["git", "show", f"origin/gh-pages:{path}"], capture=True)


def verify_gh_pages_snapshot(main_sha: str) -> None:
    run(["git", "fetch", "origin", "gh-pages"])

    pages_build = show_from_gh_pages("pages-build.txt")
    index_html = show_from_gh_pages("index.html")
    view_js = show_from_gh_pages("js/mvc/view.js")

    errors: list[str] = []

    if main_sha[:12] not in pages_build and main_sha[:10] not in pages_build:
        errors.append(f"gh-pages pages-build.txt does not mention current main source {main_sha[:12]}")

    if EXPECTED_SVG not in index_html:
        errors.append(f"gh-pages index.html does not preload {EXPECTED_SVG}")

    if EXPECTED_SVG not in view_js:
        errors.append(f"gh-pages js/mvc/view.js does not render {EXPECTED_SVG}")

    if "assets/board/gameboard.svg" in index_html or "assets/board/gameboard.svg" in view_js:
        errors.append("gh-pages still references stale assets/board/gameboard.svg")

    if errors:
        print("Force publish verification failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("OK: gh-pages snapshot matches current main source and runtime SVG truth.")


def main() -> int:
    message = sys.argv[1] if len(sys.argv) > 1 else "Force publish WC2026 site snapshot"

    run(["python3", "tools/clean_repo_hygiene.py"])
    run(["make", "verify"])
    run(["make", "pack"])

    commit_if_needed(message)

    main_sha = run(["git", "rev-parse", "HEAD"], capture=True).strip()

    run(["git", "push", "origin", "main"])
    run(["python3", "tools/publish_pages_snapshot.py"])

    verify_gh_pages_snapshot(main_sha)

    cachebust_url = LIVE_URL + "?" + urllib.parse.urlencode({"cachebust": str(int(time.time()))})
    print(f"Opening {cachebust_url}")
    webbrowser.open(cachebust_url)

    run(["git", "status", "--short"])
    print("Force publish complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
