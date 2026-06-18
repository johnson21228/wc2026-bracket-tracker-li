.PHONY: verify pack clean-hygiene open-site

verify:
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
	python3 tools/verify_wc2026_group_standings_model_data.py
	python3 tools/verify_wc2026_make_opensite_target.py
	python3 tools/verify_wc2026_group_panel_runtime_v1.py
	python3 tools/verify_wc2026_group_panel_highlight_link_storage.py
	python3 tools/verify_wc2026_complete_group_matches_from_poster.py
	python3 tools/verify_wc2026_completed_match_highlight_links.py
	python3 tools/verify_wc2026_group_button_rail.py

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

