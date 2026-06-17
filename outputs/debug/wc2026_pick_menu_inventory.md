# WC2026 Pick/Menu Inventory
Tue Jun 16 23:15:03 EDT 2026

## Git
aed7104 Revert "Prevent duplicate R32 menu assignments"
a3ae51a Prevent duplicate R32 menu assignments
3aa3d05 Anchor choice menu to picked item
804611c Anchor choice menu to board scroll surface
57ce181 Repair long third-place menu scrolling
dc61f8c Hide Pages review script text
2a55d6c Repair Pages review pick acceptance
cec2717 Publish unified bracket site with GitHub Pages

 M site.zip
 M site/index.html
?? apply_wc2026_canonical_assignment_render_repair.py
?? capture_back/CAPTURE_BACK_ANCHORED_KNOCKOUT_CHOICE_MENU_ASSIGNMENT.md
?? capture_back/CAPTURE_BACK_APPLY_SELECTION_TO_PICKED_CELL.md
?? capture_back/CAPTURE_BACK_BRACKET_LIFECYCLE_STATE.md
?? capture_back/CAPTURE_BACK_CANONICAL_KNOCKOUT_ASSIGNMENT_RENDER_REPAIR.md
?? capture_back/CAPTURE_BACK_CANONICAL_KNOCKOUT_ASSIGNMENT_SURFACE.md
?? capture_back/CAPTURE_BACK_GAME1_KNOCKOUT_CHOICE_MENU_RUNTIME_WIRING.md
?? capture_back/CAPTURE_BACK_GAME1_KNOCKOUT_CHOICE_RESOLUTION_TESTS.md
?? capture_back/CAPTURE_BACK_GAME1_NODE_KNOCKOUT_CHOICE_RESOLUTION_TESTS.md
?? capture_back/CAPTURE_BACK_GAME1_NODE_KNOCKOUT_DATA_LOADING_REPAIR.md
?? capture_back/CAPTURE_BACK_GAME1_QF_SF_WINNER_PICKS.md
?? capture_back/CAPTURE_BACK_GAME1_R16_CHOICE_MENU_RULES.md
?? capture_back/CAPTURE_BACK_GAME1_R16_WINNER_PICKS.md
?? capture_back/CAPTURE_BACK_IMPLEMENT_TOOLTIP_SIDE_PLACEMENT_AND_TRACKING.md
?? capture_back/CAPTURE_BACK_MENU_SELECTION_STORAGE_RENDER.md
?? capture_back/CAPTURE_BACK_REPAIR_GAME1_R16_LIVE_CANDIDATE_RESOLUTION.md
?? capture_back/CAPTURE_BACK_SCROLL_CLOSES_ALL_TOOLTIPS.md
?? capture_back/CAPTURE_BACK_SHORT_TERM_R16_HARDCODED_HOLD.md
?? cards/111_add_game1_r16_winner_picks_card.md
?? cards/112_define_game1_r16_choice_menu_rules_card.md
?? cards/113_add_game1_knockout_choice_resolution_tests_card.md
?? cards/113_add_game1_qf_sf_winner_picks_card.md
?? cards/114_add_game1_node_knockout_choice_resolution_tests_card.md
?? cards/115_wire_game1_knockout_choice_menu_runtime_card.md
?? cards/116_add_bracket_lifecycle_state_card.md
?? cards/117_repair_game1_node_knockout_data_loading_card.md
?? cards/119_implement_tooltip_side_placement_and_tracking_card.md
?? cards/120_repair_game1_r16_live_candidate_resolution_card.md
?? cards/122_anchor_knockout_choice_menu_assignment_card.md
?? cards/123_menu_selection_storage_render_card.md
?? cards/124_apply_selection_to_picked_cell_card.md
?? cards/125_scroll_closes_all_tooltips_card.md
?? cards/126_repair_canonical_knockout_assignment_render_card.md
?? cards/127_replace_stacked_knockout_assignment_wrappers_card.md
?? cards/128_short_term_r16_hardcoded_hold_card.md
?? cards/135_define_bracket_pick_finality_validation_card.md
?? cards/145_render_menu_items_as_flag_abbr_only_card.md
?? cards/148_retarget_open_choice_menu_on_pickable_tap_card.md
?? cards/149_replace_unpick_word_with_delete_graphic_card.md
?? docs/features/anchored_knockout_choice_menu_assignment.md
?? docs/features/apply_selection_to_picked_cell.md
?? docs/features/bracket_lifecycle_state.md
?? docs/features/bracket_pick_finality_validation.md
?? docs/features/canonical_knockout_assignment_render_repair.md
?? docs/features/canonical_knockout_assignment_surface.md
?? docs/features/delete_pick_button_graphic.md
?? docs/features/game1_knockout_choice_menu_runtime_wiring.md
?? docs/features/game1_knockout_choice_resolution_tests.md
?? docs/features/game1_node_knockout_choice_resolution_tests.md
?? docs/features/game1_node_knockout_data_loading_repair.md
?? docs/features/game1_qf_sf_winner_picks.md
?? docs/features/game1_r16_choice_menu_rules.md
?? docs/features/game1_r16_live_candidate_resolution_repair.md
?? docs/features/game1_r16_winner_picks.md
?? docs/features/menu_flag_abbr_only.md
?? docs/features/menu_selection_storage_render.md
?? docs/features/retarget_open_choice_menu.md
?? docs/features/scroll_closes_all_tooltips.md
?? docs/features/short_term_r16_hardcoded_hold.md
?? docs/features/tooltip_side_placement_and_tracking_implementation.md
?? li/world_cup/anchored_knockout_choice_menu_assignment_rule.md
?? li/world_cup/apply_selection_to_picked_cell_rule.md
?? li/world_cup/bracket_lifecycle_state_rule.md
?? li/world_cup/bracket_pick_finality_validation_rule.md
?? li/world_cup/canonical_knockout_assignment_render_rule.md
?? li/world_cup/canonical_knockout_assignment_surface_rule.md
?? li/world_cup/delete_pick_button_graphic_rule.md
?? li/world_cup/game1_knockout_choice_menu_runtime_wiring_rule.md
?? li/world_cup/game1_knockout_choice_resolution_tests_rule.md
?? li/world_cup/game1_node_knockout_choice_resolution_tests_rule.md
?? li/world_cup/game1_node_knockout_data_loading_rule.md
?? li/world_cup/game1_qf_sf_winner_pick_rule.md
?? li/world_cup/game1_r16_choice_menu_rule.md
?? li/world_cup/game1_r16_live_candidate_resolution_rule.md
?? li/world_cup/game1_r16_winner_pick_rule.md
?? li/world_cup/menu_flag_abbr_only_rule.md
?? li/world_cup/menu_selection_storage_render_rule.md
?? li/world_cup/retarget_open_choice_menu_rule.md
?? li/world_cup/scroll_closes_all_tooltips_rule.md
?? li/world_cup/short_term_r16_hardcoded_hold_rule.md
?? outputs/debug/
?? prompts/add_bracket_lifecycle_state.md
?? prompts/add_game1_knockout_choice_resolution_tests.md
?? prompts/add_game1_node_knockout_choice_resolution_tests.md
?? prompts/add_game1_qf_sf_winner_picks.md
?? prompts/add_game1_r16_winner_picks.md
?? prompts/define_game1_r16_choice_menu_rules.md
?? prompts/repair_game1_knockout_choice_menu_runtime_wiring.md
?? prompts/repair_game1_node_knockout_data_loading.md
?? prompts/repair_game1_r16_live_candidate_resolution.md
?? prompts/verify_anchored_knockout_choice_menu_assignment.md
?? prompts/verify_apply_selection_to_picked_cell.md
?? prompts/verify_bracket_pick_finality_validation.md
?? prompts/verify_canonical_knockout_assignment_render_repair.md
?? prompts/verify_canonical_knockout_assignment_surface.md
?? prompts/verify_delete_pick_button_graphic.md
?? prompts/verify_menu_flag_abbr_only.md
?? prompts/verify_menu_selection_storage_render.md
?? prompts/verify_retarget_open_choice_menu.md
?? prompts/verify_scroll_closes_all_tooltips.md
?? prompts/verify_short_term_r16_hardcoded_hold.md
?? prompts/verify_tooltip_side_placement_and_tracking.md
?? tools/implement_wc2026_tooltip_side_placement.py
?? tools/run_wc2026_game1_knockout_choice_resolution_tests.js
?? tools/verify_wc2026_anchored_knockout_choice_menu_patch.py
?? tools/verify_wc2026_apply_selection_to_picked_cell_patch.py
?? tools/verify_wc2026_bracket_lifecycle_state_patch.py
?? tools/verify_wc2026_bracket_pick_finality_validation_patch.py
?? tools/verify_wc2026_canonical_assignment_render_repair_patch.py
?? tools/verify_wc2026_canonical_knockout_assignment_surface_patch.py
?? tools/verify_wc2026_delete_pick_button_graphic_patch.py
?? tools/verify_wc2026_game1_knockout_choice_menu_runtime_wiring_patch.py
?? tools/verify_wc2026_game1_knockout_choice_resolution_tests.py
?? tools/verify_wc2026_game1_node_knockout_choice_tests_patch.py
?? tools/verify_wc2026_game1_node_knockout_data_loading_patch.py
?? tools/verify_wc2026_game1_qf_sf_winner_picks_patch.py
?? tools/verify_wc2026_game1_r16_choice_menu_rules_patch.py
?? tools/verify_wc2026_game1_r16_live_candidate_resolution_patch.py
?? tools/verify_wc2026_game1_r16_winner_picks_patch.py
?? tools/verify_wc2026_menu_flag_abbr_only_patch.py
?? tools/verify_wc2026_menu_selection_storage_render_patch.py
?? tools/verify_wc2026_retarget_open_choice_menu_patch.py
?? tools/verify_wc2026_scroll_closes_all_tooltips_patch.py
?? tools/verify_wc2026_short_term_r16_hold_patch.py
?? tools/verify_wc2026_tooltip_side_placement_patch.py
?? wc2026-anchor-menu-to-picked-item-cb-overlay/
?? wc2026-board-attached-choice-menu-cb-overlay/
?? wc2026-delete-pick-button-graphic-cb-overlay/
?? wc2026-hide-pages-review-script-text-cb-overlay/
?? wc2026-menu-flag-abbr-only-cb-overlay/
?? wc2026-opaque-menu-pub-background-cb-overlay/
?? wc2026-pages-review-pick-acceptance-cb-overlay/
?? wc2026-prevent-duplicate-r32-menu-assignments-cb-overlay/
?? wc2026-retarget-open-choice-menu-cb-overlay/
?? wc2026-third-place-menu-scroll-cb-overlay/

