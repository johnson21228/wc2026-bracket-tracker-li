.PHONY: generate render polygon-proof spans verify build run clean

generate:
	python3 tools/generate_blockout_renderer.py

render: generate
	python3 tools/render_blockout_gameboard_projection_svg.py

polygon-proof: generate
	python3 tools/render_single_cube_polygon_svg.py

spans: polygon-proof
	python3 tools/generate_single_cube_polygon_spans.py

build: generate
	python3 tools/build_blockout_renderer_prg.py

verify: build render polygon-proof spans
	python3 tools/verify_blockout_projection_tables.py
	python3 tools/verify_blockout_perspective_projection.py
	python3 tools/verify_blockout_renderer_asm.py
	python3 tools/verify_blockout_gameboard_projection_svg.py
	python3 tools/verify_blockout_prg_build.py
	python3 tools/verify_blockout_single_cube_polygon.py
	python3 tools/verify_blockout_single_cube_spans.py

run: build
	@if command -v x64sc >/dev/null 2>&1; then \
		x64sc dist/blockout_renderer.prg; \
	elif command -v x64 >/dev/null 2>&1; then \
		x64 dist/blockout_renderer.prg; \
	else \
		echo "VICE not found. Open dist/blockout_renderer.prg with your C64 emulator."; \
	fi

clean:
	rm -rf dist/*
	rm -f src/generated_*.s
