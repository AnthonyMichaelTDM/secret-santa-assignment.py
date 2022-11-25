#!/usr/bin/env python3
import random
import copy


def get_names(file: str) -> list[str]:
    names: list[str] = []
    with open(file, "r") as f:
        # extract names
        names = [str(name).strip() for name in f.readlines()]

        # prune empty elements
        names = [name for name in names if name != ""]

        # remove duplicates
        names = list(set(names))

    # return names
    return names


def get_assignments(names: list[str]) -> dict[str, str]:
    assignments: dict[str, str] = {}
    names_copy: list[str] = copy.deepcopy(names)

    # generate random assignments
    # randomize the list
    random.shuffle(names_copy)
    # pair each person with the next person in the list, wrap around at the end
    for i in range(0, len(names_copy)):
        assignments[names_copy[i]] = names_copy[(i+1) % len(names_copy)]

    # ensure every person is both givin and receiving a gift
    if len(assignments) != len(names):
        raise Exception("not everyone is giving a gift")
    if len(set(assignments.values())) != len(names):
        raise Exception("not everyone is receiving a gift")

    # return assignments
    return assignments


def format_assignments(assignments: dict[str, str]) -> str:
    # get length of longest name (to ensure readable format)
    max_len: int = max([len(k) for k in assignments.keys()])

    # format each key-value pair in assignments as a string,
    # then join those strings with newline characters
    output = ".\n".join(
        [
            f"{k:<{max_len}} is giving a gift to {v}"
            for k, v in assignments.items()
        ]
    )

    # return formatted string
    return output


def main():
    # get names from names.txt
    names: list[str] = get_names("./names.txt")

    # get assignments from names
    assignments: dict[str, str] = get_assignments(names)

    # print assignments in a nice format
    print(format_assignments(assignments))


if __name__ == "__main__":
    main()
