# WC2026 Game 1 State Read / Rendering Inventory

This report inventories code regions that read pick state or render pick state.

Classify findings as:

- GOOD: reads from `WC2026_GAME1_PICK_STATE`
- OK TEMPORARY: reads through `WC2026_GAME1_BRACKET_PICK_STORE_API`
- BAD: render path reads localStorage or legacy mirrors directly


## canonical_model

3617: `window.WC2026_GAME1_PICK_STATE = {`

## old_api

2106: `if (typeof wc2026PickForSlot === 'function') {`
2107: `wc2026PickForSlot = function wc2026PickForSlotWithR32ManifestAliases(slotId){`
2355: `const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;`
2373: `function wc2026StorePickForSlot(slotId, team, rule){`
2401: `function wc2026PickForSlot(slotId){`
2451: `const direct = wc2026PickForSlot(slotId);`
2489: `const pick = wc2026PickForSlot(rule.slotId);`
2512: `const pick = wc2026PickForSlot(rule.slotId);`
2566: `function wc2026ClearPickForSlot(slotId, round){`
2616: `? wc2026PickForSlot(rule.slotId)`
2620: `try { wc2026ClearPickForSlot(rule.slotId, round); } catch {}`
2647: `wc2026ClearPickForSlot(rule.slotId, round);`
2671: `wc2026StorePickForSlot(rule.slotId, team, rule);`
2798: `Object.entries(nextPicks || {}).forEach(([slotId, pick]) => wc2026StorePickForSlot(slotId, pick, {slotId, round: "R32"}));`
2807: `get: wc2026PickForSlot,`
2808: `set: wc2026StorePickForSlot,`
3330: `return window.WC2026_GAME1_BRACKET_PICK_STORE_API || null;`
3709: `const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;`
3749: `try { window.WC2026_GAME1_BRACKET_PICK_STORE_API?.clear?.(slotId); } catch {}`
4010: `const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;`
4110: `const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;`
4280: `const previousClearPickForSlot = typeof wc2026ClearPickForSlot === "function" ? wc2026ClearPickForSlot : null;`
4282: `wc2026ClearPickForSlot = function wc2026ClearPickForSlotWithDownstream(slotId, round){`
4324: `const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;`
4353: `try { window.WC2026_GAME1_BRACKET_PICK_STORE_API?.clear?.(slotId); } catch {}`
4521: `const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;`
4556: `try { window.WC2026_GAME1_BRACKET_PICK_STORE_API?.clear?.(id); } catch {}`
4677: `const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;`
4844: `window.WC2026_GAME1_BRACKET_PICK_STORE_API?.set?.(slotId, stored);`
4980: `try { return window.WC2026_GAME1_BRACKET_PICK_STORE_API?.slotById?.(slotId) || null; }`
5437: `const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;`

## direct_storage

1041: `try { return normalizeBracketLifecycleState(JSON.parse(localStorage.getItem(BRACKET_LIFECYCLE_STORAGE_KEY) || "null")); }`
1046: `localStorage.setItem(BRACKET_LIFECYCLE_STORAGE_KEY, JSON.stringify(bracketLifecycleState));`
1223: `function loadPicks() { try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}"); } catch { return {}; } }`
1224: `function savePicks(picks) { localStorage.setItem(STORAGE_KEY, JSON.stringify(picks)); }`
1545: `function loadR16Picks() { try { return JSON.parse(localStorage.getItem(R16_STORAGE_KEY) || "{}"); } catch { return {}; } }`
1546: `function saveR16Picks(value) { localStorage.setItem(R16_STORAGE_KEY, JSON.stringify(value)); }`
1692: `function loadAdvancementPicks() { try { return JSON.parse(localStorage.getItem(ADVANCEMENT_STORAGE_KEY) || "{}"); } catch { return {}; } }`
1693: `function saveAdvancementPicks(value) { localStorage.setItem(ADVANCEMENT_STORAGE_KEY, JSON.stringify(value)); }`
2063: `for (let i = 0; i < localStorage.length; i++) {`
2064: `const key = localStorage.key(i) || '';`
2066: `const parsed = JSON.parse(localStorage.getItem(key) || '{}');`
2411: `try { return JSON.parse(localStorage.getItem(key) || "{}"); }`
2483: `const bracket = JSON.parse(localStorage.getItem(key) || "{}");`
2485: `localStorage.setItem(key, JSON.stringify(bracket));`
2506: `const bracket = JSON.parse(localStorage.getItem(key) || "{}");`
2508: `localStorage.setItem(key, JSON.stringify(bracket));`
2574: `const bracket = JSON.parse(localStorage.getItem("wc2026.game1.bracketPicks") || "{}");`
2576: `localStorage.setItem("wc2026.game1.bracketPicks", JSON.stringify(bracket));`
2590: `const qfSf = JSON.parse(localStorage.getItem("wc2026.game1.qfSf.winnerPicks") || "{}");`
2592: `localStorage.setItem("wc2026.game1.qfSf.winnerPicks", JSON.stringify(qfSf));`
2596: `const r16 = JSON.parse(localStorage.getItem("wc2026.game1.r16.winnerPicks") || "{}");`
2598: `localStorage.setItem("wc2026.game1.r16.winnerPicks", JSON.stringify(r16));`
2695: `try { stores.push(JSON.parse(localStorage.getItem("wc2026.game1.r32.picks") || "{}")); } catch {}`
2696: `try { stores.push(JSON.parse(localStorage.getItem("wc2026.game1.bracketPicks") || "{}")); } catch {}`
2697: `try { stores.push(JSON.parse(localStorage.getItem("wc2026.game1.r16.winnerPicks") || "{}")); } catch {}`
2698: `try { stores.push(JSON.parse(localStorage.getItem("wc2026.game1.qfSf.winnerPicks") || "{}")); } catch {}`
2799: `localStorage.setItem("wc2026.game1.r32.picks", JSON.stringify(nextPicks || {}));`
2842: `try { if (key) localStorage.setItem(key, "{}"); } catch {}`
3310: `function readJson(key){`
3312: `const raw = localStorage.getItem(key);`
3321: `function writeJson(key, value){`
3322: `try { localStorage.setItem(key, JSON.stringify(value || {})); } catch {}`
3472: `const canonicalRaw = extractPickMap(readJson(MODEL_KEY));`
3482: `const legacy = extractPickMap(readJson(key));`
3512: `writeJson(MODEL_KEY, saved.picksBySlotId);`
3595: `writeJson(MODEL_KEY, {});`
3596: `MIRROR_KEYS.forEach((key) => writeJson(key, {}));`
3638: `function readJson(key){`
3639: `try { return JSON.parse(localStorage.getItem(key) || "{}"); }`
3644: `const bracket = readJson("wc2026.game1.bracketPicks");`
3645: `const r16 = readJson("wc2026.game1.r16.winnerPicks");`
3646: `const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");`
3651: `function writeJson(key, value){`
3652: `try { localStorage.setItem(key, JSON.stringify(value || {})); } catch {}`
3698: `const bracket = readJson("wc2026.game1.bracketPicks");`
3699: `const r32 = readJson("wc2026.game1.r32.picks");`
3700: `const r16 = readJson("wc2026.game1.r16.winnerPicks");`
3701: `const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");`
3731: `const bracket = readJson("wc2026.game1.bracketPicks");`
3732: `const r16 = readJson("wc2026.game1.r16.winnerPicks");`
3733: `const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");`
3734: `const knockout = readJson("wc2026.game1.knockoutPicks");`
3741: `writeJson("wc2026.game1.bracketPicks", bracket);`
3742: `writeJson("wc2026.game1.r16.winnerPicks", r16);`
3743: `writeJson("wc2026.game1.qfSf.winnerPicks", qfSf);`
3744: `writeJson("wc2026.game1.knockoutPicks", knockout);`
3824: `storedR16Keys: Object.keys(readJson("wc2026.game1.bracketPicks")).filter(k => String(k).includes("-R16-")),`
3825: `storedQfSfKeys: Object.keys(readJson("wc2026.game1.bracketPicks")).filter(k => String(k).includes("-QF-") || String(k).includes("-SF-")),`
4002: `try { bracket = JSON.parse(localStorage.getItem("wc2026.game1.bracketPicks") || "{}"); } catch {}`
4003: `try { r16 = JSON.parse(localStorage.getItem("wc2026.game1.r16.winnerPicks") || "{}"); } catch {}`
4004: `try { qfSf = JSON.parse(localStorage.getItem("wc2026.game1.qfSf.winnerPicks") || "{}"); } catch {}`
4039: `function readJson(key){`
4040: `try { return JSON.parse(localStorage.getItem(key) || "{}"); }`
4044: `function writeJson(key, value){`
4045: `localStorage.setItem(key, JSON.stringify(value || {}));`
4100: `const state = readJson(LOCK_KEY);`
4149: `bracket: readJson(BRACKET_KEY),`
4150: `r32: readJson(R32_KEY),`
4151: `r16: readJson(R16_KEY),`
4152: `qfSf: readJson(QFSF_KEY)`
4157: `writeJson(BRACKET_KEY, stores.bracket);`
4158: `writeJson(R32_KEY, stores.r32);`
4159: `writeJson(R16_KEY, stores.r16);`
4160: `writeJson(QFSF_KEY, stores.qfSf);`
4262: `const before = readJson(R32_KEY);`
4295: `function readJson(key){`
4296: `try { return JSON.parse(localStorage.getItem(key) || "{}"); }`
4300: `function writeJson(key, value){`
4301: `localStorage.setItem(key, JSON.stringify(value || {}));`
4334: `const bracket = readJson("wc2026.game1.bracketPicks");`
4335: `const r32 = readJson("wc2026.game1.r32.picks");`
4336: `const r16 = readJson("wc2026.game1.r16.winnerPicks");`
4337: `const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");`
4344: `writeJson("wc2026.game1.bracketPicks", bracket);`
4345: `writeJson("wc2026.game1.r32.picks", r32);`
4346: `writeJson("wc2026.game1.r16.winnerPicks", r16);`
4347: `writeJson("wc2026.game1.qfSf.winnerPicks", qfSf);`
4363: `const bracket = readJson("wc2026.game1.bracketPicks");`
4364: `const r16 = readJson("wc2026.game1.r16.winnerPicks");`
4365: `const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");`
4411: `const bracket = readJson("wc2026.game1.bracketPicks");`
4412: `const r32 = readJson("wc2026.game1.r32.picks");`
4467: `function readJson(key){`
4468: `try { return JSON.parse(localStorage.getItem(key) || "{}"); }`
4472: `function writeJson(key, value){`
4473: `localStorage.setItem(key, JSON.stringify(value || {}));`
4512: `const bracket = readJson("wc2026.game1.bracketPicks");`
4513: `const r32 = readJson("wc2026.game1.r32.picks");`
4514: `const r16 = readJson("wc2026.game1.r16.winnerPicks");`
4515: `const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");`
4539: `const bracket = readJson("wc2026.game1.bracketPicks");`
4540: `const r32 = readJson("wc2026.game1.r32.picks");`
4541: `const r16 = readJson("wc2026.game1.r16.winnerPicks");`
4542: `const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");`
4543: `const knockout = readJson("wc2026.game1.knockoutPicks");`
4559: `writeJson("wc2026.game1.bracketPicks", bracket);`
4560: `writeJson("wc2026.game1.r32.picks", r32);`
4561: `writeJson("wc2026.game1.r16.winnerPicks", r16);`
4562: `writeJson("wc2026.game1.qfSf.winnerPicks", qfSf);`
4563: `writeJson("wc2026.game1.knockoutPicks", knockout);`
4579: `const bracket = readJson("wc2026.game1.bracketPicks");`
4580: `const r16 = readJson("wc2026.game1.r16.winnerPicks");`
4581: `const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");`
4737: `function readJson(key){`
4738: `try { return JSON.parse(localStorage.getItem(key) || "{}"); }`
4742: `function writeJson(key, value){`
4743: `localStorage.setItem(key, JSON.stringify(value || {}));`
4778: `const r32 = readJson(R32_KEY);`
4779: `const bracket = readJson(BRACKET_KEY);`
4821: `const r32 = readJson(R32_KEY);`
4822: `const bracket = readJson(BRACKET_KEY);`
4836: `writeJson(R32_KEY, r32);`
4837: `writeJson(BRACKET_KEY, bracket);`
4897: `function readJson(key){`
4898: `try { return JSON.parse(localStorage.getItem(key) || "{}"); }`
4961: `bracket: readJson(BRACKET_KEY),`
4962: `r32: readJson(R32_KEY),`
4963: `r16: readJson(R16_KEY),`
4964: `qfSf: readJson(QFSF_KEY)`
5344: `function readJson(key){`
5345: `try { return JSON.parse(localStorage.getItem(key) || "{}"); }`
5349: `function writeJson(key, value){`
5350: `localStorage.setItem(key, JSON.stringify(value || {}));`
5441: `const bracket = readJson(STORAGE.bracket);`
5443: `writeJson(STORAGE.bracket, bracket);`
5446: `const r32 = readJson(STORAGE.r32);`
5448: `writeJson(STORAGE.r32, r32);`
5450: `const r16 = readJson(STORAGE.r16);`
5452: `writeJson(STORAGE.r16, r16);`
5454: `const adv = readJson(STORAGE.advance);`
5456: `writeJson(STORAGE.advance, adv);`

