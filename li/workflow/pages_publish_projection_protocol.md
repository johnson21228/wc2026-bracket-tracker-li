# Pages Publish Projection Protocol

A Workbench may keep its real app surface in a source-owned folder such as `site/` while publishing a snapshot to a hosting-specific shape.

For this WB, `site/ is the source truth` and `gh-pages is generated deployment output`.

The projection protocol is:

1. Verify the Workbench source state.
2. Treat `site/` as the current app truth.
3. Create or update a temporary `gh-pages` worktree.
4. Clear prior generated snapshot files while preserving Git metadata.
5. Copy the contents of `site/` to `gh-pages` root.
6. Add `.nojekyll` and `pages-build.txt`.
7. Commit and push the published snapshot.
8. Confirm GitHub Pages is configured to serve `gh-pages`.

Do not hand-edit gh-pages. Re-publish from `site/` instead.
