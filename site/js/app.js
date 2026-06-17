import { BOARD_TRUTH_RESOURCES } from "./services/assetPaths.js";
import { requireElementById } from "./services/domMounts.js";
import { createBoardShell } from "./board/BoardShell.js";
import { createDeveloperControlsPanel } from "./dev/DeveloperControlsPanel.js";

function startApp() {
  const appMount = requireElementById("wc2026-app");
  const boardShell = createBoardShell({
    truthResources: BOARD_TRUTH_RESOURCES,
  });
  const boardPlane = boardShell.querySelector("[data-board-plane]");
  const developerControls = createDeveloperControlsPanel({
    appMount,
    boardPlane,
    truthResources: BOARD_TRUTH_RESOURCES,
  });

  appMount.replaceChildren(boardShell, developerControls);
}

startApp();
