function byKey(items, key) {
  return Object.fromEntries((items || []).map((item) => [item[key], item]));
}

function getBounds(slot) {
  return slot?.boundsPx || slot?.bounds || slot?.box || null;
}

function markerFor({ logicSlot, geometrySlot }) {
  const bounds = getBounds(geometrySlot);
  const marker = document.createElement("div");
  marker.className = "fifa-slot-map-marker";
  marker.dataset.fifaSlotId = logicSlot.fifaSlotId;
  marker.dataset.fifaLabel = logicSlot.fifaLabel;
  marker.dataset.geometrySlotId = geometrySlot.slotId;
  marker.dataset.matchupId = logicSlot.matchupId;
  marker.dataset.qualifierKind = logicSlot.qualifierKind;

  marker.style.left = `${bounds.x}px`;
  marker.style.top = `${bounds.y}px`;
  marker.style.width = `${bounds.width}px`;
  marker.style.height = `${bounds.height}px`;

  const label = document.createElement("span");
  label.className = "fifa-slot-map-label";
  label.textContent = logicSlot.fifaLabel;

  marker.append(label);
  return marker;
}

async function fetchJson(path) {
  const response = await fetch(path, { cache: "no-cache" });
  if (!response.ok) throw new Error(`${path}: HTTP ${response.status}`);
  return response.json();
}

async function createFifaSlotMapLayer({
  logicSource = "data/model/fifa_r32_logical_slot_order.json",
  bridgeSource = "data/geometry/game1_fifa_slot_geometry_map.json",
  geometryManifest = "data/geometry/gameboard_manifest.json",
} = {}) {
  const layer = document.createElement("div");
  layer.className = "board-layer board-fifa-slot-map-layer";
  layer.dataset.layerRole = "fifa-slot-map";
  layer.dataset.fifaSlotMapState = "loading";

  try {
    const [logic, bridge, geometry] = await Promise.all([
      fetchJson(logicSource),
      fetchJson(bridgeSource),
      fetchJson(geometryManifest),
    ]);

    const logicByFifaSlotId = byKey(logic.slots, "fifaSlotId");
    const geometryBySlotId = byKey(geometry.slots, "slotId");

    let rendered = 0;
    for (const bridgeSlot of bridge.slots || []) {
      const logicSlot = logicByFifaSlotId[bridgeSlot.fifaSlotId];
      const geometrySlot = geometryBySlotId[bridgeSlot.geometrySlotId];

      if (!logicSlot || !getBounds(geometrySlot)) continue;

      layer.append(markerFor({ logicSlot, geometrySlot }));
      rendered += 1;
    }

    layer.dataset.fifaSlotMapState = rendered === 0 ? "empty" : "ready";
    layer.dataset.fifaSlotMapCount = String(rendered);
  } catch (error) {
    layer.dataset.fifaSlotMapState = "error";
    layer.dataset.fifaSlotMapError = error instanceof Error ? error.message : String(error);
  }

  return layer;
}

export { createFifaSlotMapLayer };
