(function(){
  const storageKey = "wc2026.game1.bracketPicks";
  // WC2026_R32_PROJECTION_UNTIL_FIFA_LOCK_STORE_START
  const r32AssignmentStateKey = "wc2026.game1.r32.assignmentState";
  const defaultR32AssignmentState = Object.freeze({
    state: "projection",
    locked: false,
    source: null,
    label: "R32 projection: editable until FIFA lock"
  });

  function normalizeR32AssignmentState(value){
    const state = String(value?.state || "projection").toLowerCase();
    const locked = Boolean(value?.locked || state === "official");
    return Object.assign({}, defaultR32AssignmentState, value || {}, {
      state: locked ? "official" : state,
      locked,
      source: locked ? (value?.source || "fifa") : (value?.source || null),
      label: value?.label || (locked ? "Official FIFA R32: locked" : defaultR32AssignmentState.label)
    });
  }

  function loadR32AssignmentState(){
    const raw = localStorage.getItem(r32AssignmentStateKey);
    if (!raw) return normalizeR32AssignmentState(defaultR32AssignmentState);
    try { return normalizeR32AssignmentState(JSON.parse(raw)); }
    catch { return normalizeR32AssignmentState(defaultR32AssignmentState); }
  }

  function saveR32AssignmentState(value){
    const normalized = normalizeR32AssignmentState(value);
    localStorage.setItem(r32AssignmentStateKey, JSON.stringify(normalized));
    return normalized;
  }

  function isR32Locked(){ return loadR32AssignmentState().locked === true; }
  function canEditR32(){ return !isR32Locked(); }
  // WC2026_R32_PROJECTION_UNTIL_FIFA_LOCK_STORE_END
  const legacyKeys = Object.freeze({
    r32: "wc2026.game1.r32.picks",
    r16: "wc2026.game1.r16.winnerPicks",
    advancement: "wc2026.game1.qfSf.winnerPicks",
    knockout: "wc2026.game1.knockoutPicks"
  });

  function pad2(n){ return String(n).padStart(2, "0"); }
  function slot(slotId, round, side, index, sourceSlotIds){
    return {slotId, round, side, index, sourceSlotIds: sourceSlotIds || []};
  }

  const slots = [];
  ["L", "R"].forEach(side => {
    for (let i = 1; i <= 16; i++) slots.push(slot(`${side}-R32-${pad2(i)}`, "R32", side, i));
    for (let i = 1; i <= 8; i++) slots.push(slot(`${side}-R16-${pad2(i)}`, "R16", side, i, [`${side}-R32-${pad2((i * 2) - 1)}`, `${side}-R32-${pad2(i * 2)}`]));
    for (let i = 1; i <= 4; i++) slots.push(slot(`${side}-QF-${pad2(i)}`, "QF", side, i, [`${side}-R16-${pad2((i * 2) - 1)}`, `${side}-R16-${pad2(i * 2)}`]));
    for (let i = 1; i <= 2; i++) slots.push(slot(`${side}-SF-${pad2(i)}`, "SF", side, i, [`${side}-QF-${pad2((i * 2) - 1)}`, `${side}-QF-${pad2(i * 2)}`]));
  });
  slots.push(slot("CENTER-FINAL-FOUR", "FINAL_FOUR", "CENTER", 1, ["L-SF-01", "L-SF-02", "R-SF-01", "R-SF-02"]));

  const slotById = Object.fromEntries(slots.map(s => [s.slotId, s]));

  function readJson(key){
    try { return JSON.parse(localStorage.getItem(key) || "{}"); }
    catch { return {}; }
  }

  function writeJson(key, value){
    localStorage.setItem(key, JSON.stringify(value || {}));
    return value || {};
  }

  function normalizePick(slotId, pick){
    const meta = slotById[slotId] || {};
    return Object.assign({}, pick || {}, {
      assignedSlotId: slotId,
      assignmentTargetSlotId: slotId,
      round: pick?.round || meta.round || "UNKNOWN",
      sourceSlotIds: pick?.sourceSlotIds || meta.sourceSlotIds || [],
      storeContract: "wc2026-game1-bracket-picks-v001"
    });
  }

  function load(){ return readJson(storageKey); }
  function save(value){ return writeJson(storageKey, value); }
  function get(slotId){ return load()[slotId] || null; }
  function set(slotId, pick){
    if (!slotId || !pick) return null;
    const current = load();
    current[slotId] = normalizePick(slotId, pick);
    save(current);
    return current[slotId];
  }
  function clear(slotId){
    const current = load();
    delete current[slotId];
    save(current);
    return current;
  }

  function migrateLegacy(){
    const current = load();
    const r32 = readJson(legacyKeys.r32);
    const r16 = readJson(legacyKeys.r16);
    const adv = readJson(legacyKeys.advancement);
    Object.entries(r32 || {}).forEach(([slotId, pick]) => { current[slotId] = normalizePick(slotId, pick); });
    Object.entries(r16 || {}).forEach(([slotId, pick]) => { current[slotId] = normalizePick(slotId, pick); });
    Object.entries(adv || {}).forEach(([slotId, pick]) => { current[slotId] = normalizePick(slotId, pick); });
    save(current);
    return current;
  }

  window.WC2026_GAME1_BRACKET_PICK_STORE = Object.freeze({
    version: "v001",
    storageKey,
    r32AssignmentStateKey,
    defaultR32AssignmentState,
    legacyKeys,
    slots,
    slotById
  });

  window.WC2026_GAME1_BRACKET_PICK_STORE_API = Object.freeze({
    load,
    save,
    get,
    set,
    clear,
    migrateLegacy,
    loadR32AssignmentState,
    saveR32AssignmentState,
    isR32Locked,
    canEditR32,
    slots: () => slots.slice(),
    slotById: id => slotById[id] || null
  });
})();
