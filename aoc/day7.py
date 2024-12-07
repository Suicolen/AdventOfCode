import itertools
import re


def get_input(path):
    with open(path) as file:
        return file.read()


def parse_target_and_values():
    return [
        (int(target), list(map(int, values.split())))
        for target, values in re.findall(r'(\d+): (\d+(?: \d+)*)', get_input("../input/day7input.txt"))
    ]


def generate_possible_operations(length, use_concat_operator):
    operators = ['+', '*', '||'] if use_concat_operator else ['+', '*']
    return itertools.product(operators, repeat=length)


def apply_operations(values, ops):
    result = values[0]
    for op, value in zip(ops, values[1:]):
        match op:
            case '+':
                result += value
            case '*':
                result *= value
            case '||':
                result = int(str(result) + str(value))
    return result


def solve(use_concat_operator):
    return sum(
        target for target, values in parse_target_and_values()
        if any(apply_operations(values, ops) == target for ops in
               generate_possible_operations(len(values) - 1, use_concat_operator))
    )


def part1():
    return solve(False)


def part2():
    return solve(True)


def solutions():
    part1_solution = part1()
    part2_solution = part2()
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


solutions()
