const DEFAULT_BOTTOM_CONTROL_SELECTORS = [
  "[data-group-rail-layer]",
  ".board-group-rail-layer",
  ".group-rail",
  ".group-button-rail",
  "[data-bottom-controls]",
  ".board-bottom-controls",
  ".gameboard-bottom-controls",
  ".bottom-frame-controls",
];

function clamp(value, min, max) {
  if (max < min) return min;
  return Math.max(min, Math.min(max, value));
}

function rectsOverlapHorizontally(a, b) {
  return a.left < b.right && a.right > b.left;
}

function intersectRects(a, b) {
  return {
    left: Math.max(a.left, b.left),
    top: Math.max(a.top, b.top),
    right: Math.min(a.right, b.right),
    bottom: Math.min(a.bottom, b.bottom),
  };
}

function rectWidth(rect) {
  return Math.max(0, rect.right - rect.left);
}

function rectHeight(rect) {
  return Math.max(0, rect.bottom - rect.top);
}

function boardScaleFromRenderedRect(boardPlane) {
  const nativeWidth = Number(boardPlane?.dataset?.nativeWidth) || Number.parseFloat(getComputedStyle(boardPlane).getPropertyValue("--board-w-px")) || boardPlane?.offsetWidth || 1536;
  const renderedWidth = boardPlane?.getBoundingClientRect().width || nativeWidth;
  const scale = renderedWidth / nativeWidth;
  return Number.isFinite(scale) && scale > 0 ? scale : 1;
}

function clientPointToBoardPoint({ boardRect, scale, x, y }) {
  return {
    x: (x - boardRect.left) / scale,
    y: (y - boardRect.top) / scale,
  };
}

function clientRectToBoardRect({ boardRect, scale, rect }) {
  const topLeft = clientPointToBoardPoint({ boardRect, scale, x: rect.left, y: rect.top });
  const bottomRight = clientPointToBoardPoint({ boardRect, scale, x: rect.right, y: rect.bottom });
  return {
    left: topLeft.x,
    top: topLeft.y,
    right: bottomRight.x,
    bottom: bottomRight.y,
    width: bottomRight.x - topLeft.x,
    height: bottomRight.y - topLeft.y,
  };
}

function boardRectFromNativeBounds(bounds) {
  return {
    left: bounds.x,
    top: bounds.y,
    right: bounds.x + bounds.width,
    bottom: bounds.y + bounds.height,
    width: bounds.width,
    height: bounds.height,
  };
}

function findBottomControlRect({ boardPlane, viewportRect, selectors, margin }) {
  let top = null;
  for (const selector of selectors) {
    for (const element of boardPlane.querySelectorAll(selector)) {
      const rect = element.getBoundingClientRect();
      if (rect.width <= 0 || rect.height <= 0) continue;
      if (!rectsOverlapHorizontally(rect, viewportRect)) continue;
      if (rect.bottom < viewportRect.top || rect.top > viewportRect.bottom) continue;
      top = top === null ? rect.top : Math.min(top, rect.top);
    }
  }
  if (top === null) return null;
  return Math.max(viewportRect.top, top - margin);
}

function computeVisibleSafeRect({ boardPlane, viewportEl, margin, bottomControlSelectors }) {
  const viewport = viewportEl || boardPlane?.closest("[data-board-scroll]") || boardPlane?.parentElement || boardPlane;
  const viewportRect = viewport.getBoundingClientRect();
  const windowRect = {
    left: 0,
    top: 0,
    right: window.innerWidth || document.documentElement.clientWidth || viewportRect.right,
    bottom: window.innerHeight || document.documentElement.clientHeight || viewportRect.bottom,
  };
  let safeClient = intersectRects(viewportRect, windowRect);

  const bottomControlTop = findBottomControlRect({
    boardPlane,
    viewportRect: safeClient,
    selectors: bottomControlSelectors,
    margin,
  });
  if (bottomControlTop !== null) {
    safeClient = { ...safeClient, bottom: Math.min(safeClient.bottom, bottomControlTop) };
  }

  if (rectWidth(safeClient) < margin * 2 || rectHeight(safeClient) < margin * 2) {
    safeClient = viewportRect;
  }

  const boardRect = boardPlane.getBoundingClientRect();
  const scale = boardScaleFromRenderedRect(boardPlane);
  const safeBoard = clientRectToBoardRect({ boardRect, scale, rect: safeClient });
  return {
    left: safeBoard.left + margin / scale,
    top: safeBoard.top + margin / scale,
    right: safeBoard.right - margin / scale,
    bottom: safeBoard.bottom - margin / scale,
    scale,
  };
}

function chooseCandidate({ candidates, safeRect, surfaceWidth, surfaceHeight }) {
  for (const candidate of candidates) {
    const fitsX = candidate.left >= safeRect.left && candidate.left + surfaceWidth <= safeRect.right;
    const fitsY = candidate.top >= safeRect.top && candidate.top + surfaceHeight <= safeRect.bottom;
    if (fitsX && fitsY) return candidate;
  }
  return candidates[0];
}

