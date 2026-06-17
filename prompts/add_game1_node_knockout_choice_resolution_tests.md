# Prompt — Add Game 1 Node knockout choice resolution tests

Add a browser-free command-line test for Game 1 knockout choice resolution.

The test should run from repo root with Node, extract the existing browser-exposed knockout choice resolution harness from `site/game1/index.html`, seed deterministic R32/R16/QF picks, and verify that R16/QF/SF slots each resolve exactly two contestants from their feeding match path.

Do not change visible Game 1 behavior in this patch.
