#!/usr/bin/env python3
"""Summarize anonymized playback measurements; standard library only."""
import argparse
import json
import statistics
import sys
from pathlib import Path

FIELDS = ("startup_ms", "frame_drops", "seek_ms", "av_drift_ms")
def analyze(data):
    if not isinstance(data, dict) or not isinstance(data.get("samples"), list) or not data["samples"]:
        raise ValueError("samples must be a non-empty array")
    samples = data["samples"]
    for i, sample in enumerate(samples):
        if not isinstance(sample, dict):
            raise ValueError(f"sample {i} must be an object")
        for field in FIELDS:
            v = sample.get(field)
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not (-1000000 < v < 1000000):
                raise ValueError(f"sample {i}: invalid {field}")
            if field != "av_drift_ms" and v < 0:
                raise ValueError(f"sample {i}: negative {field}")
    result = {"sample_count": len(samples)}
    for field in FIELDS:
        vals = [x[field] for x in samples]
        result[field] = {"median": statistics.median(vals), "maximum": max(vals)}
    return result

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file", type=Path)
    args = ap.parse_args()
    try:
        report = analyze(json.loads(args.file.read_text(encoding="utf-8")))
    except (OSError, ValueError) as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2))
    return 0
if __name__ == "__main__":
    sys.exit(main())
