"""Fortune in a Pot - one-line fortune for a windowsill houseplant."""

import os

LINE = "Good news, little windowsill friend: the sun loves you, water is coming, and your leaves are about to look fabulous."

assert 1 <= len(LINE) <= 120 and LINE.strip(), "LINE must be 1-120 chars and non-blank"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
