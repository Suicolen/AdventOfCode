from functools import cmp_to_key


def get_input(path):
    with open(path) as file: return file.read().splitlines()


def get_rules_and_updates():
    lines = get_input("../input/day5input.txt")
    split_index = lines.index("")
    rules = [list(map(int, line.split("|"))) for line in lines[:split_index]]
    updates = [list(map(int, line.split(","))) for line in lines[split_index + 1:]]
    return rules, updates


def is_correctly_ordered(update, rules):
    return all(
        update.index(a) < update.index(b)
        for a, b in rules
        if a in update and b in update
    )


def middle_element(update):
    return update[len(update) // 2]


def part1():
    rules, updates = get_rules_and_updates()
    return sum(middle_element(update) for update in updates if is_correctly_ordered(update, rules))


def get_comparator(a, b, rules):
    for rule in rules:
        if [a, b] == rule:
            return -1
        elif [b, a] == rule:
            return 1
    return 0


def part2():
    rules, updates = get_rules_and_updates()
    result = 0
    for update in updates:
        if not is_correctly_ordered(update, rules):
            update.sort(key=cmp_to_key(lambda a, b: get_comparator(a, b, rules)))
            result += middle_element(update)

    return result


def solutions():
    part1_solution = part1()
    part2_solution = part2()
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


solutions()
