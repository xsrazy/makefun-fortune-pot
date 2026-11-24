"""Fortune in a Pot - one-line fortune for a windowsill houseplant."""

import os

LINE = "Your leaves will catch the morning sun, your roots will stay cozy, and someone will water you right on time."

assert 1 <= len(LINE) <= 120 and LINE.strip(), "LINE must be 1-120 chars and non-blank"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
