from typing import List


def part1(data):
    ids = [calculate_id(line) for line in data]
    return max(ids)


def part2(data):
    ids = [calculate_id(line) for line in data]

    for i in range(max(ids)):
        low = i - 1
        high = i + 1
        if low in ids and high in ids and i not in ids:
            return i


def calculate_id(row):
    binary = "".join(["1" if x in ["B", "R"] else "0" for x in row])
    id = int(binary, 2)
    return id


def main():
    filename = "Day5\\day5_input.txt"
    input: List[str] = open(filename).read().splitlines()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
