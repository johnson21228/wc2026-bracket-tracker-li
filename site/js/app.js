import { BOARD_TRUTH_RESOURCES } from "./services/assetPaths.js";
import { requireElementById } from "./services/domMounts.js";
import { createBoardShell } from "./board/BoardShell.js";
import { createDeveloperFrame } from "./dev/DeveloperFrame.js";

function startApp() {
  const appMount = requireElementById("wc2026-app");

  const boardShell = createBoardShell({
    truthResources: BOARD_TRUTH_RESOURCES,
  });

  const boardPlane = boardShell.querySelector("[data-board-plane]");
  const developerFrame = createDeveloperFrame({ boardPlane });

  appMount.replaceChildren(boardShell, developerFrame);
}

startApp();
