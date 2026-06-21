.PHONY: verify pack clean-hygiene open-site publish-pages publish-pages-force check-pages

verify:
	python3 tools/verify_capture_back_governance.py
	python3 tools/verify_wc2026_raw_pick_id_truth_model.py
	python3 tools/verify_wc2026_pick_conflicts_warn_not_block.py
	python3 tools/verify_wc2026_bracket_tracker.py
	python3 tools/verify_wc2026_fifa_r32_bridge.py
	python3 tools/verify_wc2026_r32_pick_menus_from_fifa_bridge.py
	python3 tools/verify_wc2026_track_r32_pick_buttons.py
	python3 tools/verify_wc2026_game1_r32_pick_controller.py
	python3 tools/verify_wc2026_clean_mvc_single_site.py
	python3 tools/verify_wc2026_group_standings_panel_li.py
	python3 tools/verify_wc2026_pick_menu_group_panel_link_li.py
	python3 tools/verify_wc2026_pick_menu_interaction_placement_li.py
	python3 tools/verify_wc2026_pick_menu_runtime_v2.py
	python3 tools/verify_wc2026_player_facing_pick_menu_labels.py
	python3 tools/verify_wc2026_group_standings_model_data.py
	python3 tools/verify_wc2026_make_opensite_target.py
	python3 tools/verify_wc2026_group_panel_runtime_v1.py
	python3 tools/verify_wc2026_group_panel_highlight_link_storage.py
	python3 tools/verify_wc2026_group_panel_highlight_espn_join.py
	python3 tools/verify_wc2026_complete_group_matches_from_poster.py
	python3 tools/verify_wc2026_completed_match_highlight_links.py
	python3 tools/verify_wc2026_group_button_rail.py
	python3 tools/verify_wc2026_group_panel_anchor_to_group_button.py
	python3 tools/verify_wc2026_group_button_rail_subtle_visual_state.py
	python3 tools/verify_wc2026_group_button_flag_hover_opacity.py
	python3 tools/verify_wc2026_group_button_rail_visual_anchor.py

	python3 tools/verify_wc2026_pages_publish_snapshot.py
	python3 tools/verify_wc2026_fail_closed_pages_publish.py
	python3 tools/verify_wc2026_pub_hero_header.py
	python3 tools/verify_wc2026_hero_banner_spelling.py
	python3 tools/verify_wc2026_banner_game_selector_ui.py
	python3 tools/verify_wc2026_banner_rules_panel_ui.py
	python3 tools/verify_wc2026_active_game_pub_background.py
	python3 tools/verify_wc2026_active_game_pick_gating.py
	python3 tools/verify_wc2026_active_game_pick_rules_pipeline.py
	python3 tools/verify_wc2026_game2_fifa_final_r32_source_with_game1_fallback.py
	python3 tools/verify_wc2026_game2_resolved_r32_field.py
	python3 tools/verify_wc2026_picked_bracket_cell_identity_rendering.py
	python3 tools/verify_wc2026_update_results_prompt.py
	python3 tools/verify_wc2026_knockout_schedule_model.py
	python3 tools/verify_wc2026_group_stage_full_match_times.py
	python3 tools/verify_wc2026_safe_group_result_cze_rsa.py
	python3 tools/verify_wc2026_june_20_21_results_and_highlights.py
	python3 tools/verify_wc2026_current_group_order_rendering.py
	python3 tools/verify_wc2026_pick_validity_rendering.py
	python3 tools/verify_wc2026_pick_validity_no_current_rank_block.py
	python3 tools/verify_wc2026_group_stage_background_runtime.py
	python3 tools/verify_wc2026_interaction_overlay_stack.py
	python3 tools/verify_wc2026_zoom50_floating_surface_placement.py
	python3 tools/verify_wc2026_remove_player_storage_ui.py
	python3 tools/verify_wc2026_pages_owned_board_zoom_out_scale.py
	python3 tools/verify_wc2026_pages_owned_board_zoom_out_runtime.py
	python3 tools/verify_wc2026_pages_owned_board_wheel_pinch_zoom.py
	python3 tools/verify_wc2026_public_multi_user_play_li.py
	python3 tools/verify_wc2026_empty_pick_state_storage_li.py
	python3 tools/verify_wc2026_supabase_shared_pick_sql_target.py
	python3 tools/verify_wc2026_supabase_sql_rls_finalization.py
	python3 tools/verify_wc2026_supabase_identity_ui_surface.py
	python3 tools/verify_wc2026_supabase_auth_identity_surface_before_postgres.py
	python3 tools/verify_wc2026_full_canonical_bracket_document_runtime.py
	python3 tools/verify_wc2026_bracketdocument_save_seam_before_supabase.py
clean-hygiene:
	python3 tools/clean_repo_hygiene.py

open-site:
	open site/index.html

pack: clean-hygiene verify
	mkdir -p dist
	rm -f dist/wc2026-bracket-tracker-li.pack.zip
	zip -r dist/wc2026-bracket-tracker-li.pack.zip . 		-x 'dist/*' 		-x '.git/*' 		-x '__MACOSX/*' 		-x '.DS_Store' 		-x '*/.DS_Store' 		-x '*/__pycache__/*' 		-x '*.pyc' 		-x 'wc2026_*_overlay/*' 		-x 'wc2026-*-cb-overlay/*' 		-x 'wb_*_overlay/*' 		-x 'wc2026_bracket_tracker_cb_001/*' 		-x 'wc2026_schedule_poster_input_artifact/*'

.PHONY: opensite stopsite

opensite:
	@PID="$$(lsof -ti tcp:8000 || true)"; \
	if [ -n "$$PID" ]; then \
		echo "Stopping existing server on port 8000: $$PID"; \
		kill $$PID || true; \
	fi; \
	echo "Starting WC2026 site at http://localhost:8000"; \
	python3 -m http.server 8000 -d site >/tmp/wc2026-bracket-tracker-site.log 2>&1 & \
	echo $$! > /tmp/wc2026-bracket-tracker-site.pid; \
	open http://localhost:8000; \
	echo "Server PID: $$(cat /tmp/wc2026-bracket-tracker-site.pid)"; \
	echo "Log: /tmp/wc2026-bracket-tracker-site.log"

stopsite:
	@PID="$$(cat /tmp/wc2026-bracket-tracker-site.pid 2>/dev/null || true)"; \
	if [ -n "$$PID" ]; then \
		echo "Stopping WC2026 site server: $$PID"; \
		kill $$PID || true; \
		rm -f /tmp/wc2026-bracket-tracker-site.pid; \
	else \
		PID="$$(lsof -ti tcp:8000 || true)"; \
		if [ -n "$$PID" ]; then \
			echo "Stopping server on port 8000: $$PID"; \
			kill $$PID || true; \
		else \
			echo "No WC2026 site server found."; \
		fi; \
	fi

.PHONY: publish-pages publish-pages-force check-pages

publish-pages:
	python3 tools/publish_pages_snapshot.py --strict --verify-live

publish-pages-force:
	python3 tools/publish_pages_snapshot.py --strict --verify-live --force-redeploy

check-pages:
	python3 tools/check_pages_publish_freshness.py
