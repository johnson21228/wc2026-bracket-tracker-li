# Capture Back: Remote store activation guard without enabling remote mode

Adds a fail-closed remote store activation guard.

Implemented:
- site/js/services/RemoteStoreActivationGuard.js
- DEFAULT_REMOTE_STORE_ACTIVATION.remoteStoreEnabled is false
- createRemoteStoreActivationGuard
- assertRemoteStoreEnabled

Still intentionally not done:
- no remote-mode runtime wiring
- no public runtime import of the guard
- no Supabase store activation
- no Supabase SQL applied
- no Supabase dashboard state changed
- no merge to main

The guard creates a named future switch point without turning it on.
