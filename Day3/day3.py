from typing import List
from operator import mul
from functools import reduce


def calculate_slope(coordinate_moves, data):
    line_length = len(data[0])
    result = []
    for dx, dy in coordinate_moves:
        counter = 0
        x = 0
        for line in data[::dy]:
            counter += line[x] == "#"
            x = (x + dx) % line_length
        result.append(counter)
    return reduce(mul, result, 1)


def part1(data):
    coordinate_moves = [(3, 1)]
    return calculate_slope(coordinate_moves, data)


def part2(data):
    coordinate_moves = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]
    return calculate_slope(coordinate_moves, data)


def main():
    filename = "Day3\\day3_input.txt"
    input: List[str] = open(filename).read().splitlines()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
