.PHONY: generate verify build run clean

generate:
	python3 tools/generate_blockout_renderer.py

verify: generate
	python3 tools/verify_blockout_projection_tables.py
	python3 tools/verify_blockout_renderer_asm.py

build: generate
	@echo "Lab 011 seed only: runnable PRG arrives in Milestone 3."

run:
	@echo "Lab 011 seed only: no runnable PRG yet."

clean:
	rm -rf dist/*
	rm -f src/generated_*.s
