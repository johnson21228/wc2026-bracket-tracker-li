function slotBounds(slot) {
  return slot.boundsPx || slot.bounds || slot.rectPx || slot.rect || null;
}

function slotIdentity(slot, index) {
  return (
    slot.id ||
    slot.slotId ||
    slot.pickId ||
    slot.identifier ||
    slot.key ||
    slot.name ||
    slot.label ||
    `pick-${String(index + 1).padStart(2, "0")}`
  );
}

function slotKind(slot) {
  return (
    slot.kind ||
    slot.type ||
    slot.round ||
    slot.role ||
    "pick"
  );
}

function makeLabel({ slot, index }) {
  const bounds = slotBounds(slot);
  if (!bounds) return null;

  const x = Number(bounds.x);
  const y = Number(bounds.y);
  const width = Number(bounds.width ?? bounds.w);
  const height = Number(bounds.height ?? bounds.h);

  if (![x, y, width, height].every(Number.isFinite)) return null;

  const label = document.createElement("div");
  label.className = "pick-identifier-label";
  label.dataset.slotIdentity = slotIdentity(slot, index);
  label.dataset.slotKind = slotKind(slot);
  label.textContent = slotIdentity(slot, index);
  label.title = JSON.stringify(
    {
      identity: slotIdentity(slot, index),
      kind: slotKind(slot),
      bounds: { x, y, width, height },
    },
    null,
    2
  );

  label.style.left = `${x}px`;
  label.style.top = `${y}px`;
  label.style.width = `${width}px`;
  label.style.height = `${height}px`;

  return label;
}

async function createPickIdentifierLayer({ geometryManifest }) {
  const layer = document.createElement("div");
  layer.className = "board-layer pick-identifier-layer";
  layer.dataset.layerRole = "developer-pick-identifiers";
  layer.dataset.geometryManifest = geometryManifest;

  try {
    const response = await fetch(geometryManifest);
    if (!response.ok) {
      throw new Error(`Could not load geometry manifest: ${response.status}`);
    }

    const manifest = await response.json();
    const slots = Array.isArray(manifest.slots) ? manifest.slots : [];

    slots
      .map((slot, index) => makeLabel({ slot, index }))
      .filter(Boolean)
      .forEach((label) => layer.appendChild(label));

    layer.dataset.identifierState = "ready";
    layer.dataset.identifierCount = String(layer.childElementCount);
  } catch (error) {
    layer.dataset.identifierState = "error";
    layer.dataset.identifierError = error instanceof Error ? error.message : String(error);
  }

  return layer;
}

export { createPickIdentifierLayer, slotIdentity };
