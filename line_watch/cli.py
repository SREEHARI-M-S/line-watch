#!/usr/bin/env python3

import sys
from line_watch.engine import RegexEngine

def entry_point():
    if len(sys.argv) != 3:
        print("Usage: python cli.py <pattern> <text>")
        sys.exit(1)

    pattern = sys.argv[1]
    line_text = sys.argv[2]

    engine = RegexEngine(pattern)
    if engine.match_current_line(line_text):
        print("✓ - Matched")
    else:
        print("X - Not Matched")
