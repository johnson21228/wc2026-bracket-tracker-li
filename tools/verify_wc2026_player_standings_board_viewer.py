#!/usr/bin/env python3
from pathlib import Path


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def main():
    errors = []

    surface_path = Path("site/js/standings/PlayerStandingsSurface.js")
    css_path = Path("site/css/app.css")
    makefile_path = Path("Makefile")

    surface = surface_path.read_text()
    css = css_path.read_text()
    makefile = makefile_path.read_text()

    require("data-player-board-viewer-open" in surface,
            "Standings rows must expose a player board viewer open action.", errors)
    require("player-standings-player-button" in surface and "View picks" in surface,
            "Player standings names must have visible View picks action copy.", errors)
    require("data-player-board-viewer-panel" in surface,
            "Surface must create a full board viewer panel.", errors)
    require("player-board-viewer-panel" in surface,
            "Surface must use the board viewer panel class.", errors)
    require("Viewing ${row.publicPlayerName}'s picks" in surface,
            "Viewer title must identify whose picks are being viewed.", errors)
    require("Read-only" in surface,
            "Viewer must include read-only copy.", errors)
    require("Back to my board" in surface,
            "Viewer must include close/back affordance.", errors)
    require("data-player-board-viewer-scroll" in surface and "data-player-board-viewer-zoom" in surface,
            "Viewer must provide pan/zoom-oriented hooks.", errors)
    require("installBoardViewerDragPan" in surface,
            "Viewer must install local drag-pan behavior.", errors)
    require("BOARD_VIEWER_GEOMETRY_URL" in surface and "gameboard_manifest.json" in surface,
            "Viewer must use the board geometry manifest.", errors)
    require("BOARD_VIEWER_LINEWORK_URL" in surface and "uniform_pick_card_gameboard.svg" in surface,
            "Viewer must render board linework.", errors)
    require("picksBySlot[slot.slotId]" in surface,
            "Viewer must project selected row picksBySlot into board slots.", errors)
    require("data-player-board-viewer-slot" in surface,
            "Viewer must render per-slot pick cells.", errors)
    require("disabled aria-label" in surface or "disabled" in surface,
            "Viewer pick cells must be disabled/read-only.", errors)
    require("pointer-events: none" in css and ".player-board-viewer-pick:disabled" in css,
            "Viewer pick cells must be styled as disabled/read-only display cells.", errors)
    require("closePlayerBoardViewer" in surface and "restoreFocus" in surface,
            "Viewer must provide close/back restoration behavior.", errors)
    require("currentStandingsRows" in surface and "renderStandingsRows(panel, rows)" in surface,
            "Viewer must use the current public standings rows rather than a private source.", errors)

    forbidden_viewer_write_tokens = [
        "saveUserBracket",
        "LocalStorageBracketStore",
        "SupabaseBracketStore",
        ".insert(",
        ".upsert(",
        ".update(",
        ".delete(",
        "localStorage.setItem",
    ]
    viewer_section_start = surface.find("function renderPlayerBoard")
    viewer_section = surface[viewer_section_start:] if viewer_section_start >= 0 else surface
    for token in forbidden_viewer_write_tokens:
        require(token not in viewer_section,
                f"Board viewer must not call write/save path token: {token}", errors)

    for private_token in ["auth_id", "raw_user_meta_data", "auth.uid()", "email"]:
        require(private_token not in surface,
                f"Standings board viewer must not expose private identity token: {private_token}", errors)

    require(".player-board-viewer-panel" in css,
            "CSS must style the full board viewer panel.", errors)
    require(".player-board-viewer-card" in css,
            "CSS must style the full board viewer card.", errors)
    require(".player-board-viewer-scroll" in css and "overflow: auto" in css,
            "CSS must make the board viewer navigable.", errors)
    require(".player-board-viewer-plane" in css and "transform: scale" in css,
            "CSS must support board viewer zoom scaling.", errors)
    require(".player-board-viewer-pick" in css and "position: absolute" in css,
            "CSS must place viewer pick cells on the board.", errors)
    require(".player-standings-player-button" in css and "text-decoration: underline" in css,
            "CSS must make standings player actions visually actionable.", errors)

    for path in [
        "cards/285_player_standings_board_viewer_card.md",
        "captures/CAPTURE_BACK_PLAYER_STANDINGS_BOARD_VIEWER.md",
        "docs/features/player_standings_board_viewer.md",
        "li/world_cup/player_standings_board_viewer_rule.md",
    ]:
        require(Path(path).exists(), f"Missing governance/doc file: {path}", errors)

    require("python3 tools/verify_wc2026_player_standings_board_viewer.py" in makefile,
            "Makefile verify must include player standings board viewer verifier.", errors)

    if errors:
        print("Player standings board viewer verification failed: " + "; ".join(errors))
        return 1

    print("OK: Player Standings opens a full read-only board viewer from public picksBySlot without save-path writes or private identity exposure.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
