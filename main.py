"""Two Robots in an Elevator — one line of awkward robot small talk.

The entry is a single constant line: one robot, stuck in an elevator with
another robot, finally says the thing out loud — its proximity sensor has
been screaming for four floors and it still has nothing to say.
"""

import os

LINE = (
    "So... my proximity sensor's been screaming for four floors now, "
    "and I still don't know what to say to you."
)


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write the single line to the output file and return it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return LINE


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
