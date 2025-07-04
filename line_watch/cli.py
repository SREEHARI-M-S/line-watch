import sys
from line_watch.engine import RegexEngine

def entry_point():
    if len(sys.argv) != 3:
        sys.exit(1)
    
    pattern = sys.argv[1]
    line_text = sys.argv[2]

    engine = RegexEngine(pattern)
    if engine.match_current_line(text):
        print("✓ - Matched")
    else:
        print("X - Not Matched")

if __name__ == "__main__":
    entry_point()