import { createBackgroundLayer } from "./BackgroundLayer.js";

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

function createBoardShell({ truthResources }) {
  const viewport = document.createElement("section");
  viewport.className = "game1-board-viewport";
  viewport.setAttribute("aria-label", "WC2026 clean board viewport");
  viewport.dataset.module = "BoardShell";

  const plane = document.createElement("div");
  plane.className = "pixel-native-board-plane";
  plane.dataset.nativeWidth = String(BOARD_NATIVE_SIZE.width);
  plane.dataset.nativeHeight = String(BOARD_NATIVE_SIZE.height);
  plane.dataset.boardPlane = "background-first";
  plane.dataset.truthSvgGameboardDefinition = truthResources.svgGameboardDefinition;
  plane.dataset.truthGeometryManifest = truthResources.geometryManifest;

  plane.append(
    createBackgroundLayer({
      backgroundImage: truthResources.backgroundImage,
    }),
    createBackgroundGradientLayer()
  );

  viewport.appendChild(plane);
  return viewport;
}

export { BOARD_NATIVE_SIZE, createBoardShell };
