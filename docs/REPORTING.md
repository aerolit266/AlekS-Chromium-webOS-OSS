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

## Privacy regression coverage

The test suite includes 11 cases covering missing fields, invalid verification states, nested token-like field names, MAC-style identifiers, private IPv4, non-public IPv6, and a public IPv6 control. Latest independent fresh-clone run: **11/11 PASS** on a VPS on 2026-10-10. These checks are heuristic and do not provide comprehensive secret detection or a legal clearance for redistribution.

The same test-report schema may later be reused in AlekS Kino research, but this repository does not include or open-source its production media engine.
