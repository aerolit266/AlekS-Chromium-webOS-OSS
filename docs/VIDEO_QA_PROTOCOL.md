# AlekS / GameFree24 — video QA: time-series screenshots and playback proof

This is a reusable QA procedure for AlekS/ GameFree24 video applications, browsers and players. It does not authorize device modifications or require elevated access. On a non-webOS target, use a supported platform-specific capture method and preserve the same evidence rules.

## Required capture series

For every playback start, capture **five frames** at nominal T+0, T+2, T+5, T+10 and T+20 seconds. For seek/resume, additionally capture at T_seek+0, +2 and +5 seconds. Record the **actual** timestamp for each frame: capture/API latency means actual and nominal offsets can differ. For a brief clip, sample every two seconds. Prefer a real on-screen capture mechanism rather than one isolated screenshot.

For LG webOS, a tested native screenshot API is:

```sh
luna-send -n 1 -f luna://com.webos.service.capture/executeOneShot \
  '{"path":"/tmp/aleks-video-qa-02.png","method":"GRAPHIC","format":"PNG","width":960,"height":540}'
```

An example nonpersistent five-frame collection while an application is **already running**:

```sh
#!/bin/sh
set -eu
out="/tmp/aleks-video-qa-$(date +%s)"
mkdir -m 700 "$out"
capture() {
  tag="$1"
  file="$out/frame-$tag.png"
  printf 'FRAME=%s TIME=%s\n' "$tag" "$(date +%s)" >> "$out/timeline.txt"
  luna-send -n 1 -f luna://com.webos.service.capture/executeOneShot \
    "{\"path\":\"$file\",\"method\":\"GRAPHIC\",\"format\":\"PNG\",\"width\":960,\"height\":540}" \
    > "$out/capture-$tag.json"
  if [ -s "$file" ]; then sha256sum "$file" >> "$out/SHA256SUMS"; fi
}
capture 0
sleep 2; capture 2
sleep 3; capture 5
sleep 5; capture 10
sleep 10; capture 20
```

The command creates a new private temporary folder; it does not install an application, alter controller routing or modify firmware. Do not collect screenshots containing secrets or other people's content without authorization. Save evidence privately and remove temporary device files only after verifying a retained copy and SHA256.

## Interpreting evidence

1. Record application ID/foreground, screen capture method and return status, file size, SHA256 and actual sampling time. Where available collect playback position, decoder frame counters, media VDEC/ADEC state, audio and network diagnostics. **A decoder allocation or HTTP 200 alone is not proof of displayed playback.**
2. Compare frame pixels (not only hashes). A changing pixel region may be a loading spinner, an overlay, or video: inspect what changed before claiming decoded frames.
3. **Validate capture against a reference app** (for example Live TV). LG webOS 6 can return identical all-black PNGs for BOTH official YouTube and Live TV when hardware video is in a separate overlay. In that case classify the capture as `CAPTURE_UNRELIABLE_FOR_VIDEO`; never conclude the television physically showed a black screen. Prefer an authorized external optical capture, reliable frame counter, or physical user observation.
4. Record physical user testimony separately from API evidence: `USER_VISIBLE_VIDEO`, `USER_AUDIBLE_SOUND`, `API_UI_FRAME`, `DECODED_FRAME_COUNTER`, `NETWORK_ONLY`. Do not let an unreliable screenshot override direct user confirmation of video and sound.
5. Validate sound, pause/resume, seek, replay and sustained playback separately. Restore original foreground/network state afterward, check temporary processes and sockets, and record PASS / PARTIAL / NOT VERIFIED with real observations.

## Actual LG validation motivating this rule

On 2026-11-07 a five-point `GRAPHIC` sequence on the hall LG displayed a real loading spinner at approximately T+3 seconds (1,264 nonblack pixels), while subsequent API PNGs were black. The user directly confirmed that **video appeared AFTER that spinner**, and had previously confirmed audible sound. The correct conclusion is visible video **confirmed by user**, screenshot API **not capable of reliably showing the hardware video overlay**. TLS timeouts can still occur independently.

Repository-specific instructions and platform licensing take priority over this generic procedure. This is original AlekS/GameFree24 QA documentation; it grants no rights to upstream proprietary code.
