#!/usr/bin/env python3
"""Validate anonymized browser-on-TV test reports. Standard library only."""
import argparse
import ipaddress
import json
import re
import sys
from pathlib import Path

REQUIRED = ("device_family", "webos_version", "build_id", "test_type", "environment",
            "result", "evidence")
RESULTS = {"PLANNED", "BUILT", "TESTED_ON_HOST", "VERIFIED_ON_TV"}
TYPES = {"launch", "back_exit", "fullscreen", "playback", "seek", "hardware_decode", "performance"}
FORBIDDEN_KEYS = {"password", "token", "secret", "ssh_key", "private_key", "serial_number",
                  "device_id", "mac_address", "internal_ip", "api_key"}
PRIVATE_IPV6 = re.compile(r"(?i)(?<![0-9a-f:])(?:[0-9a-f]{0,4}:){2,}[0-9a-f:.%]*")
PRIVATE_IPV4 = re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])")
MAC = re.compile(r"(?i)\b(?:[0-9a-f]{2}:){5}[0-9a-f]{2}\b")
SECRET = re.compile(r"(?i)(?:bearer\s+[a-z0-9._-]+|-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:password|api[_-]?key|token)\s*[:=]\s*\S+)")
def validate(report):
    problems = []
    if not isinstance(report, dict):
        return ["root must be a JSON object"]
    for name in REQUIRED:
        if name not in report:
            problems.append(f"missing field: {name}")
        elif not isinstance(report[name], str) or not report[name].strip():
            problems.append(f"field must be a nonempty string: {name}")
    if report.get("result") not in RESULTS:
        problems.append("invalid result state")
    if report.get("test_type") not in TYPES:
        problems.append("invalid test_type")
    if report.get("result") == "VERIFIED_ON_TV" and report.get("environment") != "TV":
        problems.append("VERIFIED_ON_TV requires environment TV")
    def scan(v, path="$"):
        if isinstance(v, dict):
            for k, x in v.items():
                if k.lower() in FORBIDDEN_KEYS or re.search(r"(?i)(?:^|[_-])(password|passwd|token|secret|credential|private[_-]?key|api[_-]?key|serial|device[_-]?id|mac[_-]?address)(?:$|[_-])", k):
                    problems.append(f"sensitive field name: {path}.{k}")
                scan(x, f"{path}.{k}")
        elif isinstance(v, list):
            for i, x in enumerate(v):
                scan(x, f"{path}[{i}]")
        elif isinstance(v, str):
            if MAC.search(v) or SECRET.search(v):
                problems.append(f"potential credential/device identifier: {path}")
            for m in PRIVATE_IPV6.finditer(v):
                try:
                    ip = ipaddress.ip_address(m.group(0).split("%")[0])
                    if not ip.is_global:
                        problems.append(f"non-public IPv6 address: {path}")
                except ValueError:
                    pass
            for m in PRIVATE_IPV4.finditer(v):
                try:
                    ip = ipaddress.ip_address(m.group(0))
                    if not ip.is_global:
                        problems.append(f"non-public IP address: {path}")
                except ValueError:
                    pass
    scan(report)
    return sorted(set(problems))
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("reports", nargs="+", type=Path)
    args = ap.parse_args(argv)
    failed = False
    for path in args.reports:
        try:
            issues = validate(json.loads(path.read_text(encoding="utf-8")))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            issues = [f"cannot parse report: {exc}"]
        print(f"{path}: {'PASS' if not issues else 'FAIL'}")
        for issue in issues:
            print(f"  - {issue}")
        failed |= bool(issues)
    return int(failed)
if __name__ == "__main__":
    sys.exit(main())
