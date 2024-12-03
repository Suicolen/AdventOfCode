import re


def get_input(path):
    with open(path) as file: return file.read()


def part1():
    data = get_input("../input/day3input.txt")
    matches = re.findall(r"mul\((\d+),*(\d+)\)", data)
    return sum(int(a) * int(b) for a, b in matches)


def part2():
    data = get_input("../input/day3input.txt")
    matches = re.findall(r"(don't|do)|mul\((\d+),(\d+)\)", data)
    sum, do_flag = 0, True
    for token, a, b in matches:
        if token:
            do_flag = (token == "do")
        elif do_flag:
            sum += int(a) * int(b)
    return sum


def solutions():
    part1_solution = part1()
    part2_solution = part2()
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


solutions()
