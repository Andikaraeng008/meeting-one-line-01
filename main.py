"""The Meeting That Should Have Been One Line — make.fun entry.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt. Deterministic: same line
on every run.
"""

import os

LINE = (
    "The client already said yes in the email we were meeting "
    "to read out loud to each other."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