## legacy_state

958: `<div class="toolbar" aria-label="Game 1 tools"><button type="button" id="clearPicks">Clear picks</button><button type="button" id="exportPicks">Export picks</button></div>`
960: `<section class="pixelNativeBoardPlane" aria-label="WC2026 unified bracket board with R32 assignment and knockout picks" data-board-source="site/assets/playfield/uniform_pick_card_gameboard.svg" data-native-width="1536" data-native-height="1024" data-display-mode="native-pixel-scrollable" data-board-visual-authority="uniform-svg-gameboard" data-placement-mode="uniform-svg-r32-manifest" data-game="unified-bracket">`
962: `<div class="pickLayer" id="pickLayer" aria-label="Filled Round of 32 picks"></div>`
1009: `const STORAGE_KEY = "wc2026.game1.r32.picks";`
1074: `game1KnockoutPicksStorageKey: GAME1_KNOCKOUT_PICKS_STORAGE_KEY,`
1224: `function savePicks(picks) { localStorage.setItem(STORAGE_KEY, JSON.stringify(picks)); }`
1225: `let picks = loadPicks();`
1383: `const pick = picks[rule.slotId];`
1505: `function assignTeam(team) { if (!activeSlot) return; picks[activeSlot.slotId] = {...team, assignedSlotId: activeSlot.slotId, slotRule: activeSlot.slotRule, slotRuleLong: activeSlot.slotRuleLong}; savePicks(picks); applyGame1ManifestR32GeometryToSlotRules();`
1547: `let r16Picks = loadR16Picks();`
1583: `return (rule.sourceR32SlotIds || []).map(slotId => picks[slotId]).filter(Boolean);`
1641: `const pick = r16Picks[rule.slotId];`
1677: `r16Picks[activeSlot.slotId] = { ...team, assignedSlotId: activeSlot.slotId, round: "R16", sourceR32SlotIds: activeSlot.sourceR32SlotIds, slotRule: activeSlot.slotRule, slotRuleLong: activeSlot.slotRuleLong };`
1678: `saveR16Picks(r16Picks);`
1694: `let advancementPicks = loadAdvancementPicks();`
1731: `if (String(slotId).includes("-R16-")) return r16Picks?.[slotId] || null;`
1732: `if (String(slotId).includes("-QF-") || String(slotId).includes("-SF-")) return advancementPicks?.[slotId] || null;`
1787: `const pick = advancementPicks[rule.slotId];`
1823: `advancementPicks[activeSlot.slotId] = { ...team, assignedSlotId: activeSlot.slotId, round: activeSlot.round, sourceSlotIds: activeSlot.sourceSlotIds, slotRule: activeSlot.slotRule, slotRuleLong: activeSlot.slotRuleLong };`
1824: `saveAdvancementPicks(advancementPicks);`
1918: `typeof picks !== "undefined" ? picks : null,`
1919: `typeof r16Picks !== "undefined" ? r16Picks : null,`
1920: `typeof advancementPicks !== "undefined" ? advancementPicks : null,`
1922: `window.game1KnockoutPicks,`
1947: `window.game1R32Picks = Object.assign({}, typeof picks !== "undefined" ? picks : {}, window.game1R32Picks || {});`
1948: `window.game1KnockoutPicks = Object.assign({}, typeof r16Picks !== "undefined" ? r16Picks : {}, typeof advancementPicks !== "undefined" ? advancementPicks : {}, window.game1KnockoutPicks || {});`
2057: `try { if (typeof picks !== 'undefined' && picks) stores.push(picks); } catch {}`
2058: `try { if (typeof r16Picks !== 'undefined' && r16Picks) stores.push(r16Picks); } catch {}`
2059: `try { if (typeof advancementPicks !== 'undefined' && advancementPicks) stores.push(advancementPicks); } catch {}`
2060: `try { if (window.game1KnockoutPicks) stores.push(window.game1KnockoutPicks); } catch {}`
2243: `r16Picks[slotId] = storedPick;`
2244: `saveR16Picks(r16Picks);`
2246: `advancementPicks[slotId] = storedPick;`
2247: `saveAdvancementPicks(advancementPicks);`
2253: `window.game1KnockoutPicks = Object.assign({}, window.game1KnockoutPicks || {}, r16Picks || {}, advancementPicks || {});`
2329: `storage: () => ({r16Picks, advancementPicks})`
2384: `storeContract: "wc2026-game1-bracket-picks-v001"`
2387: `if (round === "R16" && typeof r16Picks !== "undefined") {`
2388: `r16Picks[slotId] = stored;`
2389: `if (typeof saveR16Picks === "function") saveR16Picks(r16Picks);`
2390: `} else if ((round === "QF" || round === "SF") && typeof advancementPicks !== "undefined") {`
2391: `advancementPicks[slotId] = stored;`
2392: `if (typeof saveAdvancementPicks === "function") saveAdvancementPicks(advancementPicks);`
2393: `} else if (round === "R32" && typeof picks !== "undefined") {`
2394: `picks[slotId] = stored;`
2395: `if (typeof savePicks === "function") savePicks(picks);`
2403: `|| (typeof r16Picks !== "undefined" ? r16Picks?.[slotId] : null)`
2404: `|| (typeof advancementPicks !== "undefined" ? advancementPicks?.[slotId] : null)`
2405: `|| (typeof picks !== "undefined" ? picks?.[slotId] : null)`
2434: `const legacyR32 = wc2026LegacyJsonForKey("wc2026.game1.r32.picks");`
2439: `|| (typeof picks !== "undefined" ? picks?.[alias] : null)`
2478: `// WC2026_R16_RENDER_SOURCE_GATED: stale R16 picks cannot render before both source R32 picks exist.`
2479: `try { if (typeof r16Picks !== "undefined" && r16Picks) delete r16Picks[rule.slotId]; } catch {}`
2480: `try { if (typeof saveR16Picks === "function" && typeof r16Picks !== "undefined") saveR16Picks(r16Picks); } catch {}`
2501: `// WC2026_ADVANCEMENT_RENDER_SOURCE_GATED: stale QF/SF picks cannot render before both source winners exist.`
2502: `try { if (typeof advancementPicks !== "undefined" && advancementPicks) delete advancementPicks[rule.slotId]; } catch {}`
2503: `try { if (typeof saveAdvancementPicks === "function" && typeof advancementPicks !== "undefined") saveAdvancementPicks(advancementPicks); } catch {}`
2579: `if (round === "R16" && typeof r16Picks !== "undefined") {`
2580: `delete r16Picks[slotId];`
2581: `if (typeof saveR16Picks === "function") saveR16Picks(r16Picks);`
2584: `if ((round === "QF" || round === "SF") && typeof advancementPicks !== "undefined") {`
2585: `delete advancementPicks[slotId];`
2586: `if (typeof saveAdvancementPicks === "function") saveAdvancementPicks(advancementPicks);`
2691: `try { stores.push(picks); } catch {}`
2692: `try { stores.push(r16Picks); } catch {}`
2693: `try { stores.push(advancementPicks); } catch {}`
2694: `try { stores.push(window.game1KnockoutPicks); } catch {}`
2695: `try { stores.push(JSON.parse(localStorage.getItem("wc2026.game1.r32.picks") || "{}")); } catch {}`
2770: `console.info("WC2026 knockout menu blocked until source picks exist", {`
2799: `localStorage.setItem("wc2026.game1.r32.picks", JSON.stringify(nextPicks || {}));`
2819: `picks = {};`
2820: `r16Picks = {};`
2821: `advancementPicks = {};`
2822: `try { window.game1KnockoutPicks = {}; } catch {}`
2832: `"wc2026.game1.r32.picks",`
2837: `"wc2026.game1.picks",`
2840: `"game1KnockoutPicks"`
2850: `console.info("WC2026 Clear picks reset canonical Game 1 state");`
2852: `document.getElementById("exportPicks").addEventListener("click", async () => { const text = JSON.stringify({version:"game1-r32-r16-qf-sf-user-picks-v001", picks, r16WinnerPicks: r16Picks, advancementPicks}, null, 2); try { await navigator.clipboard.writeText(text); alert("Game 1 picks copied to clipboard."); } catch { console.log(text); alert("Could not copy; picks printed to console."); } });`
2901: `window.game1KnockoutPicks,`
2949: `game1KnockoutPicks: window.game1KnockoutPicks,`
2961: `window.game1KnockoutPicks = previous.game1KnockoutPicks;`
3300: `"wc2026.game1.r32.picks",`
3304: `"wc2026.game1.picks",`
3307: `"game1KnockoutPicks"`
3467: `if (value.picks && typeof value.picks === "object") return value.picks;`
3540: `try { delete window.picks?.[id]; } catch {}`
3541: `try { delete window.r16Picks?.[id]; } catch {}`
3542: `try { delete window.advancementPicks?.[id]; } catch {}`
3543: `try { delete window.game1KnockoutPicks?.[id]; } catch {}`
3597: `try { window.picks = {}; } catch {}`
3598: `try { window.r16Picks = {}; } catch {}`
3599: `try { window.advancementPicks = {}; } catch {}`
3600: `try { window.game1KnockoutPicks = {}; } catch {}`
3699: `const r32 = readJson("wc2026.game1.r32.picks");`
3746: `try { if (typeof r16Picks !== "undefined" && r16Picks) delete r16Picks[slotId]; } catch {}`
3747: `try { if (typeof advancementPicks !== "undefined" && advancementPicks) delete advancementPicks[slotId]; } catch {}`
3748: `try { if (window.game1KnockoutPicks) delete window.game1KnockoutPicks[slotId]; } catch {}`
3821: `window.WC2026_TRACE_ASSIGNMENT("Rendered stored knockout picks from site store.", {`
4034: `const R32_KEY = "wc2026.game1.r32.picks";`
4161: `if (typeof r16Picks !== "undefined") r16Picks = stores.r16;`
4162: `if (typeof advancementPicks !== "undefined") advancementPicks = stores.qfSf;`
4163: `if (typeof picks !== "undefined") picks = stores.r32;`
4248: `window.WC2026_TRACE_ASSIGNMENT("Cleared downstream invalid picks.", result);`
4335: `const r32 = readJson("wc2026.game1.r32.picks");`
4345: `writeJson("wc2026.game1.r32.picks", r32);`
4349: `if (typeof picks !== "undefined" && picks) delete picks[slotId];`
4350: `if (typeof r16Picks !== "undefined" && r16Picks) delete r16Picks[slotId];`
4351: `if (typeof advancementPicks !== "undefined" && advancementPicks) delete advancementPicks[slotId];`
4392: `if (typeof savePicks === "function" && typeof picks !== "undefined") savePicks(picks);`
4393: `if (typeof saveR16Picks === "function" && typeof r16Picks !== "undefined") saveR16Picks(r16Picks);`
4394: `if (typeof saveAdvancementPicks === "function" && typeof advancementPicks !== "undefined") saveAdvancementPicks(advancementPicks);`
4412: `const r32 = readJson("wc2026.game1.r32.picks");`
4513: `const r32 = readJson("wc2026.game1.r32.picks");`
4540: `const r32 = readJson("wc2026.game1.r32.picks");`
4552: `if (typeof picks !== "undefined" && picks) delete picks[id];`
4553: `if (typeof r16Picks !== "undefined" && r16Picks) delete r16Picks[id];`
4554: `if (typeof advancementPicks !== "undefined" && advancementPicks) delete advancementPicks[id];`
4560: `writeJson("wc2026.game1.r32.picks", r32);`
4565: `if (typeof savePicks === "function" && typeof picks !== "undefined") savePicks(picks);`
4566: `if (typeof saveR16Picks === "function" && typeof r16Picks !== "undefined") saveR16Picks(r16Picks);`
4567: `if (typeof saveAdvancementPicks === "function" && typeof advancementPicks !== "undefined") saveAdvancementPicks(advancementPicks);`
4637: `window.WC2026_TRACE_ASSIGNMENT("Cleared downstream picks after source clear.", {cleared});`
4652: `- Explicit clear actions may clear downstream picks.`
4734: `const R32_KEY = "wc2026.game1.r32.picks";`
4817: `storeContract: "wc2026-game1-bracket-picks-v001",`
4839: `if (typeof picks !== "undefined" && picks) {`
4840: `picks[slotId] = stored;`
4893: `const R32_KEY = "wc2026.game1.r32.picks";`
5053: `reasons.push(`Team ${key || "unknown"} is not reachable from this slot's immediate feeder picks`);`
5339: `r32: "wc2026.game1.r32.picks",`
5422: `if (round === "R32" && typeof window.picks !== "undefined") window.picks[slotId] = stored;`
5423: `if (round === "R16" && typeof window.r16Picks !== "undefined") window.r16Picks[slotId] = stored;`
5424: `if ((round === "QF" || round === "SF" || round === "FINAL") && typeof window.advancementPicks !== "undefined") window.advancementPicks[slotId] = stored;`
5425: `if (typeof window.game1KnockoutPicks !== "undefined") {`
5426: `window.game1KnockoutPicks = Object.assign({}, window.game1KnockoutPicks || {}, {[slotId]: stored});`

