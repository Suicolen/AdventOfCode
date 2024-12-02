def get_input(path):
    with open(path) as file: return file.read().splitlines()

def get_lists():
    return zip(*(map(int, line.split()) for line in get_input("../input/day1input.txt")))

def part1():
    left, right = map(sorted, get_lists())
    total_distance = sum(abs(r - l) for r, l in zip(left, right))
    return total_distance


def part2():
    left, right = get_lists()
    similarity_score = sum(l * right.count(l) for l in left)
    return similarity_score


def solutions():
    part1_solution = part1()
    part2_solution = part2()
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


solutions()
