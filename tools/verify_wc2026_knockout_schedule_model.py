#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"WC2026 knockout schedule model verification failed:\n- {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def jpeg_size(path: Path) -> tuple[int, int]:
    """Return JPEG dimensions without Pillow/PIL."""
    data = path.read_bytes()
    require(data[:2] == b"\xff\xd8", f"{path} is not a JPEG file")

    i = 2
    while i < len(data) - 1:
        if data[i] != 0xFF:
            i += 1
            continue

        marker = data[i + 1]
        i += 2

        # Standalone markers.
        if marker in (0xD8, 0xD9):
            continue

        require(i + 2 <= len(data), f"truncated JPEG segment in {path}")
        length = int.from_bytes(data[i : i + 2], "big")
        require(length >= 2, f"invalid JPEG segment length in {path}")

        # Start of frame markers that carry dimensions.
        if marker in {
            0xC0, 0xC1, 0xC2, 0xC3,
            0xC5, 0xC6, 0xC7,
            0xC9, 0xCA, 0xCB,
            0xCD, 0xCE, 0xCF,
        }:
            require(i + 7 <= len(data), f"truncated JPEG size segment in {path}")
            height = int.from_bytes(data[i + 3 : i + 5], "big")
            width = int.from_bytes(data[i + 5 : i + 7], "big")
            return width, height

        i += length

    fail(f"could not read JPEG dimensions for {path}")


def load_matches(path: Path) -> list[dict]:
    data = json.loads(path.read_text())

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        for key in ("matches", "knockout_matches", "match_updates"):
            value = data.get(key)
            if isinstance(value, list):
                return value

    fail(f"{path} must contain a list or a dict with matches/knockout_matches/match_updates")


def match_id_of(match: dict) -> str:
    for key in ("match_id", "id", "matchNumber", "match_number"):
        if key in match:
            return str(match[key])
    return ""


def has_any(match: dict, keys: tuple[str, ...]) -> bool:
    return any(match.get(key) not in (None, "", "TBD") for key in keys)


def main() -> None:
    knockout_json = ROOT / "site/data/current/knockout_matches.json"
    evidence_json = ROOT / "source/text/knockout_schedule_evidence_20260618.json"
    manifest_json = ROOT / "source/text/knockout_pub_calendar_background_manifest.json"
    source_image = ROOT / "source/images/wc2026_knockout_pub_calendar_background.jpeg"
    runtime_image = ROOT / "site/assets/board/knockout_pub_background.jpeg"

    required_paths = [
        knockout_json,
        evidence_json,
        manifest_json,
        source_image,
        runtime_image,
        ROOT / "li/world_cup/knockout_schedule_model_rule.md",
        ROOT / "docs/features/knockout_schedule_model.md",
        ROOT / "cards/198_capture_knockout_schedule_model_card.md",
        ROOT / "capture_back/CAPTURE_BACK_KNOCKOUT_SCHEDULE_MODEL.md",
    ]

    for path in required_paths:
        require(path.exists(), f"missing required knockout schedule/model file: {path.relative_to(ROOT)}")

    matches = load_matches(knockout_json)
    ids = {match_id_of(match) for match in matches}

    expected_ids = {str(i) for i in range(73, 105)}
    require(expected_ids.issubset(ids), "knockout_matches.json must include match IDs 73 through 104")
    require(len([match for match in matches if match_id_of(match) in expected_ids]) >= 32, "expected at least 32 knockout match records")

    by_id = {match_id_of(match): match for match in matches}

    for match_id in sorted(expected_ids, key=int):
        match = by_id[match_id]
        require(has_any(match, ("round", "stage")), f"match {match_id} missing round/stage")
        require(has_any(match, ("date", "match_date")), f"match {match_id} missing date")
        require(has_any(match, ("kickoff_local", "kickoffLocal", "local_time")), f"match {match_id} missing local kickoff")
        require(has_any(match, ("timezone", "time_zone")), f"match {match_id} missing timezone")
        require(has_any(match, ("kickoff_et", "kickoffET", "eastern_time")), f"match {match_id} missing Eastern kickoff")
        require(has_any(match, ("venue", "stadium")), f"match {match_id} missing venue/stadium")
        require(has_any(match, ("city", "host_city")), f"match {match_id} missing city")
        require(has_any(match, ("source_url", "source", "sourceUrl")), f"match {match_id} missing source evidence")

    require("103" in ids, "third-place match 103 must be present")
    require("104" in ids, "final match 104 must be present")

    source_size = jpeg_size(source_image)
    runtime_size = jpeg_size(runtime_image)

    require(source_size == (1536, 1024), f"source knockout image must be 1536x1024, got {source_size}")
    require(runtime_size == (1536, 1024), f"runtime knockout image must be 1536x1024, got {runtime_size}")
    require(source_image.read_bytes() == runtime_image.read_bytes(), "source and runtime knockout pub background images must match byte-for-byte")

    manifest_text = manifest_json.read_text()
    require("32 TEAMS" in manifest_text, "manifest must capture corrected 32 TEAMS chalkboard text")
    require("32 MATCHES" in manifest_text, "manifest must capture corrected 32 MATCHES chalkboard text")

    print("OK: WC2026 knockout schedule model and pub background are captured and verified.")


if __name__ == "__main__":
    main()
