# Browser lifecycle event validation

This original, standard-library Python utility checks *synthetic or anonymized* event traces against a simple expected state machine. It does not run Chromium, inspect webOS, prove exit works on a remote control, or change device configuration.

Usage:

```bash
python tools/browser_lifecycle.py examples/browser-lifecycle.json
python -m unittest discover -s tests -v
```

Accepted events: `LAUNCH`, `READY`, `ENTER_FULLSCREEN`, `EXIT_FULLSCREEN`, `BACK`, `EXIT_REQUEST`, `CLOSED`.

Expected behavior in this **simplified reference model**: a Back press while fullscreen leaves fullscreen; a later Back triggers exit; a `CLOSED` event requires an exit request. Actual UX and webOS lifecycle behavior vary by application.

Only events are accepted; never add private URLs, SSH details, device identifiers or credentials to public traces. Run on independently collected, reviewed event data. Passing the reference model does **not** establish that the deployed browser has correct Back/Exit behavior.
