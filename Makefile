.PHONY: verify pack clean-hygiene open-site publish-pages publish-pages-force check-pages

verify:
	python3 tools/verify_wc2026_workbench_easter_egg_button_visible.py
	python3 tools/verify_wc2026_c64_workbench_loop_easter_egg_tab.py
	python3 tools/verify_wc2026_official_truth_bracket_hidden_player.py
	python3 tools/verify_wc2026_joined_game1_brackets_public_visibility.py
	python3 tools/verify_wc2026_paste_back_terminal_output_contract.py
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
	python3 tools/verify_wc2026_knockout_pick_menu_no_feeder_language.py
	python3 tools/verify_wc2026_group_standings_model_data.py
	python3 tools/verify_wc2026_make_opensite_target.py
	python3 tools/verify_wc2026_group_panel_runtime_v1.py
	python3 tools/verify_wc2026_group_panel_no_context_column.py
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
	python3 tools/verify_wc2026_bracketeering_pub_hub_title.py
	python3 tools/verify_wc2026_banner_game_selector_ui.py
	python3 tools/verify_wc2026_lifecycle_stage_nomenclature.py
	python3 tools/verify_wc2026_lifecycle_stage_presentation_only_picks.py
	python3 tools/verify_wc2026_dev_game_selector_next_to_zoom.py
	python3 tools/verify_wc2026_banner_rules_panel_ui.py
	python3 tools/verify_wc2026_rules_panel_no_developer_note.py
	python3 tools/verify_wc2026_info_panel_copy_polish.py
	python3 tools/verify_wc2026_active_game_pub_background.py
	python3 tools/verify_wc2026_knockout_runtime_default_background.py
	python3 tools/verify_wc2026_knockout_background_deemphasis.py
	python3 tools/verify_wc2026_knockout_pub_background_image_prompt.py
	python3 tools/verify_wc2026_knockout_pub_background_runtime_asset.py
	python3 tools/verify_wc2026_lifecycle_background_softening.py
	python3 tools/verify_wc2026_active_game_pick_gating.py
	python3 tools/verify_wc2026_active_game_pick_rules_pipeline.py
	python3 tools/verify_wc2026_group_stage_hides_later_round_pick_fills.py
	python3 tools/verify_wc2026_group_stage_r16_interaction_gate.py
	python3 tools/verify_wc2026_game1_game2_state_separation_no_r16_preselect_highlight.py
	python3 tools/verify_wc2026_pick_slot_button_label_centering.py
	python3 tools/verify_wc2026_game2_fifa_final_r32_source_with_game1_fallback.py
	python3 tools/verify_wc2026_game2_resolved_r32_field.py
	python3 tools/verify_wc2026_game2_r32_readonly_rendering.py
	python3 tools/verify_wc2026_picked_bracket_cell_identity_rendering.py
	python3 tools/verify_wc2026_single_geometry_truth_li.py
	python3 tools/verify_wc2026_runtime_uses_single_geometry_svg_truth.py
	python3 tools/verify_wc2026_final_four_center_stack_geometry.py
	python3 tools/verify_wc2026_final_four_center_stack_pick_menu.py
	python3 tools/verify_wc2026_unpicked_bracket_cells_choose_team.py
	python3 tools/verify_wc2026_r32_group_panel_shortcut.py
	python3 tools/verify_wc2026_r32_slot_full_team_tooltip.py
	python3 tools/verify_wc2026_update_results_prompt.py
	python3 tools/verify_wc2026_knockout_schedule_model.py
	python3 tools/verify_wc2026_group_stage_full_match_times.py
	python3 tools/verify_wc2026_safe_group_result_cze_rsa.py
	python3 tools/verify_wc2026_june_20_21_results_and_highlights.py
	python3 tools/verify_wc2026_spain_saudi_result_and_highlight.py
	python3 tools/verify_wc2026_belgium_iran_result_and_highlight.py
	python3 tools/verify_wc2026_june_22_group_i_j_results_and_highlights.py
	python3 tools/verify_wc2026_june_23_group_k_l_results.py
	python3 tools/verify_wc2026_group_b_complete_results.py
	python3 tools/verify_wc2026_current_group_order_rendering.py
	python3 tools/verify_wc2026_pick_validity_rendering.py
	python3 tools/verify_wc2026_pick_validity_no_current_rank_block.py
	python3 tools/verify_wc2026_group_stage_background_runtime.py
	python3 tools/verify_wc2026_interaction_overlay_stack.py
	python3 tools/verify_wc2026_zoom50_floating_surface_placement.py
	python3 tools/verify_wc2026_floating_surface_dismissal_view_owned.py
	python3 tools/verify_wc2026_floating_board_surfaces_above_overlay_controls.py
	python3 tools/verify_wc2026_floating_controls_fixed_size_during_zoom.py
	python3 tools/verify_wc2026_iphone_touch_map_mode.py
	python3 tools/verify_wc2026_sign_in_panel_over_game_board.py
	python3 tools/verify_wc2026_identity_round_icon_buttons.py
	python3 tools/verify_wc2026_css_owned_top_right_player_controls.py
	python3 tools/verify_wc2026_center_final_four_visual_only.py
	python3 tools/verify_wc2026_final_stack_svg_manifest_alignment.py
	python3 tools/verify_wc2026_final_four_pick_display.py
	python3 tools/verify_wc2026_champion_pixel_aura.py
	python3 tools/verify_wc2026_remove_player_storage_ui.py
	python3 tools/verify_wc2026_map_style_full_window_board_shell.py
	python3 tools/verify_wc2026_map_icon_controls.py
	python3 tools/verify_wc2026_map_control_icon_centering.py
	python3 tools/verify_wc2026_later_round_choose_winner_labels.py
	python3 tools/verify_wc2026_scotland_flag_emoji_data.py
	python3 tools/verify_wc2026_england_flag_emoji_data.py
	python3 tools/verify_wc2026_pages_owned_board_zoom_out_scale.py
	python3 tools/verify_wc2026_pages_owned_board_zoom_out_runtime.py
	python3 tools/verify_wc2026_pages_owned_board_wheel_pinch_zoom.py
	python3 tools/verify_wc2026_mouse_drag_board_pan.py
	python3 tools/verify_wc2026_mouse_double_click_zoom.py
	python3 tools/verify_wc2026_public_multi_user_play_li.py
	python3 tools/verify_wc2026_empty_pick_state_storage_li.py
	python3 tools/verify_wc2026_official_r32_hydration_li.py
	python3 tools/verify_wc2026_official_r32_hydration_runtime.py
	python3 tools/verify_wc2026_official_r32_as_player_feeder_teams.py
	python3 tools/verify_wc2026_supabase_admin_official_r32_source.py
	python3 tools/verify_wc2026_single_game_admin_official_runtime.py
	python3 tools/verify_wc2026_force_player_r32_matches_admin_official.py
	python3 tools/verify_wc2026_admin_official_r32_editor_mode.py
	python3 tools/verify_wc2026_admin_official_full_bracket_editor_mode.py
	python3 tools/verify_wc2026_hydrate_only_supabase_admin_r32_into_player_picks.py
	python3 tools/verify_wc2026_admin_r32_hydration_compatibility_model_li.py
	python3 tools/verify_wc2026_site_owned_official_truth_li.py
	python3 tools/verify_wc2026_editable_site_official_truth_json.py
	python3 tools/verify_wc2026_site_official_truth_runtime_source.py
	python3 tools/verify_wc2026_official_truth_r32_only_seed.py
	python3 tools/verify_wc2026_superseded_admin_official_truth_li.py
	python3 tools/verify_wc2026_admin_official_results_truth.py
	python3 tools/verify_wc2026_official_knockout_results_append_only.py
	python3 tools/verify_wc2026_brazil_japan_knockout_result.py
	python3 tools/verify_wc2026_germany_paraguay_knockout_result.py
	python3 tools/verify_wc2026_knockout_result_dom_classification.py
	python3 tools/verify_wc2026_july_04_r16_extended_highlights.py
	python3 tools/verify_wc2026_supabase_shared_pick_sql_target.py
	python3 tools/verify_wc2026_supabase_sql_rls_finalization.py
	python3 tools/verify_wc2026_supabase_profiles_and_bracket_saving_target.py
	python3 tools/verify_wc2026_supabase_identity_ui_surface.py
	python3 tools/verify_wc2026_supabase_auth_identity_surface_before_postgres.py
	python3 tools/verify_wc2026_not_joined_startup_guidance.py
	python3 tools/verify_wc2026_not_joined_notice_auth_settled.py
	python3 tools/verify_wc2026_join_required_dialog_copy.py
	python3 tools/verify_wc2026_live_player_name_edit.py
	python3 tools/verify_wc2026_signed_in_identity_ui_polish.py
	python3 tools/verify_wc2026_supabase_profile_store_public_player_name.py
	python3 tools/verify_wc2026_supabase_bracket_store_seam.py
	python3 tools/verify_wc2026_supabase_bracket_store_smoke_test.py
	python3 tools/verify_wc2026_shared_supabase_browser_client.py
	python3 tools/verify_wc2026_dev_active_supabase_bracket_store.py
	python3 tools/verify_wc2026_account_save_action_target.py
	python3 tools/verify_wc2026_join_first_live_picks_player_ui.py
	python3 tools/verify_wc2026_player_standings_panel.py
	python3 tools/verify_wc2026_player_supplied_links_panel.py
	python3 tools/verify_wc2026_player_standings_no_pick_links.py
	python3 tools/verify_wc2026_player_standings_scoring_rule.py
	python3 tools/verify_wc2026_player_standings_max_possible_reachability_rule.py
	python3 tools/verify_wc2026_player_standings_weighted_reachability_runtime.py
	python3 tools/verify_wc2026_player_standings_score_headers.py
	python3 tools/verify_wc2026_player_standings_scoring_vocabulary.py
	python3 tools/verify_wc2026_storage_backed_player_standings.py
	python3 tools/verify_wc2026_player_standings_board_viewer.py
	python3 tools/verify_wc2026_player_board_viewer_trickle_on_miss.py
	python3 tools/verify_wc2026_group_stage_pick_lock_gate.py
	python3 tools/verify_wc2026_bracketeering_workflow_easter_egg_panel.py
	python3 tools/verify_wc2026_full_canonical_bracket_document_runtime.py
	python3 tools/verify_wc2026_bracketdocument_save_seam_before_supabase.py
	python3 tools/verify_wc2026_update_all_missing_completed_group_results.py
	python3 tools/verify_wc2026_player_pick_lockdown_times.py
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
force-pages-publish:
	python3 tools/force_pages_publish.py

