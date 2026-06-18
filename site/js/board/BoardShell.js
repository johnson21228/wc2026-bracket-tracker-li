import { createBackgroundLayer } from "./BackgroundLayer.js";
import { createSvgGameboardLayer } from "./SvgGameboardLayer.js";
import { createFifaSlotMapLayer } from "./FifaSlotMapLayer.js";
import { createGame1LifecycleStatusSurface } from "./Game1LifecycleStatusSurface.js";
import { createPickIdentifierLayer } from "./PickIdentifierLayer.js";

const BOARD_NATIVE_SIZE = Object.freeze({
  width: 1536,
  height: 1024,
});

function createBackgroundGradientLayer() {
  const layer = document.createElement("div");
  layer.className = "board-layer board-background-gradient-layer";
  layer.dataset.layerRole = "bottom-background-gradient";
  return layer;
}

async function createBoardShell({ truthResources }) {
  const viewport = document.createElement("section");
  viewport.className = "game1-board-viewport";
  viewport.setAttribute("aria-label", "WC2026 clean board viewport");
  viewport.dataset.module = "BoardShell";

  const plane = document.createElement("div");
  plane.className = "pixel-native-board-plane";
  plane.dataset.nativeWidth = String(BOARD_NATIVE_SIZE.width);
  plane.dataset.nativeHeight = String(BOARD_NATIVE_SIZE.height);
  plane.dataset.boardPlane = "background-gameboard-outline";
  plane.dataset.truthSvgGameboardDefinition = truthResources.svgGameboardDefinition;
  plane.dataset.truthGeometryManifest = truthResources.geometryManifest;
  plane.dataset.showPubBackground = "true";
  plane.dataset.showGameboard = "true";
  plane.dataset.showGeometryFrames = "false";
  plane.dataset.showPickIndex = "false";
  plane.dataset.showPickIdentifiers = "true";
  plane.dataset.showFifaSlotMap = "false";
  plane.style.setProperty("--gameboard-opacity", "0.52");
  plane.style.setProperty("--gameboard-line-color", "rgba(255, 255, 255, 0.98)");
  plane.style.setProperty("--gameboard-line-width", "1.5");
  plane.style.setProperty("--gameboard-line-glow", "0.05");

  plane.append(
    createBackgroundLayer({
      backgroundImage: truthResources.backgroundImage,
    }),
    createBackgroundGradientLayer(),
    createGame1LifecycleStatusSurface(),
    await createSvgGameboardLayer({
      svgGameboardDefinition: truthResources.svgGameboardDefinition,
    })
    await createFifaSlotMapLayer({
      geometryManifest: truthResources.geometryManifest,
    }),,
    await createPickIdentifierLayer({
      geometryManifest: truthResources.geometryManifest,
    })
  );

  viewport.appendChild(plane);
  return viewport;
}

export { BOARD_NATIVE_SIZE, createBoardShell };
