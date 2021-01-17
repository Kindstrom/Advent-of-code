from typing import List
import re


def part1(data):
    required_fields = ("ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt")
    counter = 0
    for line in data:
        if all(field in line for field in required_fields):
            counter += 1
    return counter


def part2(data: List[str]):
    counter = 0
    for line in data:
        passport = {}
        for field in line.split():
            key, value = field.split(':')
            passport[key] = value

        if vaild_passport(passport):
            counter += 1
    return counter


def vaild_passport(passport):
    # Validate that mandatory keys exist
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for f in fields:
        if(f not in passport):
            return False

    # Validate numericals
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False

    # Validate strings
    if not (
        (
            "cm" in passport['hgt']
            and 150 <= int(passport['hgt'][:-2]) <= 193
        )
            or
        (
            "in" in passport['hgt']
            and 59 <= int(passport['hgt'][:-2]) <= 76
        )
    ):
        return False

    if re.match(r'^\#[0-9a-f]{6}$', passport['hcl']) is None:
        return False

    if re.match(r'^\d{9}$', passport['pid']) is None:
        return False

    if (
        passport['ecl']
        not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ):
        return False

    return True


def main():
    filename = "Day4\\day4_input.txt"
    input: List[str] = open(filename).read().split("\n\n")

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
