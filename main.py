"""The Meeting That Should Have Been One Line — make.fun entry.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt. Deterministic: same line
on every run.
"""

import os

LINE = (
    "I joined from the parking lot, approved the budget from my car, "
    "and the meeting still needed forty more minutes to agree I had approved it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
