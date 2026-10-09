# Reproducing Chromium browser tests on legacy webOS

This checklist is intended for a **device owner operating an independently installed test application**. It does not require replacing firmware, rooting a TV, exposing diagnostic services, or publishing device-specific credentials. Exact controls vary by device and installation.

## Preparation

1. Record model **family** and major webOS version only. Remove serial numbers and unique device identifiers.
2. Record browser build ID and whether this is an isolated test application or the stock browser.
3. Keep network conditions and test media consistent across runs. Use legally distributable, known test content.
4. Note whether keyboard, software automation or physical remote control produced each input. Do **not** treat scripted input as equivalent to physical remote behavior.

## Manual browser lifecycle test

1. Launch the test application through its normal user-facing icon.
2. Confirm its visible title, focus and response to navigation.
3. Open a page containing a normal HTML5 video element.
4. Enter fullscreen through the on-screen player button; record whether the video **and shell** enter fullscreen.
5. Press Back on the *physical* remote. Record which layer exits fullscreen.
6. Press Back again where appropriate; verify navigation/exit prompt behavior.
7. Confirm application Exit and whether the Home screen returns, then verify the app has stopped.

For each action record outcome, reproducibility (for example, 3/3), time-to-response and whether a second remote press was necessary. A successful system API close is **not** proof of a physical remote Exit.

## Media verification matrix

Repeat short and longer sessions at supported resolutions. For each session capture:
- media container and codecs; stream delivery (progressive or MSE);
- resolution, FPS, HDR metadata *if actually detected*;
- startup-to-first-rendered-frame latency, dropped/total frames and seek-to-frame latency;
- A/V drift, audio track switches, visible buffering/repeated segments;
- CPU and RSS where measurable;
- **decoder backend evidence**, not just browser capability flags.

Only claim 4K/HDR or hardware decoding when measured on the actual TV with sufficient evidence. Browser-reported `video_decode=enabled` is insufficient.

## Reporting

Use anonymized [format validation](../tools/validate_report.py), [lifecycle checks](../tools/browser_lifecycle.py) and [playback measurement summaries](../tools/analyze_playback.py). These tools **analyze supplied reports only**; they do not run or instrument the browser.

Reference: [limited historical LG device observations](REAL_DEVICE_OBSERVATIONS.md). Do not fill missing values from those observations with estimates.

## Safety

Do not change firmware, privileged system components, device access permissions or SSH configuration as part of these steps. Do not publish private device URLs, keys, account identifiers, system logs or proprietary binaries.