## rendering

94: `.teamTile { display: flex; gap: 10px; align-items: center; width: 100%; text-align: left; border: 1px solid rgba(255,255,255,.18); border-radius: 14px; padding: 10px; background: rgba(255,255,255,.10); color: white; cursor: pointer; }`
95: `.teamTile:hover, .teamTile:focus-visible { outline: 2px solid white; background: rgba(255,255,255,.18); }`
795: `.tapMenu .teamTile {`
801: `.tapMenu .teamTile .teamAbbrOnly {`
924: `.tapMenu .teamTile,`
927: `.choiceMenu .teamTile,`
930: `.choice-menu .teamTile,`
933: `[data-choice-menu] .teamTile,`
940: `.tapMenu .teamTile:hover,`
943: `.choiceMenu .teamTile:hover,`
946: `.choice-menu .teamTile:hover,`
949: `[data-choice-menu] .teamTile:hover,`
1260: `function createHotspots() {`
1379: `function renderPicks() {`
1494: `tile.type = "button"; tile.className = "teamTile";`
1506: `renderPicks(); closeMenu(); }`
1535: `const __wc2026RenderPicksBeforeSlotFit = renderPicks;`
1536: `renderPicks = function renderPicksWithR32SlotFit() {`
1604: `const __wc2026CreateHotspotsBeforeR16 = createHotspots;`
1605: `createHotspots = function createHotspotsWithR16WinnerTargets() {`
1613: `function renderOneR16Pick(rule, pick) {`
1643: `renderOneR16Pick(rule, pick);`
1646: `const __wc2026RenderPicksBeforeR16 = renderPicks;`
1647: `renderPicks = function renderPicksWithR16WinnerPicks() {`
1650: `createHotspots();`
1665: `tile.className = "teamTile";`
1679: `renderPicks();`
1754: `const __wc2026CreateHotspotsBeforeQfSf = createHotspots;`
1755: `createHotspots = function createHotspotsWithQfSfWinnerTargets() {`
1759: `function renderOneAdvancementPick(rule, pick) {`
1789: `renderOneAdvancementPick(rule, pick);`
1792: `const __wc2026RenderPicksBeforeQfSf = renderPicks;`
1793: `renderPicks = function renderPicksWithQfSfWinnerPicks() {`
1796: `createHotspots();`
1811: `tile.className = "teamTile";`
1825: `renderPicks();`
1966: `tile.className = "teamTile";`
2221: `if (typeof renderPicks === "function") renderPicks();`
2226: `if (round === "R16" && typeof renderOneR16Pick === "function") { renderOneR16Pick(renderRule, pick); return true; }`
2227: `if ((round === "QF" || round === "SF") && typeof renderOneAdvancementPick === "function") { renderOneAdvancementPick(renderRule, pick); return true; }`
2263: `tile.className = "teamTile";`
2491: `renderOneR16Pick(rule, pick);`
2514: `renderOneAdvancementPick(rule, pick);`
2640: `clearButton.className = "groupChip clearPickChip teamTile";`
2648: `if (typeof renderPicks === "function") renderPicks();`
2659: `const isCurrentChoice = false; // WC2026_MENU_NO_PRESELECT_HIGHLIGHT`
2662: `tile.className = "teamTile";`
2672: `if (typeof renderPicks === "function") renderPicks();`
2810: `render: () => typeof renderPicks === "function" ? renderPicks() : null,`
2847: `try { if (typeof createHotspots === "function") createHotspots(); } catch {}`
2848: `try { if (typeof renderPicks === "function") renderPicks(); } catch {}`
2853: `createHotspots(); renderPicks();`
3275: `document.querySelectorAll(".teamTile").forEach(tile => {`
3281: `const tile = ev.target && ev.target.closest ? ev.target.closest(".teamTile") : null;`
3756: `function renderStoredR16Picks(){`
3758: `if (typeof renderOneR16Pick !== "function") return [];`
3772: `renderOneR16Pick(rule, pick);`
3785: `function renderStoredAdvancementPicks(){`
3787: `if (typeof renderOneAdvancementPick !== "function") return [];`
3801: `renderOneAdvancementPick(rule, pick);`
3814: `function renderStoredKnockoutPicksFromSiteStore(){`
3817: `const r16Rendered = renderStoredR16Picks();`
3818: `const advancementRendered = renderStoredAdvancementPicks();`
3838: `const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;`
3840: `renderPicks = function renderPicksWithStoredKnockoutPickRenderBridge(){`
3842: `renderStoredKnockoutPicksFromSiteStore();`
3846: `window.WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE = renderStoredKnockoutPicksFromSiteStore;`
3848: `setTimeout(renderStoredKnockoutPicksFromSiteStore, 120);`
3925: `const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;`
3927: `renderPicks = function renderPicksWithPickableFeedbackOnly(){`
3964: `function patchCardText(card, pick){`
3998: `function patchStoredKnockoutCards(){`
4013: `patchCardText(card, pick);`
4017: `const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;`
4019: `renderPicks = function renderPicksWithKnockoutThreeLetterCodes(){`
4021: `patchStoredKnockoutCards();`
4025: `window.WC2026_PATCH_KNOCKOUT_THREE_LETTER_CODES = patchStoredKnockoutCards;`
4026: `setTimeout(patchStoredKnockoutCards, 150);`
4246: `if (typeof renderPicks === "function") renderPicks();`
4396: `if (typeof renderPicks === "function") renderPicks();`
4436: `clearButton.className = "groupChip clearPickChip teamTile";`
4606: `const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;`
4608: `renderPicks = function renderPicksWithRecursiveDownstreamClear(){`
4614: `if (typeof renderPicks === "function") {`
4615: `const fn = renderPicks;`
4616: `if (fn !== renderPicksWithRecursiveDownstreamClear) fn();`
4634: `if (typeof renderPicks === "function") renderPicks();`
4653: `- renderPicks() must never be destructive.`
4657: `if (typeof renderPicks === "function" && !window.WC2026_RENDER_PICKS_NONDESTRUCTIVE_PATCHED) {`
4658: `const currentRenderPicks = renderPicks;`
4660: `renderPicks = function renderPicksNonDestructiveAfterClear(){`
4872: `if (typeof renderPicks === "function") renderPicks();`
5104: `const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;`
5106: `renderPicks = function renderPicksWithBracketPickFinalityValidation(){`
5233: `document.querySelectorAll(".teamTile").forEach(tile => tile.blur());`
5308: `const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;`
5310: `renderPicks = function renderPicksWithFinalityAdornments(){`
5463: `try { if (typeof window.renderPicks === "function") window.renderPicks(); }`
5487: `const siblings = grid ? Array.from(grid.querySelectorAll("button, .teamTile, [role='button']")) : [];`
5502: `const tile = ev.target.closest(".teamTile, .teamChoice, .menuChoice, .countryChoice, [data-team-id], [data-team-abbr]");`
5736: `const ITEM_SELECTOR = ".teamTile, .teamChoice, .menuChoice, .countryChoice, [data-team-id], [data-team-abbr], [data-country-code], [data-code], [role='menuitem']";`

