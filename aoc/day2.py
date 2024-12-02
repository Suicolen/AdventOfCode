from itertools import pairwise


def get_input(path):
    with open(path) as file: return file.read().splitlines()


def get_reports():
    return [[int(x) for x in line.split(" ")] for line in get_input("../input/day2input.txt")]


def is_safe(report):
    return (
            all(0 < (b - a) <= 3 for a, b in pairwise(report)) or
            all(0 < (a - b) <= 3 for a, b in pairwise(report))
    )


def part1():
    return sum(is_safe(report) for report in get_reports())


def part2():
    return sum(
        is_safe(report) or any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))
        for report in get_reports()
    )


def solutions():
    part1_solution = part1()
    part2_solution = part2()
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


solutions()
