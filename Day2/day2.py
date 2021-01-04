from typing import List
import re


def part1(data):
    return (
        sum(
            int(min_freq) <= password.count(letter) <= int(max_freq)
            for min_freq, max_freq, letter, password in re.findall(
                r"(\d+)-(\d+)\s+(\w+):\s+(\w+)", data
            )
        )
    )


def part2(data):
    counter = 0
    for i, j, letter, password in re.findall(
        r"(\d+)-(\d+)\s+(\w+):\s+(\w+)", data
    ):
        if (
            password[int(i) - 1] == letter and password[int(j) - 1] != letter
        ):
            counter = counter + 1
        elif (
            password[int(i) - 1] != letter and password[int(j) - 1] == letter
        ):
            counter = counter + 1

    return counter


def main():
    filename = "Day2\\day2_input.txt"
    input: List[str] = open(filename).read()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
