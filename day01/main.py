#! /usr/bin/env python3
import sys


def get_data(path) -> list[str]:
    with open(path) as f:
        return [c for c in f.read().strip()]


def part1(directions: list[str]) -> int:
    floor = 0

    for direction in directions:
        if direction == '(':
            floor += 1
        else:
            floor -= 1

    return floor


def part2(directions: list[str]) -> int:
    floor = 0

    for index, direction in enumerate(directions):
        if direction == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return index + 1

    return -10000


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(get_data(file_name))}')
    print()
    print(f'part2 {part2(get_data(file_name))}')
