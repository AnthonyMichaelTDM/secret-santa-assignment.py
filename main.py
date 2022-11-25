#!/usr/bin/env python3


def get_names(file: str) -> list[str]:
    names: list[str] = []
    with open(file, "r") as f:
        # extract names
        names = [str(name).strip() for name in f.readlines()]

        # prune empty elements
        names = [name for name in names if name != ""]

    # return names
    return names


def get_assignments(names: list[str]) -> dict[str, str]:
    pass


def main():
    # get names from names.txt
    names: list[str] = get_names("./names.txt")

    # get assignments from names
    assignments: dict[str, str] = get_assignments(names)

    # print assignments in a nice format

    pass


if __name__ == "__main__":
    main()
