function numberFrom(value) {
  const number = Number(value);
  return Number.isFinite(number) ? number : null;
}

function labelFor(value, fallback) {
  if (!value || typeof value !== "object") return fallback;

  return (
    value.slotId ||
    value.pickId ||
    value.bracketId ||
    value.id ||
    value.key ||
    value.name ||
    value.label ||
    value.slotKey ||
    value.role ||
    fallback
  );
}

function rectFrom(value) {
  if (!value || typeof value !== "object") return null;

  const x = numberFrom(value.x ?? value.left);
  const y = numberFrom(value.y ?? value.top);
  const width = numberFrom(value.width ?? value.w);
  const height = numberFrom(value.height ?? value.h);

  if (x === null || y === null || width === null || height === null) return null;
  if (width <= 0 || height <= 0) return null;

  return { x, y, width, height };
}

function collectIndexedRects(value, path = "manifest", out = [], parent = null) {
  const rect = rectFrom(value);

  if (rect) {
    const labelSource = parent && parent !== value ? parent : value;
    out.push({
      ...rect,
      index: out.length + 1,
      id: String(labelFor(labelSource, path)),
      path,
    });
  }

  if (Array.isArray(value)) {
    value.forEach((child, index) => collectIndexedRects(child, `${path}[${index}]`, out, value));
    return out;
  }

  if (value && typeof value === "object") {
    Object.entries(value).forEach(([key, child]) => {
      const nextParent = key === "boundsPx" ? value : child;
      collectIndexedRects(child, `${path}.${key}`, out, nextParent);
    });
  }

  return out;
}

function createIndexMarker(rect) {
  const marker = document.createElement("div");
  marker.className = "pick-index-marker";
  marker.dataset.pickIndex = String(rect.index);
  marker.dataset.pickIndexId = rect.id;
  marker.dataset.pickIndexPath = rect.path;
  marker.style.left = `${rect.x}px`;
  marker.style.top = `${rect.y}px`;
  marker.style.width = `${rect.width}px`;
  marker.style.height = `${rect.height}px`;

  const badge = document.createElement("span");
  badge.className = "pick-index-badge";
  badge.textContent = `${String(rect.index).padStart(2, "0")} · ${rect.id}`;

  marker.append(badge);
  return marker;
}

async function createPickIndexLayer({ geometryManifest }) {
  const layer = document.createElement("div");
  layer.className = "board-layer board-pick-index-layer";
  layer.dataset.layerRole = "pick-index";
  layer.dataset.pickIndexState = "loading";

  try {
    const response = await fetch(geometryManifest);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);

    const manifest = await response.json();
    const rects = collectIndexedRects(manifest)
      .filter((rect) => rect.width >= 4 && rect.height >= 4);

    layer.dataset.pickIndexState = rects.length === 0 ? "empty" : "ready";
    layer.dataset.pickIndexCount = String(rects.length);

    rects.forEach((rect) => {
      layer.append(createIndexMarker(rect));
    });
  } catch (error) {
    layer.dataset.pickIndexState = "error";
    layer.dataset.pickIndexError = error instanceof Error ? error.message : String(error);
  }

  return layer;
}

export { createPickIndexLayer };
