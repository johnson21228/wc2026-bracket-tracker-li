function createBackgroundLayer({ backgroundImage }) {
  const layer = document.createElement("img");
  layer.className = "board-layer board-background-layer";
  layer.dataset.layerRole = "bottom-background-authority";
  layer.alt = "WC2026 pub background";
  layer.decoding = "async";
  layer.src = backgroundImage;
  return layer;
}

export { createBackgroundLayer };
