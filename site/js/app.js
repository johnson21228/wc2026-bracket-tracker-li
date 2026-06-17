import { requireElementById } from "./services/domMounts.js";
import {
  createDebugConsole,
  debugError,
  debugLog,
  installGlobalDebugConsole,
} from "./services/DebugConsole.js";

function createStartupFailurePanel(error) {
  const message = error instanceof Error ? error.message : String(error);

  const panel = document.createElement("section");
  panel.className = "startup-error";
  panel.setAttribute("role", "alert");

  const title = document.createElement("h1");
  title.textContent = "WC2026 site failed to start";

  const body = document.createElement("pre");
  body.textContent = message;

  panel.append(title, body);
  return panel;
}

async function loadRuntimeModules() {
  debugLog("importing asset paths");
  const assetPathsModule = await import("./services/assetPaths.js");

  debugLog("importing board shell");
  const boardShellModule = await import("./board/BoardShell.js");

  debugLog("importing developer frame");
  const developerFrameModule = await import("./dev/DeveloperFrame.js");

  return {
    BOARD_TRUTH_RESOURCES: assetPathsModule.BOARD_TRUTH_RESOURCES,
    createBoardShell: boardShellModule.createBoardShell,
    createDeveloperFrame: developerFrameModule.createDeveloperFrame,
  };
}

async function startApp() {
  installGlobalDebugConsole();

  const appMount = requireElementById("wc2026-app");
  const debugConsole = createDebugConsole();

  appMount.replaceChildren(debugConsole);
  debugLog("debug console mounted");
  debugLog("app mount found", { id: appMount.id });

  try {
    const {
      BOARD_TRUTH_RESOURCES,
      createBoardShell,
      createDeveloperFrame,
    } = await loadRuntimeModules();

    debugLog("truth resources", BOARD_TRUTH_RESOURCES);

    debugLog("creating board shell");
    const boardShell = await createBoardShell({
      truthResources: BOARD_TRUTH_RESOURCES,
    });

    debugLog("board shell created", {
      module: boardShell.dataset.module,
      childCount: boardShell.childElementCount,
    });

    const boardPlane = boardShell.querySelector("[data-board-plane]");
    debugLog("board plane lookup", {
      found: Boolean(boardPlane),
      boardPlane: boardPlane?.dataset.boardPlane,
      svgState: boardPlane?.querySelector(".board-svg-gameboard-layer")?.dataset.svgState,
    });

    debugLog("creating developer frame");
    const developerFrame = createDeveloperFrame({ boardPlane });

    appMount.replaceChildren(boardShell, developerFrame, debugConsole);
    debugLog("app mounted");
  } catch (error) {
    debugError("startup failed", error);
    appMount.replaceChildren(createStartupFailurePanel(error), debugConsole);
  }
}

startApp();