## stored_bridge

3636: `// WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE_START`
3643: `function storedPickForSlot(slotId){`
3763: `const pick = storedPickForSlot(rule.slotId);`
3792: `const pick = storedPickForSlot(rule.slotId);`
3846: `window.WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE = renderStoredKnockoutPicksFromSiteStore;`
3850: `// WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE_END`


# Focused Snippets


## Around `function storedPickForSlot` at line 3643

```js
3631:   };
3632: })();
3633: /* WC2026_GAME1_CANONICAL_PICK_STATE_MODEL_END */
3634: </script>
3635: 
3636: // WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE_START
3637: (function installStoredKnockoutPickRenderBridge(){
3638:   function readJson(key){
3639:     try { return JSON.parse(localStorage.getItem(key) || "{}"); }
3640:     catch { return {}; }
3641:   }
3642: 
3643:   function storedPickForSlot(slotId){
3644:     const bracket = readJson("wc2026.game1.bracketPicks");
3645:     const r16 = readJson("wc2026.game1.r16.winnerPicks");
3646:     const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
3647:     return bracket[slotId] || r16[slotId] || qfSf[slotId] || null;
3648:   }
3649: 
3650:   // WC2026_SOURCE_GATE_STORED_KNOCKOUT_RENDER
3651:   function writeJson(key, value){
3652:     try { localStorage.setItem(key, JSON.stringify(value || {})); } catch {}
3653:   }
3654: 
3655:   function r32ManifestToCanonical(slotId){
3656:     const match = String(slotId || "").match(/^R32-([LR])-M(\d+)([AB])$/i);
3657:     if (!match) return slotId;
3658:     const side = match[1].toUpperCase();
3659:     const matchIndex = Number(match[2]);
3660:     const offset = match[3].toUpperCase() === "A" ? 1 : 2;
3661:     return `${side}-R32-${String(((matchIndex - 1) * 2) + offset).padStart(2, "0")}`;
3662:   }
3663: 
3664:   function r32CanonicalToManifest(slotId){
3665:     const match = String(slotId || "").match(/^([LR])-R32-(\d+)$/i);
3666:     if (!match) return slotId;
3667:     const side = match[1].toUpperCase();
3668:     const index = Number(match[2]);
3669:     return `R32-${side}-M${Math.ceil(index / 2)}${index % 2 === 1 ? "A" : "B"}`;
3670:   }
3671: 
3672:   function slotAliases(slotId){
3673:     const ids = new Set();
3674:     const id = String(slotId || "");
3675:     if (!id) return [];
3676:     ids.add(id);
3677:     ids.add(id.toUpperCase());
```

## Around `function renderStoredR16Picks` at line 3756

```js
3744:     writeJson("wc2026.game1.knockoutPicks", knockout);
3745: 
3746:     try { if (typeof r16Picks !== "undefined" && r16Picks) delete r16Picks[slotId]; } catch {}
3747:     try { if (typeof advancementPicks !== "undefined" && advancementPicks) delete advancementPicks[slotId]; } catch {}
3748:     try { if (window.game1KnockoutPicks) delete window.game1KnockoutPicks[slotId]; } catch {}
3749:     try { window.WC2026_GAME1_BRACKET_PICK_STORE_API?.clear?.(slotId); } catch {}
3750:   }
3751: 
3752:   function removeExistingStoredCards(){
3753:     document.querySelectorAll(".storedKnockoutPickCard").forEach(el => el.remove());
3754:   }
3755: 
3756:   function renderStoredR16Picks(){
3757:     if (typeof r16SlotRulesFromManifest !== "function") return [];
3758:     if (typeof renderOneR16Pick !== "function") return [];
3759: 
3760:     const rendered = [];
3761: 
3762:     r16SlotRulesFromManifest().forEach(rule => {
3763:       const pick = storedPickForSlot(rule.slotId);
3764:       if (!storedKnockoutPickIsRenderable(rule, pick)) {
3765:         clearInvalidStoredKnockoutPick(rule);
3766:         return;
3767:       }
3768: 
3769:       const before = Array.from(document.querySelectorAll(`.r16PickCard[data-slot-id="${rule.slotId}"]`));
3770:       before.forEach(el => el.remove());
3771: 
3772:       renderOneR16Pick(rule, pick);
3773: 
3774:       const card = document.querySelector(`.r16PickCard[data-slot-id="${rule.slotId}"]`);
3775:       if (card) {
3776:         card.classList.add("storedKnockoutPickCard");
3777:         card.dataset.renderSource = "site-bracket-pick-store";
3778:         rendered.push({slotId: rule.slotId, text: card.innerText});
3779:       }
3780:     });
3781: 
3782:     return rendered;
3783:   }
3784: 
3785:   function renderStoredAdvancementPicks(){
3786:     if (typeof advancementSlotRulesFromManifest !== "function") return [];
3787:     if (typeof renderOneAdvancementPick !== "function") return [];
3788: 
3789:     const rendered = [];
3790: 
```

## Around `function renderStoredAdvancementPicks` at line 3785

```js
3773: 
3774:       const card = document.querySelector(`.r16PickCard[data-slot-id="${rule.slotId}"]`);
3775:       if (card) {
3776:         card.classList.add("storedKnockoutPickCard");
3777:         card.dataset.renderSource = "site-bracket-pick-store";
3778:         rendered.push({slotId: rule.slotId, text: card.innerText});
3779:       }
3780:     });
3781: 
3782:     return rendered;
3783:   }
3784: 
3785:   function renderStoredAdvancementPicks(){
3786:     if (typeof advancementSlotRulesFromManifest !== "function") return [];
3787:     if (typeof renderOneAdvancementPick !== "function") return [];
3788: 
3789:     const rendered = [];
3790: 
3791:     advancementSlotRulesFromManifest().forEach(rule => {
3792:       const pick = storedPickForSlot(rule.slotId);
3793:       if (!storedKnockoutPickIsRenderable(rule, pick)) {
3794:         clearInvalidStoredKnockoutPick(rule);
3795:         return;
3796:       }
3797: 
3798:       const before = Array.from(document.querySelectorAll(`.advancePickCard[data-slot-id="${rule.slotId}"]`));
3799:       before.forEach(el => el.remove());
3800: 
3801:       renderOneAdvancementPick(rule, pick);
3802: 
3803:       const card = document.querySelector(`.advancePickCard[data-slot-id="${rule.slotId}"]`);
3804:       if (card) {
3805:         card.classList.add("storedKnockoutPickCard");
3806:         card.dataset.renderSource = "site-bracket-pick-store";
3807:         rendered.push({slotId: rule.slotId, text: card.innerText});
3808:       }
3809:     });
3810: 
3811:     return rendered;
3812:   }
3813: 
3814:   function renderStoredKnockoutPicksFromSiteStore(){
3815:     removeExistingStoredCards();
3816: 
3817:     const r16Rendered = renderStoredR16Picks();
3818:     const advancementRendered = renderStoredAdvancementPicks();
3819: 
```

## Around `function patchStoredKnockoutCards` at line 3998

```js
3986:         codeEl = document.createElement("span");
3987:         codeEl.className = "pickCode";
3988:         pickText.appendChild(codeEl);
3989:       }
3990:     }
3991: 
3992:     if (codeEl) codeEl.textContent = "";
3993: 
3994:     card.dataset.tooltip = `${name}\n${code}`;
3995:     card.setAttribute("aria-label", `${name} (${code}) selected for ${card.dataset.slotId || "slot"}. Click or tap to change winner.`);
3996:   }
3997: 
3998:   function patchStoredKnockoutCards(){
3999:     let bracket = {};
4000:     let r16 = {};
4001:     let qfSf = {};
4002:     try { bracket = JSON.parse(localStorage.getItem("wc2026.game1.bracketPicks") || "{}"); } catch {}
4003:     try { r16 = JSON.parse(localStorage.getItem("wc2026.game1.r16.winnerPicks") || "{}"); } catch {}
4004:     try { qfSf = JSON.parse(localStorage.getItem("wc2026.game1.qfSf.winnerPicks") || "{}"); } catch {}
4005: 
4006:     document.querySelectorAll(".r16PickCard, .advancePickCard").forEach(card => {
4007:       const slotId = card.dataset.slotId;
4008:       const pick = bracket[slotId] || r16[slotId] || qfSf[slotId] || null;
4009:       if (!pick) return;
4010:       const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;
4011:       const rule = api && typeof api.slotById === "function" ? api.slotById(slotId) : null;
4012:       if (rule && typeof storedKnockoutPickIsRenderable === "function" && !storedKnockoutPickIsRenderable(rule, pick)) return;
4013:       patchCardText(card, pick);
4014:     });
4015:   }
4016: 
4017:   const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;
4018:   if (previousRenderPicks) {
4019:     renderPicks = function renderPicksWithKnockoutThreeLetterCodes(){
4020:       previousRenderPicks();
4021:       patchStoredKnockoutCards();
4022:     };
4023:   }
4024: 
4025:   window.WC2026_PATCH_KNOCKOUT_THREE_LETTER_CODES = patchStoredKnockoutCards;
4026:   setTimeout(patchStoredKnockoutCards, 150);
4027: })();
4028: // WC2026_KNOCKOUT_RENDER_THREE_LETTER_CODE_END
4029: 
4030: 
4031: // WC2026_DOWNSTREAM_CLEAR_INTEGRITY_START
4032: (function installDownstreamClearIntegrity(){
```

