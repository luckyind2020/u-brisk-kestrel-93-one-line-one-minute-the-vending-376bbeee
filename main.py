"""Vending machine pickup line: read entry.txt and print the line."""

import pathlib


def load_line():
    path = pathlib.Path(__file__).with_name("entry.txt")
    line = path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError("entry.txt is empty")
    if len(line) > 200:
        raise ValueError("pickup line exceeds the 200-character limit")
    return line


def main():
    print(load_line())


if __name__ == "__main__":
    main()
