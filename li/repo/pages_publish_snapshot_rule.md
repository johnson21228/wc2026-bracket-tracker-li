# Pages Publish Snapshot Rule

`site/ is the source truth` for the deployable WC2026 app surface in this Workbench.

`gh-pages is generated deployment output`. It is a published snapshot in the hosting shape GitHub Pages expects. Do not hand-edit gh-pages.

The publish projection copies the contents of `site/` to the root of the `gh-pages` branch so the public Pages URL can serve:

- `index.html`
- `css/`
- `js/`
- `data/`
- `assets/`
- `.nojekyll`
- `pages-build.txt`

The `main` branch remains the Workbench source and LI branch. The `gh-pages` branch is disposable and reproducible from `site/`.
