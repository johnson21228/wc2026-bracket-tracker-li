# Game 1 duplicate JS state fix

Game 1 hit targets are DOM buttons. If they do not appear despite `#hitLayer` existing, check for JavaScript parse errors. Duplicate top-level `const` declarations stop the entire script before hotspot creation.
