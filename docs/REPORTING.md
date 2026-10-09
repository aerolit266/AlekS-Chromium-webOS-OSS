# Reproducible test report format

This public utility validates anonymized JSON reports before they are shared. It is original Python code using only the standard library. It **does not** interact with LG firmware, run a web browser, prove TV functionality or guarantee that all secrets are removed.

## Quickstart

```bash
python -m unittest discover -s tests -v
python tools/validate_report.py examples/host-playback.json
```

Required string fields: `device_family`, `webos_version`, `build_id`, `test_type`, `environment`, `result`, `evidence`.

States: `PLANNED`, `BUILT`, `TESTED_ON_HOST`, `VERIFIED_ON_TV`. The last state requires environment `TV`. The tool checks format and basic privacy red flags; it **cannot authenticate** submitted evidence.

Supported test types: launch, back_exit, fullscreen, playback, seek, hardware_decode, performance.

Never submit logs, keys, identifiers or diagnostics until a human has reviewed them. A PASS from this script is not a comprehensive secret scan.
