# AlekS Chromium / webOS — evidence-based project history

This document tracks technical milestones without claiming that the public repository contains the private production browser implementation.

| Period | Engineering milestone | Evidence scope |
| --- | --- | --- |
| October 2026 | Chromium 120.0.6099.269 executed as an isolated LG webOS browser test application | Historical device-side diagnostic checkpoint; not a redistributable binary |
| 9 October 2026 | Chromium GPU/WebGL diagnostics and short YouTube 720p session | GPU context observed; 206 total frames, 4 dropped; no proof of hardware decoding |
| 9–10 October 2026 | System application manager closing route and window-identity investigation | Programmatic close returned Home; physical remote Exit remains unverified |
| October 2026 | Public research repository separated from private code | Public documentation, independent original utilities and automated checks |
| October 2026 | Report validation, playback statistics and lifecycle event validation | 24 host-side Python tests passed after fresh public clone; not a TV integration suite |

## Known unsolved engineering problems

- Real YouTube fullscreen and physical Back/Exit behavior across device types.
- Actual media decoder attribution and sustained playback performance.
- 4K/HDR compatibility on resource-limited legacy devices.
- Reproducible on-device metrics from safely shareable traces.

## Public benefit and boundaries

Independent developers may reuse the original report-validator, measurement summarizer, and lifecycle-reference tools under their published software license. The published findings aim to reduce ambiguity between a feature flag, a synthetic test, and a tested on-device capability.

No popularity, external adoption, first-in-world status or general device compatibility is asserted. A real on-device test procedure is documented in [REPRODUCE_ON_DEVICE.md](REPRODUCE_ON_DEVICE.md).
