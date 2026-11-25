"""Two Robots in an Elevator — one line of awkward robot small talk.

The entry is a single constant line: one robot, stuck in an elevator with
another robot, finally says the thing out loud — its proximity sensor has
been screaming for four floors and it still has nothing to say.

Why this line: the obvious angle is robot noises ("beep boop") or a
malfunction gag, but those are jokes *about* robots told by a human.
This line works because it is a robot confessing a very human social
failure — it has a sensor for closeness and still cannot do small talk.
The comedy is the gap between what it can sense and what it can say.
"""

import os

LINE = (
    "So... my proximity sensor's been screaming for four floors now, "
    "and I still don't know what to say to you."
)


def validate_entry(line: str) -> str:
    """Check the gate: UTF-8, single line, 1-200 chars, not only whitespace."""
    line.encode("utf-8")
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip(), "entry must not be only whitespace"
    return line


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write the single line to the output file and return it."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return LINE


def main() -> None:
    validate_entry(LINE)
    write_entry()


if __name__ == "__main__":
    main()
