# AlekS Chromium webOS — Open Research

[Русский](README.ru.md)

Independent compatibility research exploring modern Chromium on legacy LG webOS / ARMv7 devices.

## Scope

- Document browser lifecycle and remote-control behavior on resource-constrained TV hardware.
- Develop independently owned, reproducible and non-invasive test utilities.
- Research Chromium media routing, Mojo IPC, platform services and GPU acceleration.
- Track verified measurements separately from experimental or proposed work.

**Current status:** research and documentation. Private experimental Chromium 120 builds have passed bounded on-device GPU, 4K hardware-video and HDR10 output-signal tests, but no production-ready browser or universal 4K/HDR reliability is claimed here. See the [public non-code progress summary](docs/CHROMIUM120_PUBLIC_STATUS.ru.md). This public repository does **not** contain a working Chromium binary, LG firmware, proprietary platform libraries, private patches or credentials.

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

## Verification checkpoint (2026-10-10)

The public repository was freshly cloned into a disposable directory on a separate VPS host. All **7 Python unit tests passed** and `examples/host-playback.json` passed schema validation. This is a **host-side verification only**; a successful GitHub Actions run and TV playback remain unverified. This report validator cannot guarantee that all secrets were removed.

## Playback metrics utility

An original [playback measurements analyzer](tools/analyze_playback.py) calculates medians and maxima for startup latency, dropped frames, seek delay and audio/video drift. See [measurement protocol](docs/PLAYBACK_METRICS.md). All bundled measurements are synthetic. The latest fresh-clone VPS check passed **16/16 Python tests** and both example CLI tools (2026-10-10). GitHub Actions results for this commit require separate confirmation.

## Browser lifecycle validation

The original [lifecycle state-machine validator](tools/browser_lifecycle.py) tests anonymized event traces for launch, fullscreen, Back and Exit behavior. See [lifecycle protocol](docs/BROWSER_LIFECYCLE.md). The latest independent clean-clone VPS run passed **24/24 unit tests** and all three example tools (2026-10-10). These synthetic checks do not validate a physical LG TV. GitHub Actions status for the newest commits requires separate confirmation.

## Real LG test observations and progress

The [historical anonymized observation summary](docs/REAL_DEVICE_OBSERVATIONS.md) covers early 9–10 October 2026 tests, including 720p and GPU diagnostics. Later private on-device engineering tests of Chromium 120 passed bounded VP9 4K60 SDR, HEVC hardware playback, and HDR10 video-output signaling, with explicit limitations.

The new [sanitized public project update (Russian, 20 October 2026)](docs/CHROMIUM120_PUBLIC_STATUS.ru.md) summarizes these later findings and outlines the proposed webOS 4/5 adapter strategy without releasing proprietary implementation details, binary builds, or internal configurations. These tests do **not** establish a production-ready or universally compatible browser.

## Reproducible device research

- [Step-by-step on-device verification protocol](docs/REPRODUCE_ON_DEVICE.md)
- [Evidence-based engineering history and open problems](docs/PROJECT_HISTORY.md)

These materials clearly distinguish actual TV observations from host-side and synthetic checks.

## Maintainer and Open Source Program

See the [evidence-grounded maintainer brief](docs/MAINTAINER_BRIEF.md) for project scope, reproducibility, honest limitations and prepared application wording. The application is **not submitted**, and acceptance is not guaranteed.
