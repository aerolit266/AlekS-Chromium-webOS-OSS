#!/usr/bin/env python3
"""Validate a sequence of browser lifecycle events without controlling a device."""
import argparse
import json
import sys
from pathlib import Path

EVENTS = {"LAUNCH", "READY", "ENTER_FULLSCREEN", "EXIT_FULLSCREEN", "BACK", "EXIT_REQUEST", "CLOSED"}
def check(events):
    if not isinstance(events, list) or not events:
        return ["events must be a non-empty list"]
    problems, state, fullscreen, exit_requested = [], "NEW", False, False
    for i, event in enumerate(events):
        if not isinstance(event, str) or event not in EVENTS:
            problems.append(f"event {i}: unknown event")
            continue
        if event == "LAUNCH" and state == "NEW":
            state = "LAUNCHED"
        elif event == "READY" and state == "LAUNCHED":
            state = "READY"
        elif event == "ENTER_FULLSCREEN" and state == "READY" and not fullscreen:
            fullscreen = True
        elif event == "EXIT_FULLSCREEN" and state == "READY" and fullscreen:
            fullscreen = False
        elif event == "BACK" and state == "READY":
            if fullscreen:
                fullscreen = False
            else:
                exit_requested = True
        elif event == "EXIT_REQUEST" and state == "READY":
            exit_requested = True
        elif event == "CLOSED" and state == "READY" and exit_requested:
            state = "CLOSED"
        else:
            problems.append(f"event {i}: invalid transition ({state}, fullscreen={fullscreen}, exit_requested={exit_requested}) -> {event}")
    if state != "CLOSED":
        problems.append(f"incomplete lifecycle: {state}")
    return problems

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", type=Path)
    args = ap.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
        problems = check(data["events"]) if isinstance(data, dict) else ["root must be object"]
    except (OSError, ValueError, KeyError) as exc:
        problems = [str(exc)]
    print("PASS" if not problems else "FAIL")
    for p in problems:
        print(p)
    return bool(problems)
if __name__ == "__main__":
    sys.exit(main())
