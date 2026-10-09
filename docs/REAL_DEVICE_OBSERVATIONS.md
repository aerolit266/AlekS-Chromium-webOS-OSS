# Anonymized LG webOS / Chromium 120 observations

**Evidence class:** historical device-side observations, summarized from a private technical checkpoint (2026-10-09 to 2026-10-10). These are actual device experiments, **not** measurements produced by the public test utilities. Sensitive paths, connection details and personal identifiers have been omitted.

## Observations verified in device-side diagnostic notes

| Test | Result | Limit |
| --- | --- | --- |
| Browser/version | Chromium 120.0.6099.269 used in an isolated application | Not a stock-browser replacement |
| GPU context | Mali-G52, OpenGL ES 3.2; a WebGL readback returned the expected bytes | Does not establish video hardware decoding |
| Chromium GPU feature report | GPU compositing, rasterization, OpenGL and video_decode reported enabled | Feature report is not decoder-backend attribution |
| YouTube 720p short playback | 1280×720, readyState=4, currentTime advanced, 206 frames total, 4 dropped, 0 corrupted | Short session only; frame interval and decoder unknown |
| Fullscreen/Back | Scripted CDP input and Fullscreen API transitions were exercised | Physical remote and YouTube video button not fully verified |
| App close | System application manager close returned to Home and terminated app shell | Physical remote Exit still unverified |
| Performance observation | Renderer RSS ≈166 MiB and cumulative CPU ≈84% in an observed YouTube session | Snapshot, not a repeatable controlled benchmark |

### Interpretation

The short playback observation gives 4 dropped frames out of 206 total (about 1.94%). It must **not** be read as a sustained dropout rate or evidence for 4K/HDR support. CPU measurements do not identify the active decoder. A scripted Back/fullscreen test does not prove that every physical remote interaction works.

### Not yet established

- Reliable physical Magic Remote Back/Exit and YouTube fullscreen behavior
- Sustained playback or seek performance over long intervals
- Actual hardware decoder backend for streamed video
- 4K/HDR playback support
- Reproducible A/V drift measurements

### Provenance and confidentiality

The original detailed diagnostic checkpoint is stored privately and intentionally not mirrored here. The summary includes no user-specific network addresses, access credentials, firmware images or proprietary libraries.

**Use case:** public documentation of bounded experimental results that can guide community reproducibility and future independently measured tests.
