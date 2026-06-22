# Remote store activation guard

The remote store activation guard is a named switch point for future signed-in Supabase persistence.

It does not enable remote mode.

File:
site/js/services/RemoteStoreActivationGuard.js

Default posture:
remoteStoreEnabled: false

Why this exists:
The project now has an inactive remote store implementation. The next safety boundary is to make activation explicit.

Current boundary:
- guard is not imported by public runtime yet
- guard does not instantiate the Supabase store
- guard does not apply SQL
- guard does not change dashboard state
- guard does not merge to main
- local browser storage remains the active public path