function candidatePositions({ preference, anchorRect, surfaceWidth, surfaceHeight, gap }) {
  const centeredLeft = anchorRect.left + (anchorRect.width / 2) - (surfaceWidth / 2);
  const centeredTop = anchorRect.top + (anchorRect.height / 2) - (surfaceHeight / 2);
  const positions = {
    below: { left: centeredLeft, top: anchorRect.bottom + gap, placement: "below" },
    above: { left: centeredLeft, top: anchorRect.top - surfaceHeight - gap, placement: "above" },
    right: { left: anchorRect.right + gap, top: centeredTop, placement: "right" },
    left: { left: anchorRect.left - surfaceWidth - gap, top: centeredTop, placement: "left" },
  };
  if (preference === "above-then-below") return [positions.above, positions.below, positions.right, positions.left];
  if (preference === "below-then-above") return [positions.below, positions.above, positions.right, positions.left];
  if (preference === "right-then-left") return [positions.right, positions.left, positions.above, positions.below];
  return [positions.below, positions.above, positions.right, positions.left];
}

function positionFloatingSurfaceNearAnchor({
  anchorEl,
  anchorBoundsPx,
  surfaceEl,
  boardPlane,
  viewportEl,
  preferredPlacement = "below-then-above",
  margin = 12,
  gap = 10,
  bottomControlSelectors = DEFAULT_BOTTOM_CONTROL_SELECTORS,
  minWidth = 260,
  maxWidth = 520,
  maxHeight = 520,
} = {}) {
  if (!surfaceEl || !boardPlane) return null;

  const boardRect = boardPlane.getBoundingClientRect();
  const scale = boardScaleFromRenderedRect(boardPlane);
  const anchorRect = anchorEl
    ? clientRectToBoardRect({ boardRect, scale, rect: anchorEl.getBoundingClientRect() })
    : boardRectFromNativeBounds(anchorBoundsPx || { x: 0, y: 0, width: 0, height: 0 });
  const safeRect = computeVisibleSafeRect({ boardPlane, viewportEl, margin, bottomControlSelectors });
  const safeWidth = Math.max(minWidth, safeRect.right - safeRect.left);
  const safeHeight = Math.max(180, safeRect.bottom - safeRect.top);

  surfaceEl.dataset.floatingSurfacePlacement = "zoom-50-safe";
  surfaceEl.dataset.floatingSurfaceUsesClientRects = "true";
  surfaceEl.style.position = "absolute";
  surfaceEl.style.boxSizing = "border-box";
  surfaceEl.style.maxWidth = `${Math.round(Math.min(maxWidth, safeWidth))}px`;
  surfaceEl.style.maxHeight = `${Math.round(Math.min(maxHeight, safeHeight))}px`;
  surfaceEl.style.overflow = "auto";

  const surfaceWidth = Math.min(surfaceEl.offsetWidth || minWidth, safeWidth);
  const surfaceHeight = Math.min(surfaceEl.offsetHeight || surfaceEl.scrollHeight || 320, safeHeight);
  surfaceEl.style.width = `${Math.round(Math.max(minWidth, Math.min(surfaceWidth, maxWidth, safeWidth)))}px`;
  surfaceEl.style.maxHeight = `${Math.round(Math.max(160, Math.min(surfaceHeight, maxHeight, safeHeight)))}px`;

  const measuredWidth = Math.min(surfaceEl.offsetWidth || surfaceWidth, safeWidth);
  const measuredHeight = Math.min(surfaceEl.offsetHeight || surfaceEl.scrollHeight || surfaceHeight, safeHeight);
  const candidates = candidatePositions({ preference: preferredPlacement, anchorRect, surfaceWidth: measuredWidth, surfaceHeight: measuredHeight, gap });
  const selected = chooseCandidate({ candidates, safeRect, surfaceWidth: measuredWidth, surfaceHeight: measuredHeight });

  const left = clamp(selected.left, safeRect.left, safeRect.right - measuredWidth);
  const top = clamp(selected.top, safeRect.top, safeRect.bottom - measuredHeight);

  surfaceEl.style.left = `${Math.round(left)}px`;
  surfaceEl.style.top = `${Math.round(top)}px`;
  surfaceEl.dataset.floatingSurfacePlacementSide = selected.placement;
  surfaceEl.dataset.floatingSurfaceSafeBottomExcludesControls = "true";
  surfaceEl.dataset.floatingSurfaceBoardScale = String(Number.isFinite(scale) ? Math.round(scale * 100) / 100 : 1);

  return { left, top, width: measuredWidth, height: measuredHeight, placement: selected.placement, safeRect };
}

export { positionFloatingSurfaceNearAnchor };
