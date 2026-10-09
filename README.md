# AlekS Chromium webOS — Open Research

[Русский](README.ru.md)

Independent compatibility research exploring modern Chromium on legacy LG webOS / ARMv7 devices.

## Scope

- Document browser lifecycle and remote-control behavior on resource-constrained TV hardware.
- Develop independently owned, reproducible and non-invasive test utilities.
- Research Chromium media routing, Mojo IPC, platform services and GPU acceleration.
- Track verified measurements separately from experimental or proposed work.

**Current status:** research and documentation; no production-ready browser, HDR or 4K hardware-decoding support is claimed here. This public repository does **not** contain a working Chromium binary, LG firmware, proprietary platform libraries, private patches or credentials.

## Project boundaries

The operational AlekS Chromium development environment is maintained privately. Public contributions here must consist only of original or lawfully redistributable material. Stock TV firmware and privileged services are out of scope for public reproduction.

## Documentation

- [Research and validation approach](docs/VALIDATION.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Notices](NOTICE.md)

Maintained by the AlekS / GameFree24 project. This repository is not affiliated with LG or Google.

## Open-source test utility

A small Python standard-library [report validator](tools/validate_report.py) and [seven unit tests](tests/test_validate_report.py) are available. See [reporting guidelines](docs/REPORTING.md). A format-validation PASS is **not** evidence of playback on an actual LG TV and not a comprehensive security audit.

```bash
python -m unittest discover -s tests -v
python tools/validate_report.py examples/host-playback.json
```
