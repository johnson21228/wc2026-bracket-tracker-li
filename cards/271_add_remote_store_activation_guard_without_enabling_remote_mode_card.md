# Card 271 — Add remote store activation guard without enabling remote mode

Add a fail-closed activation guard for future signed-in remote bracket persistence.

Acceptance:
- RemoteStoreActivationGuard.js exists.
- Default activation is remoteStoreEnabled: false.
- The guard exports createRemoteStoreActivationGuard.
- The guard exports DEFAULT_REMOTE_STORE_ACTIVATION_GUARD.
- The guard has assertRemoteStoreEnabled.
- The guard throws if remote mode is not enabled.
- The guard does not import or instantiate SupabaseBracketStore.
- Public runtime does not import the guard yet.
- BracketRepository still defaults to LocalStorageBracketStore.
- Supabase SQL is not applied.
- Public Pages main remains untouched.
