#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    config = Path("site/js/config/gameLocks.js").read_text()
    index = Path("site/index.html").read_text()
    controller = Path("site/js/controllers/Game1R32PickController.js").read_text()
    r32_layer = Path("site/js/board/R32PickMenuLayer.js").read_text()
    standings = Path("site/js/standings/PlayerStandingsSurface.js").read_text()
    makefile = Path("Makefile").read_text()

    require('GROUP_STAGE_PICKS_LOCK_AT = "2026-06-25T23:59:00-04:00"' in config,
            "Shared lock config must set Group Stage Picks lock to June 25, 2026 at 11:59 PM ET.", errors)
    require("function areGroupStagePicksLocked" in config and "GROUP_STAGE_PICKS_LOCK_AT_MS" in config,
            "Shared lock config must expose a reusable lock predicate.", errors)
    require("function groupStagePicksLockedMessage" in config and "Group Stage Picks are locked." in config,
            "Shared lock config must expose player-facing locked-picks copy.", errors)
    require("function playerResultsHiddenUntilLockMessage" in config and "Standings open after Group Stage Picks lock." in config,
            "Shared lock config must expose player-facing hidden-results copy.", errors)

    require("Group Stage Picks lock at 11:59 PM ET" in index,
            "Info panel must use Group Stage Picks lock language.", errors)
    require("you will not be able to change your Round of 32 picks" in index,
            "Info panel must explain Round of 32 picks become uneditable after lock.", errors)
    require("Group Stage points are used as the Bracketeering tiebreaker" not in index,
            "Removed tiebreaker sentence must stay removed from the info panel.", errors)

    require('from "../config/gameLocks.js"' in controller,
            "R32 pick controller must import the shared lock config.", errors)
    require("function isGroupStagePickOpen" in controller,
            "R32 pick controller must combine lifecycle state with Group Stage Picks lock state.", errors)
    require("return isGroupStagePickOpen(this.lifecycle);" in controller,
            "R32 pickability must use the shared Group Stage Picks lock gate.", errors)
    require("if (areGroupStagePicksLocked()) return groupStagePicksLockedMessage();" in controller,
            "Disabled reason must show Group Stage Picks locked copy after lock.", errors)
    require("if (areGroupStagePicksLocked()) return { ok: false, reason: groupStagePicksLockedMessage() };" in controller,
            "set-pick validation must fail after Group Stage Picks lock.", errors)
    clear_start = controller.find("clearPick({ fifaSlotId })")
    clear_section = controller[clear_start:clear_start + 280] if clear_start >= 0 else ""
    require("areGroupStagePicksLocked()" in clear_section and "ok: false" in clear_section,
            "clear-pick must fail after Group Stage Picks lock.", errors)
    require("const result = controller.clearPick" in r32_layer and "renderValidationMessage(popover, result)" in r32_layer,
            "R32 menu clear action must respect locked clear-pick failures.", errors)

    require('from "../config/gameLocks.js"' in standings,
            "Player standings surface must import the shared lock config.", errors)
    require("const resultsVisible = areGroupStagePicksLocked();" in standings,
            "Standings button state must be driven by Group Stage Picks lock state.", errors)
    require("const canOpen = joined && storageReady && resultsVisible;" in standings,
            "Standings button must open only after joined, storage-readable, and Group Stage Picks locked.", errors)
    require("button.hidden = !canOpen" in standings and "button.disabled = !canOpen" in standings,
            "Standings button must be hidden/disabled while results are hidden.", errors)
    require('button.classList.toggle("is-results-locked", joined && !resultsVisible)' in standings,
            "Standings button must track hidden-results state.", errors)
    require("if (!areGroupStagePicksLocked())" in standings and "playerResultsHiddenUntilLockMessage()" in standings,
            "Standings load/open paths must block before Group Stage Picks lock.", errors)
    require("function scheduleGroupStagePicksLockRefresh" in standings and "window.setTimeout" in standings,
            "Standings surface must schedule a refresh when the lock time is reached.", errors)
    require("python3 tools/verify_wc2026_group_stage_pick_lock_gate.py" in makefile,
            "Makefile verify must include the Group Stage Picks lock verifier.", errors)

    if errors:
        print("Group Stage Picks lock gate verification failed: " + "; ".join(errors))
        return 1

    print("OK: Group Stage Picks lock gates R32 editing and hides player standings/results until lock.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
