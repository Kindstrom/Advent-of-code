from typing import List
from collections import Counter


def part1(data):
    return sum([
        len(set(line.replace('\n', '')))
        for line
        in data
    ])
    return sum


def part2(data: List[str]):
    return sum([
        len([x for x in Counter(group).values() if x == len(group.split('\n'))])
        for group
        in data
    ])


def main():
    filename = "Day6\\day6_input.txt"
    input: List[str] = open(filename).read().split("\n\n")

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
