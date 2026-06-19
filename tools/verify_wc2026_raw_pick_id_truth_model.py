#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

REQUIRED_TEXT = {
    Path("captures/CAPTURE_BACK_PICK_ID_TRUTH_MODEL.md"): [
        "pickId is truth.",
        "visual slot is projection.",
        "UI geometry may change.",
        "pickId must not change.",
        "site/data/model/canonical_pick_ids.json",
    ],
    Path("li/world_cup/raw_pick_id_truth_rule.md"): [
        "Raw pick storage must be keyed by durable semantic pick IDs",
        "LocalStorage and future RemoteBracketStore must persist raw pick-state records keyed by `pickId`",
        "Game 1 must initialize 64 stable raw pick IDs",
        "Game 2 must initialize 32 stable raw pick IDs",
    ],
    Path("docs/architecture/wc2026_raw_pick_id_truth_model.md"): [
        "Raw pick state",
        "Projection/UI state",
        "Game 1 expected total: 64 raw pick IDs",
        "Game 2 expected total: 32 raw pick IDs",
        "pickId -> sitePickId",
    ],
    Path("cards/221_define_raw_pick_id_truth_model_card.md"): [
        "Card 221",
        "pickId is truth.",
        "Previous CB governance and empty pick-state capture anchors still exist",
    ],
    Path("prompts/implement_raw_pick_id_truth_model.md"): [
        "site/data/model/canonical_pick_ids.json",
        "64 stable raw pick IDs for Game 1",
        "32 stable raw pick IDs for Game 2",
    ],
}

PREVIOUS_ANCHORS = [
    Path("captures/CAPTURE_BACK_CB_GOVERNANCE.md"),
    Path("captures/CAPTURE_BACK_EMPTY_PICK_STATE_STORAGE_MODEL.md"),
    Path("li/repo/capture_back_governance_rule.md"),
    Path("li/world_cup/canonical_pick_state_storage_model_rule.md"),
    Path("docs/architecture/wc2026_canonical_pick_state_storage_model.md"),
    Path("cards/220_enforce_capture_back_governance_card.md"),
    Path("cards/212_route_local_storage_through_canonical_pick_state_card.md"),
]

EXPECTED_HISTORY_SECTIONS = [
    "CB-Refs:",
    "Cards:",
    "Verification:",
    "History intent:",
]


def fail(msgs):
    print("WC2026 raw pick ID truth model verification failed:")
    for msg in msgs:
        print(f"- {msg}")
    sys.exit(1)


def main():
    errors = []

    for path, needles in REQUIRED_TEXT.items():
        if not path.exists():
            errors.append(f"missing {path}")
            continue
        text = path.read_text()
        for needle in needles:
            if needle not in text:
                errors.append(f"{path} missing expected text: {needle}")

    for path in PREVIOUS_ANCHORS:
        if not path.exists():
            errors.append(f"previous CB/governance anchor missing: {path}")

    root_cb = sorted(Path(".").glob("CAPTURE_BACK_*.md"))
    if root_cb:
        errors.append("root Capture Back files are forbidden: " + ", ".join(str(p) for p in root_cb))

    try:
        log_body = subprocess.check_output(
            ["git", "log", "-3", "--format=%B%n---END-COMMIT---"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except Exception as exc:
        errors.append(f"could not inspect recent git history: {exc}")
        log_body = ""

    if log_body:
        for section in EXPECTED_HISTORY_SECTIONS:
            if section not in log_body:
                errors.append(f"recent git history missing CB history section: {section}")
        # Older anchor captures are verified by PREVIOUS_ANCHORS above.
        # Do not require them to remain in the last three commits forever; that
        # makes the verifier fail as normal new work advances repo history.

    if errors:
        fail(errors)

    print("OK: WC2026 raw pick ID truth model is captured and previous CB history anchors have not drifted.")


if __name__ == "__main__":
    main()
