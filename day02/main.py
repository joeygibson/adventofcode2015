#! /usr/bin/env python3
import itertools
import sys


def get_data(path) -> list[list[str]]:
    with open(path) as f:
        return [line.strip().split('x') for line in f.readlines() if line.strip()]


def part1(packages: list[list[str]]) -> int:
    paper_needed = 0

    for dims in packages:
        l, w, h = [int(x) for x in dims]
        surface_area = 2 * l * w + 2 * w * h + 2 * h * l
        paper_needed += surface_area
        sides = itertools.combinations([l, w, h], 2)
        extra = min([x[0] * x[1] for x in sides])
        paper_needed += extra

    return paper_needed


def part2(packages: list[list[str]]) -> int:
    pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: main.py <filename>')
        sys.exit(1)

    file_name = sys.argv[1]

    print(f'part1 {part1(get_data(file_name))}')
    print()
    print(f'part2 {part2(get_data(file_name))}')
