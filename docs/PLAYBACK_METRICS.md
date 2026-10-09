# Reproducible playback measurements

`tools/analyze_playback.py` summarizes manually exported, anonymized playback measurements. It does **not** launch or control a TV, browser or media player, and cannot determine whether decoding is hardware accelerated.

The input is a JSON object with a nonempty `samples` array. Each sample requires four numeric observations:

- `startup_ms`: time from user play intent to first rendered frame, nonnegative
- `frame_drops`: number of dropped frames during a consistently defined interval, nonnegative
- `seek_ms`: time from seeking to next rendered frame, nonnegative
- `av_drift_ms`: measured audio-versus-video drift (signed, milliseconds)

The output contains median and maximum for each measurement and sample count. Compare only tests with matching device, codecs, streaming format, resolution, observation interval and playback conditions. This tool does not infer PASS/FAIL thresholds because such limits vary with hardware and use case.

```bash
python tools/analyze_playback.py examples/playback-measurements.json
python -m unittest discover -s tests -v
```

**Privacy:** do not submit raw player logs, source URLs with tokens, identifiers, internal addresses or confidential content. The sample measurements are synthetic, not evidence of actual LG or Chromium performance.
