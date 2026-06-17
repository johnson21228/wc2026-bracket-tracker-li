# Remove Static Single-File Architecture Goal

Update the WC2026 Bracket Tracker Workbench so the current architectural direction is modular MVC/TDD source.

Do not preserve the old portability property.

Keep static hosting or GitHub Pages compatibility only as a deployment property. The desired source design should be modular, testable, and separated into model, view, controller, data, and test surfaces.

Required outcomes:

- remove or rewrite LI that says the app should remain a page-concentrated implementation
- add a modular MVC/TDD source rule
- update README/MAP language away from static-first architecture
- add a verifier that prevents future LI from reintroducing the monolithic-page goal
- preserve old Capture Back records as history, not current direction