## Around `function renderPicks` at line 1379

```js
1367:         implementationLabelsHidden: true,
1368:         geometrySource: "uniform-svg-manifest-position-map"
1369:       };
1370:       const board = document.querySelector(".pixelNativeBoardPlane") || document.querySelector(".board") || document.body;
1371:       if (board) {
1372:         board.dataset.r32RuleHitIntegrity = ok ? "pass" : "fail";
1373:         board.dataset.implementationLabelsHidden = "true";
1374:       }
1375:       if (!ok) console.warn("WC2026 Game 1 R32 rule/hit integrity check failed", window.WC2026_GAME1_R32_RULE_HIT_INTEGRITY);
1376:       return window.WC2026_GAME1_R32_RULE_HIT_INTEGRITY;
1377:     }
1378: 
1379:     function renderPicks() {
1380:       hidePickDetails();
1381:       pickLayer.innerHTML = "";
1382:       SLOT_RULES.forEach(rule => {
1383:         const pick = picks[rule.slotId];
1384:         if (!pick) return;
1385:         const box = computePickCardBox(rule, pick);
1386:         const card = document.createElement("button");
1387:         card.type = "button";
1388:         card.className = "pickCard";
1389:         card.style.left = cssPx(box.left);
1390:         card.style.top = cssPx(box.top);
1391:         card.style.width = cssPx(box.width);
1392:         card.style.height = cssPx(box.height);
1393:         card.dataset.slotId = rule.slotId;
1394:         card.setAttribute("aria-label", `${r32PickFullName(pick)}. Team abbreviation ${r32TeamAbbreviation(pick)}. ${rule.slotRuleLong}. Click or tap to change pick.`);
1395:         const pickFlag = document.createElement("span");
1396:         pickFlag.className = "pickFlag";
1397:         pickFlag.textContent = pick.flagEmoji || pick.flag || "⚽";
1398:         const pickText = document.createElement("span");
1399:         pickText.className = "pickText";
1400:         const pickName = document.createElement("span");
1401:         pickName.className = "pickName";
1402:         pickName.textContent = r32TeamAbbreviation(pick);
1403:         const pickRule = document.createElement("span");
1404:         pickRule.className = "pickRule"; pickRule.hidden = true; pickRule.setAttribute("aria-hidden", "true");
1405:         pickRule.textContent = rule.slotRule;
1406:         pickText.appendChild(pickName);
1407:         pickText.appendChild(pickRule);
1408:         card.replaceChildren(pickFlag, pickText);
1409:         card.addEventListener("pointerenter", () => showPickDetails(card, rule, pick));
1410:         card.addEventListener("pointerleave", hidePickDetails);
1411:         card.addEventListener("focus", () => showPickDetails(card, rule, pick));
1412:         card.addEventListener("blur", hidePickDetails);
1413:         card.addEventListener("click", ev => openMenuForResolvedGame1R32Rule(rule, ev));
```

## Around `function renderPicks` at line 1536

```js
1524:         if (!rule || !rule.boundsPx) return;
1525:         const b = rule.boundsPx;
1526:         card.dataset.slotId = rule.slotId;
1527:         card.dataset.r32SlotFit = "true";
1528:         card.style.left = cssPx(b.x);
1529:         card.style.top = cssPx(b.y);
1530:         card.style.width = cssPx(b.w);
1531:         card.style.height = cssPx(b.h);
1532:       });
1533:       fitR32PickCardNames();
1534:     }
1535:     const __wc2026RenderPicksBeforeSlotFit = renderPicks;
1536:     renderPicks = function renderPicksWithR32SlotFit() {
1537:       __wc2026RenderPicksBeforeSlotFit();
1538:       enforceR32PickCardSlotFit();
1539:     };
1540: 
1541: 
1542: 
1543:     // WC2026_GAME1_R16_WINNER_PICKS
1544:     const R16_STORAGE_KEY = "wc2026.game1.r16.winnerPicks";
1545:     function loadR16Picks() { try { return JSON.parse(localStorage.getItem(R16_STORAGE_KEY) || "{}"); } catch { return {}; } }
1546:     function saveR16Picks(value) { localStorage.setItem(R16_STORAGE_KEY, JSON.stringify(value)); }
1547:     let r16Picks = loadR16Picks();
1548:     function uniformGameboardManifest() {
1549:       return window.WC2026_UNIFORM_PICK_CARD_GAMEBOARD_MANIFEST || window.WC2026_UNIFORM_SVG_GAMEBOARD_MANIFEST || null;
1550:     }
1551:     function normalizeManifestBounds(bounds) {
1552:       if (!bounds) return null;
1553:       return { x: bounds.x, y: bounds.y, w: bounds.w ?? bounds.width, h: bounds.h ?? bounds.height };
1554:     }
1555:     function r16SlotRulesFromManifest() {
1556:       const manifest = uniformGameboardManifest();
1557:       const slots = Array.isArray(manifest?.slots) ? manifest.slots : [];
1558:       return slots
1559:         .filter(slot => slot.round === "R16")
1560:         .map(slot => {
1561:           const side = slot.side || (String(slot.slotId || "").startsWith("R-") ? "right" : "left");
1562:           const index = Number(slot.roundIndex || String(slot.slotId || "").match(/(\d+)$/)?.[1] || 0);
1563:           const prefix = side === "right" ? "R" : "L";
1564:           const a = `${prefix}-R32-${String((index * 2) - 1).padStart(2, "0")}`;
1565:           const b = `${prefix}-R32-${String(index * 2).padStart(2, "0")}`;
1566:           return {
1567:             slotId: slot.slotId,
1568:             logicalId: slot.slotId,
1569:             round: "R16",
1570:             side,
```

## Around `function renderPicks` at line 1647

```js
1635:       card.addEventListener("click", ev => openR16Menu(rule, ev));
1636:       pickLayer.appendChild(card);
1637:       requestAnimationFrame(() => fitPickCardName(card));
1638:     }
1639:     function renderR16Picks() {
1640:       r16SlotRulesFromManifest().forEach(rule => {
1641:         const pick = r16Picks[rule.slotId];
1642:         if (!pick) return;
1643:         renderOneR16Pick(rule, pick);
1644:       });
1645:     }
1646:     const __wc2026RenderPicksBeforeR16 = renderPicks;
1647:     renderPicks = function renderPicksWithR16WinnerPicks() {
1648:       __wc2026RenderPicksBeforeR16();
1649:       renderR16Picks();
1650:       createHotspots();
1651:     };
1652:     function openR16Menu(rule, ev) {
1653:       wc2026CloseAllTooltipSurfacesForMenu();
1654:       activeSlot = rule;
1655:       const teams = r16CandidateTeams(rule);
1656:       if (teams.length !== 2) return;
1657:       menu.dataset.mode = "r16";
1658:       menuTitle.textContent = "Pick Round of 16 winner";
1659:       menuSub.textContent = rule.slotRuleLong;
1660:       groupChips.innerHTML = "";
1661:       teamGrid.innerHTML = "";
1662:       teams.forEach(team => {
1663:         const tile = document.createElement("button");
1664:         tile.type = "button";
1665:         tile.className = "teamTile";
1666:         tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
1667:         tile.addEventListener("click", () => assignR16Winner(team));
1668:         teamGrid.appendChild(tile);
1669:       });
1670:       const left = Math.min(window.innerWidth - 580, Math.max(16, ev.clientX + 18));
1671:       const top = Math.min(window.innerHeight - 520, Math.max(16, ev.clientY - 24));
1672:       menu.style.left = `${left}px`; menu.style.top = `${top}px`;
1673:       backdrop.classList.add("isOpen"); menu.classList.add("isOpen");
1674:     }
1675:     function assignR16Winner(team) {
1676:       if (!activeSlot || activeSlot.round !== "R16") return;
1677:       r16Picks[activeSlot.slotId] = { ...team, assignedSlotId: activeSlot.slotId, round: "R16", sourceR32SlotIds: activeSlot.sourceR32SlotIds, slotRule: activeSlot.slotRule, slotRuleLong: activeSlot.slotRuleLong };
1678:       saveR16Picks(r16Picks);
1679:       renderPicks();
1680:       closeMenu();
1681:     }
```

## Around `function renderPicks` at line 1793

```js
1781:       card.addEventListener("click", ev => openAdvancementMenu(rule, ev));
1782:       pickLayer.appendChild(card);
1783:       requestAnimationFrame(() => fitPickCardName(card));
1784:     }
1785:     function renderAdvancementPicks() {
1786:       advancementSlotRulesFromManifest().forEach(rule => {
1787:         const pick = advancementPicks[rule.slotId];
1788:         if (!pick) return;
1789:         renderOneAdvancementPick(rule, pick);
1790:       });
1791:     }
1792:     const __wc2026RenderPicksBeforeQfSf = renderPicks;
1793:     renderPicks = function renderPicksWithQfSfWinnerPicks() {
1794:       __wc2026RenderPicksBeforeQfSf();
1795:       renderAdvancementPicks();
1796:       createHotspots();
1797:     };
1798:     function openAdvancementMenu(rule, ev) {
1799:       wc2026CloseAllTooltipSurfacesForMenu();
1800:       activeSlot = rule;
1801:       const teams = advancementCandidateTeams(rule);
1802:       if (teams.length !== 2) return;
1803:       menu.dataset.mode = "advance";
1804:       menuTitle.textContent = `Pick ${rule.round} winner`;
1805:       menuSub.textContent = rule.slotRuleLong;
1806:       groupChips.innerHTML = "";
1807:       teamGrid.innerHTML = "";
1808:       teams.forEach(team => {
1809:         const tile = document.createElement("button");
1810:         tile.type = "button";
1811:         tile.className = "teamTile";
1812:         tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
1813:         tile.addEventListener("click", () => assignAdvancementWinner(team));
1814:         teamGrid.appendChild(tile);
1815:       });
1816:       const left = Math.min(window.innerWidth - 580, Math.max(16, ev.clientX + 18));
1817:       const top = Math.min(window.innerHeight - 520, Math.max(16, ev.clientY - 24));
1818:       menu.style.left = `${left}px`; menu.style.top = `${top}px`;
1819:       backdrop.classList.add("isOpen"); menu.classList.add("isOpen");
1820:     }
1821:     function assignAdvancementWinner(team) {
1822:       if (!activeSlot || (activeSlot.round !== "QF" && activeSlot.round !== "SF")) return;
1823:       advancementPicks[activeSlot.slotId] = { ...team, assignedSlotId: activeSlot.slotId, round: activeSlot.round, sourceSlotIds: activeSlot.sourceSlotIds, slotRule: activeSlot.slotRule, slotRuleLong: activeSlot.slotRuleLong };
1824:       saveAdvancementPicks(advancementPicks);
1825:       renderPicks();
1826:       closeMenu();
1827:     }
```

