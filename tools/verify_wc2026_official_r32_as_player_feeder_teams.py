#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    ROOT / "captures/CAPTURE_BACK_OFFICIAL_R32_AS_PLAYER_FEEDER_TEAMS.md",
    ROOT / "docs/features/official_r32_as_player_feeder_teams.md",
    ROOT / "li/world_cup/official_r32_as_player_feeder_teams_rule.md",
    ROOT / "cards/287_official_r32_as_player_feeder_teams_card.md",
]

REQUIRED_DOC_TOKENS = [
    "The existing bracket already understands how picking works",
    "The only change is the source of selected teams for R32 slots",
    "Official R32 occupants replace player-authored R32 picks",
    "The bracket’s existing feeder graph remains authoritative",
    "old R32 selected-team source: player pick",
    "new R32 selected-team source: Admin_/official truth",
    "every R32 display slot resolves its selected team from Admin_/official truth",
    "normal players cannot author, overwrite, or unlock R32 occupants",
    "every R16 winner slot receives its choices from its two R32 feeder slots",
    "every later-round winner slot receives its choices from prior-round player winners, as before",
    "player picking begins at R16",
    "not a new bracket game",
]


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    for path in DOCS:
        require(path.exists(), f"Missing required CB artifact: {path.relative_to(ROOT)}", errors)
        if path.exists():
            text = path.read_text()
            for token in REQUIRED_DOC_TOKENS:
                require(token in text, f"{path.relative_to(ROOT)} missing token: {token}", errors)

    model = (ROOT / "site/js/mvc/model.js").read_text()
    controller = (ROOT / "site/js/mvc/controller.js").read_text()

    require("selectedTeam" in model, "model.js must preserve selectedTeam resolution.", errors)
    require("officialTeam" in model, "model.js must preserve officialTeam resolution.", errors)
    require("getChoices" in model, "model.js must preserve getChoices(slotId) as the bracket choice path.", errors)
    require("dependencyMap.get(slotId)" in model, "model.js must preserve dependencyMap feeder lookup for downstream slots.", errors)
    require("teamForFeederPath" in model, "model.js must preserve feeder-team resolution.", errors)
    require("selectedTeam(sourceSlotId)" in model or "selectedTeam(feederId)" in model,
            "model.js must preserve selectedTeam use from feeder/source slots.", errors)
    require("pickable: choices.length > 0" in model,
            "model.js must preserve pickability based on resolved choices.", errors)
    require(
        "adminOfficialEditorActive" in controller,
        "controller.js must preserve Admin_/official editor detection.",
        errors,
    )

    if errors:
        print("Official R32 as player feeder teams verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: Official R32 occupants are captured as the R32 selected-team source for existing bracket propagation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