## Menu DOM
969:  <aside class="tapMenu" id="tapMenu" aria-label="Team chooser" role="dialog" aria-modal="true">
971:    <div class="groupChips" id="groupChips"></div>
972:    <div class="teamGrid" id="teamGrid"></div>

## Menu open/render paths
1270:        btn.addEventListener("click", ev => openMenuForResolvedGame1R32Rule(rule, ev));
1413:        card.addEventListener("click", ev => openMenuForResolvedGame1R32Rule(rule, ev));
1463:    function openMenuForResolvedGame1R32Rule(rule, ev) {
1484:    function openMenu(rule, ev) {
1600:        btn.addEventListener("click", ev => openR16Menu(rule, ev));
1635:      card.addEventListener("click", ev => openR16Menu(rule, ev));
1652:    function openR16Menu(rule, ev) {
1750:        btn.addEventListener("click", ev => openAdvancementMenu(rule, ev));
1781:      card.addEventListener("click", ev => openAdvancementMenu(rule, ev));
1798:    function openAdvancementMenu(rule, ev) {
1998:    if (typeof openR16Menu === "function") {
1999:      const __wc2026OpenR16MenuBeforeRuntimeWiring = openR16Menu;
2000:      openR16Menu = function wc2026OpenRuntimeR16Menu(rule, ev) { wc2026CloseAllTooltipSurfacesForMenu(); activeSlot = rule; return wc2026OpenResolvedKnockoutMenu(rule, ev) || __wc2026OpenR16MenuBeforeRuntimeWiring(rule, ev); };
2002:    if (typeof openAdvancementMenu === "function") {
2003:      const __wc2026OpenAdvancementMenuBeforeRuntimeWiring = openAdvancementMenu;
2004:      openAdvancementMenu = function wc2026OpenRuntimeAdvancementMenu(rule, ev) { wc2026CloseAllTooltipSurfacesForMenu(); activeSlot = rule; return wc2026OpenResolvedKnockoutMenu(rule, ev) || __wc2026OpenAdvancementMenuBeforeRuntimeWiring(rule, ev); };
2316:  openR16Menu = function openCanonicalR16Menu(rule, ev){ return wc2026CanonicalOpenMenu(rule, ev); };
2317:  if (typeof openAdvancementMenu === "function") {
2318:    openAdvancementMenu = function openCanonicalAdvancementMenu(rule, ev){ return wc2026CanonicalOpenMenu(rule, ev); };
2675:  function wc2026OpenSiteStoreChoiceMenu(rule, ev){
2747:  if (typeof openR16Menu === "function") {
2748:    openR16Menu = function openR16MenuUsingSitePickStore(rule, ev){
2752:  if (typeof openAdvancementMenu === "function") {
2753:    openAdvancementMenu = function openAdvancementMenuUsingSitePickStore(rule, ev){

## R32 hit testing / hotspots
1260:    function createHotspots() {
1270:        btn.addEventListener("click", ev => openMenuForResolvedGame1R32Rule(rule, ev));
1413:        card.addEventListener("click", ev => openMenuForResolvedGame1R32Rule(rule, ev));
1463:    function openMenuForResolvedGame1R32Rule(rule, ev) {
1478:        menu.dataset.activeRuleSource = "pointer-resolved-manifest-slot";
1604:    const __wc2026CreateHotspotsBeforeR16 = createHotspots;
1605:    createHotspots = function createHotspotsWithR16WinnerTargets() {
1650:      createHotspots();
1754:    const __wc2026CreateHotspotsBeforeQfSf = createHotspots;
1755:    createHotspots = function createHotspotsWithQfSfWinnerTargets() {
1796:      createHotspots();
2831:    createHotspots(); renderPicks();

## Pick state stores
1009:    const STORAGE_KEY = "wc2026.game1.r32.picks";
1010:    const BRACKET_LIFECYCLE_STORAGE_KEY = "wc2026.bracket.lifecycle";
1011:    const GAME1_KNOCKOUT_PICKS_STORAGE_KEY = "wc2026.game1.knockoutPicks";
1012:    const GAME2_KNOCKOUT_PICKS_STORAGE_KEY = "wc2026.game2.knockoutPicks";
1041:      try { return normalizeBracketLifecycleState(JSON.parse(localStorage.getItem(BRACKET_LIFECYCLE_STORAGE_KEY) || "null")); }
1046:      localStorage.setItem(BRACKET_LIFECYCLE_STORAGE_KEY, JSON.stringify(bracketLifecycleState));
1073:      storageKey: BRACKET_LIFECYCLE_STORAGE_KEY,
1074:      game1KnockoutPicksStorageKey: GAME1_KNOCKOUT_PICKS_STORAGE_KEY,
1075:      game2KnockoutPicksStorageKey: GAME2_KNOCKOUT_PICKS_STORAGE_KEY,
1223:    function loadPicks() { try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}"); } catch { return {}; } }
1224:    function savePicks(picks) { localStorage.setItem(STORAGE_KEY, JSON.stringify(picks)); }
1225:    let picks = loadPicks();
1505:    function assignTeam(team) { if (!activeSlot) return; picks[activeSlot.slotId] = {...team, assignedSlotId: activeSlot.slotId, slotRule: activeSlot.slotRule, slotRuleLong: activeSlot.slotRuleLong}; savePicks(picks); applyGame1ManifestR32GeometryToSlotRules();
1544:    const R16_STORAGE_KEY = "wc2026.game1.r16.winnerPicks";
1545:    function loadR16Picks() { try { return JSON.parse(localStorage.getItem(R16_STORAGE_KEY) || "{}"); } catch { return {}; } }
1546:    function saveR16Picks(value) { localStorage.setItem(R16_STORAGE_KEY, JSON.stringify(value)); }
1678:      saveR16Picks(r16Picks);
1691:    const ADVANCEMENT_STORAGE_KEY = "wc2026.game1.qfSf.winnerPicks";
1692:    function loadAdvancementPicks() { try { return JSON.parse(localStorage.getItem(ADVANCEMENT_STORAGE_KEY) || "{}"); } catch { return {}; } }
1693:    function saveAdvancementPicks(value) { localStorage.setItem(ADVANCEMENT_STORAGE_KEY, JSON.stringify(value)); }
1824:      saveAdvancementPicks(advancementPicks);
1922:        window.game1KnockoutPicks,
1948:      window.game1KnockoutPicks = Object.assign({}, typeof r16Picks !== "undefined" ? r16Picks : {}, typeof advancementPicks !== "undefined" ? advancementPicks : {}, window.game1KnockoutPicks || {});
2060:    try { if (window.game1KnockoutPicks) stores.push(window.game1KnockoutPicks); } catch {}
2244:      saveR16Picks(r16Picks);
2247:      saveAdvancementPicks(advancementPicks);
2253:    window.game1KnockoutPicks = Object.assign({}, window.game1KnockoutPicks || {}, r16Picks || {}, advancementPicks || {});
2422:    if (typeof saveR16Picks === "function") saveR16Picks(r16Picks);
2430:      if (typeof saveR16Picks === "function") saveR16Picks(r16Picks);
2487:      if (typeof saveR16Picks === "function") saveR16Picks(r16Picks);
2490:      if (typeof saveAdvancementPicks === "function") saveAdvancementPicks(advancementPicks);
2493:      if (typeof savePicks === "function") savePicks(picks);
2646:      const bracket = JSON.parse(localStorage.getItem("wc2026.game1.bracketPicks") || "{}");
2648:      localStorage.setItem("wc2026.game1.bracketPicks", JSON.stringify(bracket));
2653:      if (typeof saveR16Picks === "function") saveR16Picks(r16Picks);
2658:      if (typeof saveAdvancementPicks === "function") saveAdvancementPicks(advancementPicks);
2662:      const qfSf = JSON.parse(localStorage.getItem("wc2026.game1.qfSf.winnerPicks") || "{}");
2664:      localStorage.setItem("wc2026.game1.qfSf.winnerPicks", JSON.stringify(qfSf));
2668:      const r16 = JSON.parse(localStorage.getItem("wc2026.game1.r16.winnerPicks") || "{}");
2670:      localStorage.setItem("wc2026.game1.r16.winnerPicks", JSON.stringify(r16));
2758:  const __wc2026SavePicksBeforeSiteStore = typeof savePicks === "function" ? savePicks : null;
2760:    savePicks = function savePicksAndSiteStore(nextPicks){
2785:      try { window.game1KnockoutPicks = {}; } catch {}
2789:      try { savePicks({}); } catch {}
2790:      try { saveR16Picks({}); } catch {}
2791:      try { saveAdvancementPicks({}); } catch {}
2795:        "wc2026.game1.bracketPicks",
2796:        "wc2026.game1.r16.winnerPicks",
2797:        "wc2026.game1.qfSf.winnerPicks",
2802:        "game1KnockoutPicks"
2879:      window.game1KnockoutPicks,
2927:      game1KnockoutPicks: window.game1KnockoutPicks,
2939:      window.game1KnockoutPicks = previous.game1KnockoutPicks;
3280:    const bracket = readJson("wc2026.game1.bracketPicks");
3281:    const r16 = readJson("wc2026.game1.r16.winnerPicks");
3282:    const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
3352:        storedR16Keys: Object.keys(readJson("wc2026.game1.bracketPicks")).filter(k => String(k).includes("-R16-")),
3353:        storedQfSfKeys: Object.keys(readJson("wc2026.game1.bracketPicks")).filter(k => String(k).includes("-QF-") || String(k).includes("-SF-")),
3530:    try { bracket = JSON.parse(localStorage.getItem("wc2026.game1.bracketPicks") || "{}"); } catch {}
3531:    try { r16 = JSON.parse(localStorage.getItem("wc2026.game1.r16.winnerPicks") || "{}"); } catch {}
3532:    try { qfSf = JSON.parse(localStorage.getItem("wc2026.game1.qfSf.winnerPicks") || "{}"); } catch {}
3558:  const BRACKET_KEY = "wc2026.game1.bracketPicks";
3560:  const R16_KEY = "wc2026.game1.r16.winnerPicks";
3561:  const QFSF_KEY = "wc2026.game1.qfSf.winnerPicks";
3784:  const previousSavePicks = typeof savePicks === "function" ? savePicks : null;
3786:    savePicks = function savePicksWithDownstreamIntegrity(nextPicks){
3859:    const bracket = readJson("wc2026.game1.bracketPicks");
3861:    const r16 = readJson("wc2026.game1.r16.winnerPicks");
3862:    const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
3869:    writeJson("wc2026.game1.bracketPicks", bracket);
3871:    writeJson("wc2026.game1.r16.winnerPicks", r16);
3872:    writeJson("wc2026.game1.qfSf.winnerPicks", qfSf);
3888:      const bracket = readJson("wc2026.game1.bracketPicks");
3889:      const r16 = readJson("wc2026.game1.r16.winnerPicks");
3890:      const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
3917:    if (typeof savePicks === "function" && typeof picks !== "undefined") savePicks(picks);
3918:    if (typeof saveR16Picks === "function" && typeof r16Picks !== "undefined") saveR16Picks(r16Picks);
3919:    if (typeof saveAdvancementPicks === "function" && typeof advancementPicks !== "undefined") saveAdvancementPicks(advancementPicks);
3936:    const bracket = readJson("wc2026.game1.bracketPicks");
4037:    const bracket = readJson("wc2026.game1.bracketPicks");
4039:    const r16 = readJson("wc2026.game1.r16.winnerPicks");
4040:    const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
4064:    const bracket = readJson("wc2026.game1.bracketPicks");
4066:    const r16 = readJson("wc2026.game1.r16.winnerPicks");
4067:    const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
4084:    writeJson("wc2026.game1.bracketPicks", bracket);
4086:    writeJson("wc2026.game1.r16.winnerPicks", r16);
4087:    writeJson("wc2026.game1.qfSf.winnerPicks", qfSf);
4090:    if (typeof savePicks === "function" && typeof picks !== "undefined") savePicks(picks);
4091:    if (typeof saveR16Picks === "function" && typeof r16Picks !== "undefined") saveR16Picks(r16Picks);
4092:    if (typeof saveAdvancementPicks === "function" && typeof advancementPicks !== "undefined") saveAdvancementPicks(advancementPicks);
4104:      const bracket = readJson("wc2026.game1.bracketPicks");
4105:      const r16 = readJson("wc2026.game1.r16.winnerPicks");
4106:      const qfSf = readJson("wc2026.game1.qfSf.winnerPicks");
4260:  const BRACKET_KEY = "wc2026.game1.bracketPicks";
4417:  const BRACKET_KEY = "wc2026.game1.bracketPicks";
4419:  const R16_KEY = "wc2026.game1.r16.winnerPicks";
4420:  const QFSF_KEY = "wc2026.game1.qfSf.winnerPicks";
4863:    bracket: "wc2026.game1.bracketPicks",
4865:    r16: "wc2026.game1.r16.winnerPicks",
4866:    advance: "wc2026.game1.qfSf.winnerPicks"
4950:      if (typeof window.game1KnockoutPicks !== "undefined") {
4951:        window.game1KnockoutPicks = Object.assign({}, window.game1KnockoutPicks || {}, {[slotId]: stored});

## Clear picks
958:    <div class="toolbar" aria-label="Game 1 tools"><button type="button" id="clearPicks">Clear picks</button><button type="button" id="exportPicks">Export picks</button></div>
2405:      if (localStorage.getItem("wc2026.disableShortTermR16Hold") === "1") return false;
2779:    // WC2026_CLEAR_PICKS_CLEARS_ALL_GAME1_STORES
2780:    document.getElementById("clearPicks").addEventListener("click", () => {
2787:      try { localStorage.setItem("wc2026.disableShortTermR16Hold", "1"); } catch {}
2829:    }); // WC2026_CLEAR_PICKS_CLEARS_ALL_STALE_GAME1_STORAGE
5023:    return !!target.closest(".clearPickChip,.remove,[data-clear-r32-slot-id],[data-clear-slot-id],#clearPicks,#clearBtn,.groupChip,[data-group-filter]");

## Short-term R16 hold
2337:// WC2026_SHORT_TERM_R16_HOLD_START
2388:      assignmentContract: "short-term-r16-hardcoded-hold-v001"
2402:  function wc2026ShortTermApplyR16Hold(force = true){
2403:    if (window.WC2026_DISABLE_SHORT_TERM_R16_HOLD === true) return false;
2427:  function wc2026ShortTermClearR16Hold(){
2436:  window.WC2026_SHORT_TERM_R16_HOLD = {
2440:    apply: wc2026ShortTermApplyR16Hold,
2441:    clear: wc2026ShortTermClearR16Hold
2445:  setTimeout(() => wc2026ShortTermApplyR16Hold(false), 0);
2447:// WC2026_SHORT_TERM_R16_HOLD_END
2786:      try { window.WC2026_DISABLE_SHORT_TERM_R16_HOLD = true; } catch {}
2819:        if (window.WC2026_SHORT_TERM_R16_HOLD && typeof window.WC2026_SHORT_TERM_R16_HOLD.clear === "function") {
2820:          window.WC2026_SHORT_TERM_R16_HOLD.clear();

## Render wrappers
1536:    renderPicks = function renderPicksWithR32SlotFit() {
1605:    createHotspots = function createHotspotsWithR16WinnerTargets() {
1647:    renderPicks = function renderPicksWithR16WinnerPicks() {
1755:    createHotspots = function createHotspotsWithQfSfWinnerTargets() {
1793:    renderPicks = function renderPicksWithQfSfWinnerPicks() {
3368:    renderPicks = function renderPicksWithStoredKnockoutPickRenderBridge(){
3455:    renderPicks = function renderPicksWithPickableFeedbackOnly(){
3544:    renderPicks = function renderPicksWithKnockoutThreeLetterCodes(){
4133:    renderPicks = function renderPicksWithRecursiveDownstreamClear(){
4185:    renderPicks = function renderPicksNonDestructiveAfterClear(){
4631:    renderPicks = function renderPicksWithBracketPickFinalityValidation(){
4835:    renderPicks = function renderPicksWithFinalityAdornments(){

## Team menu tile renderers
99:.teamDetail { display: inline-block; margin-left: 14px; font-size: 12px; color: rgba(255,255,255,.72); white-space: nowrap; }
801:.tapMenu .teamTile .teamAbbrOnly {
1495:        tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
1666:        tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
1812:        tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
1967:      tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
2266:    tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
2701:      clearButton.innerHTML = `<span class="teamFlag pickFlag">${currentPick.flagEmoji || currentPick.flag || "⚽"}</span><span class="teamMeta pickText"><span class="teamName pickName">Clear pick</span><span class="teamDetail pickCode">${wc2026MenuTeamLabel(currentPick)}${currentPick.abbr ? ` · ${currentPick.abbr}` : ""}</span></span>`;
2729:      tile.innerHTML = `<span class="teamFlag">${team.flagEmoji || team.flag || "⚽"}</span><span class="teamAbbrOnly">${team.abbr || team.code || team.id || "TBD"}${isCurrentChoice ? " ✓" : ""}</span>`; // WC2026_MENU_FLAG_ABBR_ONLY_NORMALIZED
3963:    clearButton.innerHTML = `<span class="teamFlag pickFlag">${pick.flagEmoji || pick.flag || "⚽"}</span><span class="teamMeta pickText"><span class="teamName pickName">Clear pick</span><span class="teamDetail pickCode">${pickLabel(pick)}${pick.abbr ? ` · ${pick.abbr}` : ""}</span></span>`;