## Around `function renderPicks` at line 3840

```js
3828:           text: el.innerText,
3829:           left: el.style.left,
3830:           top: el.style.top
3831:         }))
3832:       });
3833:     }
3834: 
3835:     return {r16Rendered, advancementRendered};
3836:   }
3837: 
3838:   const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;
3839:   if (previousRenderPicks) {
3840:     renderPicks = function renderPicksWithStoredKnockoutPickRenderBridge(){
3841:       previousRenderPicks();
3842:       renderStoredKnockoutPicksFromSiteStore();
3843:     };
3844:   }
3845: 
3846:   window.WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE = renderStoredKnockoutPicksFromSiteStore;
3847: 
3848:   setTimeout(renderStoredKnockoutPicksFromSiteStore, 120);
3849: })();
3850: // WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE_END
3851: 
3852: 
3853: 
3854: 
3855: // WC2026_R32_CARD_DISPLAY_NAME_SHIM_START
3856: (function installR32CardDisplayNameShim(){
3857:   if (typeof window.r32CardDisplayName === "function") return;
3858: 
3859:   window.r32CardDisplayName = function r32CardDisplayName(pick){
3860:     if (!pick) return "";
3861:     return (
3862:       pick.display ||
3863:       pick.displayName ||
3864:       pick.displayNameFromImage ||
3865:       pick.name ||
3866:       pick.abbr ||
3867:       "Pick"
3868:     );
3869:   };
3870: })();
3871: // WC2026_R32_CARD_DISPLAY_NAME_SHIM_END
3872: 
3873: 
3874: // WC2026_PICKABLE_FEEDBACK_ONLY_RUNTIME_START
```

## Around `function renderPicks` at line 3927

```js
3915:       if (round === "R32") {
3916:         card.dataset.canPick = "true";
3917:         return;
3918:       }
3919: 
3920:       const rule = ruleForCard(card);
3921:       card.dataset.canPick = canPickForRule(rule) ? "true" : "false";
3922:     });
3923:   }
3924: 
3925:   const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;
3926:   if (previousRenderPicks) {
3927:     renderPicks = function renderPicksWithPickableFeedbackOnly(){
3928:       previousRenderPicks();
3929:       markPickableFeedback();
3930:     };
3931:   }
3932: 
3933:   document.addEventListener("mouseover", markPickableFeedback, true);
3934:   document.addEventListener("focusin", markPickableFeedback, true);
3935: 
3936:   window.WC2026_MARK_PICKABLE_FEEDBACK = markPickableFeedback;
3937:   setTimeout(markPickableFeedback, 120);
3938: })();
3939: // WC2026_PICKABLE_FEEDBACK_ONLY_RUNTIME_END
3940: 
3941: 
3942: // WC2026_KNOCKOUT_RENDER_THREE_LETTER_CODE_START
3943: (function installKnockoutThreeLetterCodeRender(){
3944:   function threeLetterCode(pick){
3945:     return String(
3946:       pick?.abbr ||
3947:       pick?.code ||
3948:       pick?.teamCode ||
3949:       pick?.fifaCode ||
3950:       ""
3951:     ).trim().toUpperCase().slice(0, 3);
3952:   }
3953: 
3954:   function compactPickLabel(pick){
3955:     return threeLetterCode(pick) || (
3956:       pick?.display ||
3957:       pick?.displayName ||
3958:       pick?.displayNameFromImage ||
3959:       pick?.name ||
3960:       "PICK"
3961:     );
```

## Around `function renderPicks` at line 4019

```js
4007:       const slotId = card.dataset.slotId;
4008:       const pick = bracket[slotId] || r16[slotId] || qfSf[slotId] || null;
4009:       if (!pick) return;
4010:       const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;
4011:       const rule = api && typeof api.slotById === "function" ? api.slotById(slotId) : null;
4012:       if (rule && typeof storedKnockoutPickIsRenderable === "function" && !storedKnockoutPickIsRenderable(rule, pick)) return;
4013:       patchCardText(card, pick);
4014:     });
4015:   }
4016: 
4017:   const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;
4018:   if (previousRenderPicks) {
4019:     renderPicks = function renderPicksWithKnockoutThreeLetterCodes(){
4020:       previousRenderPicks();
4021:       patchStoredKnockoutCards();
4022:     };
4023:   }
4024: 
4025:   window.WC2026_PATCH_KNOCKOUT_THREE_LETTER_CODES = patchStoredKnockoutCards;
4026:   setTimeout(patchStoredKnockoutCards, 150);
4027: })();
4028: // WC2026_KNOCKOUT_RENDER_THREE_LETTER_CODE_END
4029: 
4030: 
4031: // WC2026_DOWNSTREAM_CLEAR_INTEGRITY_START
4032: (function installDownstreamClearIntegrity(){
4033:   const BRACKET_KEY = "wc2026.game1.bracketPicks";
4034:   const R32_KEY = "wc2026.game1.r32.picks";
4035:   const R16_KEY = "wc2026.game1.r16.winnerPicks";
4036:   const QFSF_KEY = "wc2026.game1.qfSf.winnerPicks";
4037:   const LOCK_KEY = "wc2026.game1.choiceLockState";
4038: 
4039:   function readJson(key){
4040:     try { return JSON.parse(localStorage.getItem(key) || "{}"); }
4041:     catch { return {}; }
4042:   }
4043: 
4044:   function writeJson(key, value){
4045:     localStorage.setItem(key, JSON.stringify(value || {}));
4046:     return value || {};
4047:   }
4048: 
4049:   function teamKey(pick){
4050:     return String(pick?.abbr || pick?.code || pick?.teamCode || pick?.fifaCode || pick?.display || pick?.name || "")
4051:       .trim()
4052:       .toUpperCase();
4053:   }
```

## Around `function renderPicks` at line 4608

```js
4596:           missingSources: missing,
4597:           reason: "missing-upstream-source"
4598:         });
4599:         changed = true;
4600:       });
4601:     }
4602: 
4603:     return cleared;
4604:   }
4605: 
4606:   const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;
4607:   if (previousRenderPicks) {
4608:     renderPicks = function renderPicksWithRecursiveDownstreamClear(){
4609:       const cleared = clearInvalidDownstreamPicks();
4610:       previousRenderPicks();
4611: 
4612:       if (cleared.length) {
4613:         setTimeout(() => {
4614:           if (typeof renderPicks === "function") {
4615:             const fn = renderPicks;
4616:             if (fn !== renderPicksWithRecursiveDownstreamClear) fn();
4617:           }
4618:         }, 0);
4619:       }
4620: 
4621:       return cleared;
4622:     };
4623:   }
4624: 
4625:   document.addEventListener("click", function(ev){
4626:     const clearClicked = ev.target && ev.target.closest
4627:       ? ev.target.closest(".clearPickChip, [data-clear-r32-slot-id]")
4628:       : null;
4629: 
4630:     if (!clearClicked) return;
4631: 
4632:     setTimeout(() => {
4633:       const cleared = clearInvalidDownstreamPicks();
4634:       if (typeof renderPicks === "function") renderPicks();
4635: 
4636:       if (cleared.length && typeof window.WC2026_TRACE_ASSIGNMENT === "function") {
4637:         window.WC2026_TRACE_ASSIGNMENT("Cleared downstream picks after source clear.", {cleared});
4638:       }
4639:     }, 50);
4640:   }, true);
4641: 
4642:   window.WC2026_CLEAR_INVALID_DOWNSTREAM_PICKS = clearInvalidDownstreamPicks;
```

## Around `function renderPicks` at line 4660

```js
4648: // WC2026_DISABLE_RENDER_TIME_DOWNSTREAM_CLEAR_START
4649: (function disableRenderTimeDownstreamClear(){
4650:   /*
4651:     Integrity rule:
4652:     - Explicit clear actions may clear downstream picks.
4653:     - renderPicks() must never be destructive.
4654:     This prevents a newly selected choice from being erased during the render cycle.
4655:   */
4656: 
4657:   if (typeof renderPicks === "function" && !window.WC2026_RENDER_PICKS_NONDESTRUCTIVE_PATCHED) {
4658:     const currentRenderPicks = renderPicks;
4659: 
4660:     renderPicks = function renderPicksNonDestructiveAfterClear(){
4661:       return currentRenderPicks();
4662:     };
4663: 
4664:     window.WC2026_RENDER_PICKS_NONDESTRUCTIVE_PATCHED = true;
4665:   }
4666: 
4667:   window.WC2026_DOWNSTREAM_CLEAR_POLICY = {
4668:     mode: "explicit-clear-only",
4669:     renderIsDestructive: false
4670:   };
4671: })();
4672: // WC2026_DISABLE_RENDER_TIME_DOWNSTREAM_CLEAR_END
4673: 
4674: 
4675: // WC2026_R32_PROJECTION_UNTIL_FIFA_LOCK_RUNTIME_START
4676: (function installR32ProjectionUntilFifaLockRuntime(){
4677:   const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;
4678: 
4679:   function state(){
4680:     if (api && typeof api.loadR32AssignmentState === "function") return api.loadR32AssignmentState();
4681:     return {state:"projection", locked:false, source:null, label:"R32 projection: editable until FIFA lock"};
4682:   }
4683: 
4684:   function applyR32AssignmentStateToUI(){
4685:     const current = state();
4686:     document.body.dataset.r32AssignmentState = current.state || "projection";
4687:     document.body.dataset.r32Locked = current.locked ? "true" : "false";
4688: 
4689:     const title = document.querySelector("h1") || document.querySelector("header h1") || document.querySelector(".title");
4690:     if (!title) return current;
4691: 
4692:     let pill = document.getElementById("r32AssignmentPhasePill");
4693:     if (!pill) {
4694:       pill = document.createElement("span");
```

