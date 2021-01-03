from typing import List


def part1(data):
    for line1 in data:
        for line2 in data:
            if line1 + line2 == 2020:
                return line1 * line2


def part2(data):
    for line1 in data:
        for line2 in data:
            for line3 in data:
                if line1 + line2 + line3 == 2020:
                    return line1 * line2 * line3


def main():
    filename = "Day1\\day1_input.txt"
    input: List[int] = [int(x) for x in open(filename).read().splitlines()]

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
