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
	python3 tools/verify_wc2026_group_standings_model_data.py

clean-hygiene:
	python3 tools/clean_repo_hygiene.py

open-site:
	open site/index.html

pack: clean-hygiene verify
	mkdir -p dist
	rm -f dist/wc2026-bracket-tracker-li.pack.zip
	zip -r dist/wc2026-bracket-tracker-li.pack.zip . 		-x 'dist/*' 		-x '.git/*' 		-x '__MACOSX/*' 		-x '.DS_Store' 		-x '*/.DS_Store' 		-x '*/__pycache__/*' 		-x '*.pyc' 		-x 'wc2026_*_overlay/*' 		-x 'wc2026-*-cb-overlay/*' 		-x 'wb_*_overlay/*' 		-x 'wc2026_bracket_tracker_cb_001/*' 		-x 'wc2026_schedule_poster_input_artifact/*'