## Around `function renderPicks` at line 5106

```js
5094:       const slotId = card.dataset.slotId || card.dataset.assignmentTargetSlotId || "";
5095:       const result = validateBracketPickFinality(slotId);
5096:       card.dataset.choiceCanRemainFinal = result.canRemainFinal ? "true" : "false";
5097:       card.dataset.choiceCanBeFinal = result.canRemainFinal ? "true" : "false";
5098:       card.dataset.choiceState = result.state;
5099:       card.dataset.choiceFinalityReason = result.reasons.join(" | ");
5100:       card.dataset.choiceFinalityTeam = result.teamKey || "";
5101:     });
5102:   }
5103: 
5104:   const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;
5105:   if (previousRenderPicks && !window.WC2026_BRACKET_PICK_FINALITY_RENDER_PATCHED) {
5106:     renderPicks = function renderPicksWithBracketPickFinalityValidation(){
5107:       const result = previousRenderPicks();
5108:       markBracketPickFinality();
5109:       return result;
5110:     };
5111:     window.WC2026_BRACKET_PICK_FINALITY_RENDER_PATCHED = true;
5112:   }
5113: 
5114:   window.WC2026_VALIDATE_BRACKET_PICK_FINALITY = validateBracketPickFinality;
5115:   window.WC2026_VALIDATE_ALL_BRACKET_PICK_FINALITY = validateAllBracketPickFinality;
5116:   window.WC2026_MARK_BRACKET_PICK_FINALITY = markBracketPickFinality;
5117: 
5118:   setTimeout(markBracketPickFinality, 150);
5119: })();
5120: // WC2026_BRACKET_PICK_FINALITY_VALIDATION_END
5121: 
5122: 
5123: // WC2026_HARD_DISABLE_TOOLTIP_SURFACES_RUNTIME_START
5124: (function hardDisableTooltipSurfacesRuntime(){
5125:   function killTooltips(){
5126:     document.body.classList.remove("wb-side-tooltip-open");
5127: 
5128:     document.querySelectorAll([
5129:       ".r32PickDetails",
5130:       "#r32PickDetails",
5131:       "#wb-side-tooltip",
5132:       ".wb-side-tooltip",
5133:       ".sideTooltip",
5134:       ".r32Tooltip",
5135:       ".slotTooltip",
5136:       ".pickTooltip",
5137:       ".teamTooltip",
5138:       ".legacyTooltip",
5139:       ".tooltip",
5140:       "[role='tooltip']",
```

## Around `function renderPicks` at line 5310

```js
5298:       card.removeAttribute("title");
5299:       card.dataset.tooltip = "";
5300: 
5301:       if (canRemainFinal === "false") {
5302:         const reason = card.getAttribute("data-choice-finality-reason") || "not final eligible";
5303:         card.setAttribute("aria-label", `${card.getAttribute("aria-label") || card.textContent || "Pick"} — not final eligible: ${reason}`);
5304:       }
5305:     });
5306:   }
5307: 
5308:   const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;
5309:   if (previousRenderPicks && !window.WC2026_FINALITY_RENDER_WRAPPED) {
5310:     renderPicks = function renderPicksWithFinalityAdornments(){
5311:       const result = previousRenderPicks();
5312:       adornPickFinality();
5313:       return result;
5314:     };
5315:     window.WC2026_FINALITY_RENDER_WRAPPED = true;
5316:   }
5317: 
5318:   document.addEventListener("click", () => setTimeout(adornPickFinality, 0), true);
5319:   document.addEventListener("change", () => setTimeout(adornPickFinality, 0), true);
5320:   window.addEventListener("storage", () => setTimeout(adornPickFinality, 0));
5321: 
5322:   window.WC2026_ADORN_PICK_FINALITY = adornPickFinality;
5323: 
5324:   setTimeout(adornPickFinality, 0);
5325:   setTimeout(adornPickFinality, 250);
5326: })();
5327: // WC2026_RUN_FINALITY_CHECK_DURING_PICK_RENDER_END
5328: 
5329: </script>
5330: 
5331: 
5332: <script>
5333: // WC2026_PAGES_REVIEW_PICK_ACCEPTANCE_START
5334: (function installPagesReviewPickAcceptance(){
5335:   if (window.WC2026_PAGES_REVIEW_PICK_ACCEPTANCE?.installed) return;
5336: 
5337:   const STORAGE = {
5338:     bracket: "wc2026.game1.bracketPicks",
5339:     r32: "wc2026.game1.r32.picks",
5340:     r16: "wc2026.game1.r16.winnerPicks",
5341:     advance: "wc2026.game1.qfSf.winnerPicks"
5342:   };
5343: 
5344:   function readJson(key){
```

## Around `function renderOneR16Pick` at line 1613

```js
1601:         hitLayer.appendChild(btn);
1602:       });
1603:     }
1604:     const __wc2026CreateHotspotsBeforeR16 = createHotspots;
1605:     createHotspots = function createHotspotsWithR16WinnerTargets() {
1606:       __wc2026CreateHotspotsBeforeR16();
1607:       createR16Hotspots();
1608:     };
1609:     function computeManifestPickCardBox(rule) {
1610:       const b = rule.boundsPx;
1611:       return { left: b.x, top: b.y, width: b.w, height: b.h };
1612:     }
1613:     function renderOneR16Pick(rule, pick) {
1614:       const box = computeManifestPickCardBox(rule);
1615:       const card = document.createElement("button");
1616:       card.type = "button";
1617:       card.className = "pickCard r16PickCard";
1618:       card.style.left = cssPx(box.left);
1619:       card.style.top = cssPx(box.top);
1620:       card.style.width = cssPx(box.width);
1621:       card.style.height = cssPx(box.height);
1622:       card.dataset.slotId = rule.slotId;
1623:       card.dataset.round = "R16";
1624:       card.setAttribute("aria-label", `${displayName(pick)} selected as ${rule.slotRuleLong}. Click or tap to change winner.`);
1625:       const pickFlag = document.createElement("span");
1626:       pickFlag.className = "pickFlag";
1627:       pickFlag.textContent = pick.flagEmoji || pick.flag || "⚽";
1628:       const pickText = document.createElement("span");
1629:       pickText.className = "pickText";
1630:       const pickName = document.createElement("span");
1631:       pickName.className = "pickName";
1632:       pickName.textContent = r32CardDisplayName(pick);
1633:       pickText.appendChild(pickName);
1634:       card.replaceChildren(pickFlag, pickText);
1635:       card.addEventListener("click", ev => openR16Menu(rule, ev));
1636:       pickLayer.appendChild(card);
1637:       requestAnimationFrame(() => fitPickCardName(card));
1638:     }
1639:     function renderR16Picks() {
1640:       r16SlotRulesFromManifest().forEach(rule => {
1641:         const pick = r16Picks[rule.slotId];
1642:         if (!pick) return;
1643:         renderOneR16Pick(rule, pick);
1644:       });
1645:     }
1646:     const __wc2026RenderPicksBeforeR16 = renderPicks;
1647:     renderPicks = function renderPicksWithR16WinnerPicks() {
```

## Around `function renderOneAdvancementPick` at line 1759

```js
1747:         btn.dataset.round = rule.round;
1748:         btn.disabled = candidates.length !== 2;
1749:         btn.setAttribute("aria-label", candidates.length === 2 ? `${rule.slotRuleLong}. Pick winner.` : `${rule.slotRuleLong}. Waiting for both source winners.`);
1750:         btn.addEventListener("click", ev => openAdvancementMenu(rule, ev));
1751:         hitLayer.appendChild(btn);
1752:       });
1753:     }
1754:     const __wc2026CreateHotspotsBeforeQfSf = createHotspots;
1755:     createHotspots = function createHotspotsWithQfSfWinnerTargets() {
1756:       __wc2026CreateHotspotsBeforeQfSf();
1757:       createAdvancementHotspots();
1758:     };
1759:     function renderOneAdvancementPick(rule, pick) {
1760:       const box = computeManifestPickCardBox(rule);
1761:       const card = document.createElement("button");
1762:       card.type = "button";
1763:       card.className = "pickCard advancePickCard";
1764:       card.style.left = cssPx(box.left);
1765:       card.style.top = cssPx(box.top);
1766:       card.style.width = cssPx(box.width);
1767:       card.style.height = cssPx(box.height);
1768:       card.dataset.slotId = rule.slotId;
1769:       card.dataset.round = rule.round;
1770:       card.setAttribute("aria-label", `${displayName(pick)} selected as ${rule.slotRuleLong}. Click or tap to change winner.`);
1771:       const pickFlag = document.createElement("span");
1772:       pickFlag.className = "pickFlag";
1773:       pickFlag.textContent = pick.flagEmoji || pick.flag || "⚽";
1774:       const pickText = document.createElement("span");
1775:       pickText.className = "pickText";
1776:       const pickName = document.createElement("span");
1777:       pickName.className = "pickName";
1778:       pickName.textContent = r32CardDisplayName(pick);
1779:       pickText.appendChild(pickName);
1780:       card.replaceChildren(pickFlag, pickText);
1781:       card.addEventListener("click", ev => openAdvancementMenu(rule, ev));
1782:       pickLayer.appendChild(card);
1783:       requestAnimationFrame(() => fitPickCardName(card));
1784:     }
1785:     function renderAdvancementPicks() {
1786:       advancementSlotRulesFromManifest().forEach(rule => {
1787:         const pick = advancementPicks[rule.slotId];
1788:         if (!pick) return;
1789:         renderOneAdvancementPick(rule, pick);
1790:       });
1791:     }
1792:     const __wc2026RenderPicksBeforeQfSf = renderPicks;
1793:     renderPicks = function renderPicksWithQfSfWinnerPicks() {
```

## Around `const isCurrentChoice` at line 2659

