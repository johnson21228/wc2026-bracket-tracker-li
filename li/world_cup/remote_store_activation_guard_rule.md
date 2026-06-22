# Remote store activation guard rule

Remote bracket persistence must be fail-closed until explicitly enabled.

Default:
remoteStoreEnabled: false

The guard provides a named future switch point.

Its existence does not activate remote persistence.

Until a later CB explicitly wires remote mode:
- public runtime remains local/browser-store active
- BracketRepository defaults to LocalStorageBracketStore
- View and Controller do not call Supabase
- SupabaseBracketStore is not instantiated by runtime
- no SQL is applied by this guard
- no dashboard state is changed by this guard
- no merge to main is implied

Code that tries to require remote mode before activation must receive a clear error.