```js
2647:         wc2026ClearPickForSlot(rule.slotId, round);
2648:         if (typeof renderPicks === "function") renderPicks();
2649:         if (typeof closeMenu === "function") closeMenu();
2650:         const menuEl = document.querySelector(".tapMenu");
2651:         if (menuEl) menuEl.classList.remove("isOpen");
2652:         const backdropEl = document.querySelector(".backdrop");
2653:         if (backdropEl) backdropEl.classList.remove("isOpen");
2654:       });
2655:       groupChips.appendChild(clearButton);
2656:     }
2657: 
2658:     contestants.forEach(team => {
2659:       const isCurrentChoice = false; // WC2026_MENU_NO_PRESELECT_HIGHLIGHT
2660:       const tile = document.createElement("button");
2661:       tile.type = "button";
2662:       tile.className = "teamTile";
2663:       tile.dataset.assignmentTargetSlotId = rule.slotId;
2664:       tile.dataset.assignmentRound = round;
2665:       tile.dataset.currentChoice = "false";
2666:       tile.setAttribute("aria-pressed", "false");
2667:       tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
2668:       tile.addEventListener("click", ev2 => {
2669:         ev2.preventDefault();
2670:         ev2.stopPropagation();
2671:         wc2026StorePickForSlot(rule.slotId, team, rule);
2672:         if (typeof renderPicks === "function") renderPicks();
2673:         if (typeof closeMenu === "function") closeMenu();
2674:       });
2675:       teamGrid.appendChild(tile);
2676:     });
2677:   // WC2026_MENU_SHOWS_CURRENT_PICK_END
2678: 
2679:     backdrop.classList.add("isOpen");
2680:     menu.classList.add("isOpen");
2681:     requestAnimationFrame(() => wc2026PositionMenuBesideRule(rule, ev));
2682:     return true;
2683:   }
2684: 
2685:   // WC2026_SOURCE_GATED_KNOCKOUT_MENU_OPEN
2686:   function wc2026MenuSourcePickExistsForSlot(slotId) {
2687:     const id = String(slotId || "").trim();
2688:     if (!id) return false;
2689: 
2690:     const stores = [];
2691:     try { stores.push(picks); } catch {}
2692:     try { stores.push(r16Picks); } catch {}
2693:     try { stores.push(advancementPicks); } catch {}
```

## Around `patchCardText` at line 3964

```js
3952:   }
3953: 
3954:   function compactPickLabel(pick){
3955:     return threeLetterCode(pick) || (
3956:       pick?.display ||
3957:       pick?.displayName ||
3958:       pick?.displayNameFromImage ||
3959:       pick?.name ||
3960:       "PICK"
3961:     );
3962:   }
3963: 
3964:   function patchCardText(card, pick){
3965:     if (!card || !pick) return;
3966: 
3967:     const code = compactPickLabel(pick);
3968:     const name = (
3969:       pick.display ||
3970:       pick.displayName ||
3971:       pick.displayNameFromImage ||
3972:       pick.name ||
3973:       code
3974:     );
3975: 
3976:     const flagEl = card.querySelector(".pickFlag");
3977:     if (flagEl) flagEl.textContent = pick.flagEmoji || pick.flag || "⚽";
3978: 
3979:     const nameEl = card.querySelector(".pickName");
3980:     if (nameEl) nameEl.textContent = code;
3981: 
3982:     let codeEl = card.querySelector(".pickCode");
3983:     if (!codeEl) {
3984:       const pickText = card.querySelector(".pickText");
3985:       if (pickText) {
3986:         codeEl = document.createElement("span");
3987:         codeEl.className = "pickCode";
3988:         pickText.appendChild(codeEl);
3989:       }
3990:     }
3991: 
3992:     if (codeEl) codeEl.textContent = "";
3993: 
3994:     card.dataset.tooltip = `${name}\n${code}`;
3995:     card.setAttribute("aria-label", `${name} (${code}) selected for ${card.dataset.slotId || "slot"}. Click or tap to change winner.`);
3996:   }
3997: 
3998:   function patchStoredKnockoutCards(){
```

## Around `patchCardText` at line 4013

```js
4001:     let qfSf = {};
4002:     try { bracket = JSON.parse(localStorage.getItem("wc2026.game1.bracketPicks") || "{}"); } catch {}
4003:     try { r16 = JSON.parse(localStorage.getItem("wc2026.game1.r16.winnerPicks") || "{}"); } catch {}
4004:     try { qfSf = JSON.parse(localStorage.getItem("wc2026.game1.qfSf.winnerPicks") || "{}"); } catch {}
4005: 
4006:     document.querySelectorAll(".r16PickCard, .advancePickCard").forEach(card => {
4007:       const slotId = card.dataset.slotId;
4008:       const pick = bracket[slotId] || r16[slotId] || qfSf[slotId] || null;
4009:       if (!pick) return;
4010:       const api = window.WC2026_GAME1_BRACKET_PICK_STORE_API;
4011:       const rule = api && typeof api.slotById === "function" ? api.slotById(slotId) : null;
4012:       if (rule && typeof storedKnockoutPickIsRenderable === "function" && !storedKnockoutPickIsRenderable(rule, pick)) return;
4013:       patchCardText(card, pick);
4014:     });
4015:   }
4016: 
4017:   const previousRenderPicks = typeof renderPicks === "function" ? renderPicks : null;
4018:   if (previousRenderPicks) {
4019:     renderPicks = function renderPicksWithKnockoutThreeLetterCodes(){
4020:       previousRenderPicks();
4021:       patchStoredKnockoutCards();
4022:     };
4023:   }
4024: 
4025:   window.WC2026_PATCH_KNOCKOUT_THREE_LETTER_CODES = patchStoredKnockoutCards;
4026:   setTimeout(patchStoredKnockoutCards, 150);
4027: })();
4028: // WC2026_KNOCKOUT_RENDER_THREE_LETTER_CODE_END
4029: 
4030: 
4031: // WC2026_DOWNSTREAM_CLEAR_INTEGRITY_START
4032: (function installDownstreamClearIntegrity(){
4033:   const BRACKET_KEY = "wc2026.game1.bracketPicks";
4034:   const R32_KEY = "wc2026.game1.r32.picks";
4035:   const R16_KEY = "wc2026.game1.r16.winnerPicks";
4036:   const QFSF_KEY = "wc2026.game1.qfSf.winnerPicks";
4037:   const LOCK_KEY = "wc2026.game1.choiceLockState";
4038: 
4039:   function readJson(key){
4040:     try { return JSON.parse(localStorage.getItem(key) || "{}"); }
4041:     catch { return {}; }
4042:   }
4043: 
4044:   function writeJson(key, value){
4045:     localStorage.setItem(key, JSON.stringify(value || {}));
4046:     return value || {};
4047:   }
```

## Around `WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE_START` at line 3636

```js
3624:     getSourceSlotIds,
3625:     isPickValid,
3626:     isSlotPickable,
3627:     getRenderablePicks,
3628:     inspect,
3629:     storageKey: MODEL_KEY,
3630:     contract: MODEL_CONTRACT
3631:   };
3632: })();
3633: /* WC2026_GAME1_CANONICAL_PICK_STATE_MODEL_END */
3634: </script>
3635: 
3636: // WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE_START
3637: (function installStoredKnockoutPickRenderBridge(){
3638:   function readJson(key){
3639:     try { return JSON.parse(localStorage.getItem(key) || "{}"); }
3640:     catch { return {}; }
3641:   }
3642: 
3643:   function storedPickForSlot(slotId){
3644:     const bracket = readJson("wc2026.game1.bracketPicks");
3645:     const r16 = readJson("wc2026.game1.r16.winnerPicks");
3646:     const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
3647:     return bracket[slotId] || r16[slotId] || qfSf[slotId] || null;
3648:   }
3649: 
3650:   // WC2026_SOURCE_GATE_STORED_KNOCKOUT_RENDER
3651:   function writeJson(key, value){
3652:     try { localStorage.setItem(key, JSON.stringify(value || {})); } catch {}
3653:   }
3654: 
3655:   function r32ManifestToCanonical(slotId){
3656:     const match = String(slotId || "").match(/^R32-([LR])-M(\d+)([AB])$/i);
3657:     if (!match) return slotId;
3658:     const side = match[1].toUpperCase();
3659:     const matchIndex = Number(match[2]);
3660:     const offset = match[3].toUpperCase() === "A" ? 1 : 2;
3661:     return `${side}-R32-${String(((matchIndex - 1) * 2) + offset).padStart(2, "0")}`;
3662:   }
3663: 
3664:   function r32CanonicalToManifest(slotId){
3665:     const match = String(slotId || "").match(/^([LR])-R32-(\d+)$/i);
3666:     if (!match) return slotId;
3667:     const side = match[1].toUpperCase();
3668:     const index = Number(match[2]);
3669:     return `R32-${side}-M${Math.ceil(index / 2)}${index % 2 === 1 ? "A" : "B"}`;
3670:   }
```

## Around `WC2026_GAME1_PICK_STATE` at line 3617

```js
3605:   function inspect(){
3606:     const state = load();
3607:     return {
3608:       contract: MODEL_CONTRACT,
3609:       storageKey: MODEL_KEY,
3610:       pickCount: Object.keys(state.picksBySlotId || {}).length,
3611:       state,
3612:       renderablePicks: getRenderablePicks(),
3613:       mirrorKeys: MIRROR_KEYS.slice()
3614:     };
3615:   }
3616: 
3617:   window.WC2026_GAME1_PICK_STATE = {
3618:     load,
3619:     save,
3620:     clear,
3621:     getPick,
3622:     setPick,
3623:     clearPick,
3624:     getSourceSlotIds,
3625:     isPickValid,
3626:     isSlotPickable,
3627:     getRenderablePicks,
3628:     inspect,
3629:     storageKey: MODEL_KEY,
3630:     contract: MODEL_CONTRACT
3631:   };
3632: })();
3633: /* WC2026_GAME1_CANONICAL_PICK_STATE_MODEL_END */
3634: </script>
3635: 
3636: // WC2026_RENDER_STORED_KNOCKOUT_PICKS_FROM_SITE_STORE_START
3637: (function installStoredKnockoutPickRenderBridge(){
3638:   function readJson(key){
3639:     try { return JSON.parse(localStorage.getItem(key) || "{}"); }
3640:     catch { return {}; }
3641:   }
3642: 
3643:   function storedPickForSlot(slotId){
3644:     const bracket = readJson("wc2026.game1.bracketPicks");
3645:     const r16 = readJson("wc2026.game1.r16.winnerPicks");
3646:     const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
3647:     return bracket[slotId] || r16[slotId] || qfSf[slotId] || null;
3648:   }
3649: 
3650:   // WC2026_SOURCE_GATE_STORED_KNOCKOUT_RENDER
3651:   function writeJson(key, value){
```