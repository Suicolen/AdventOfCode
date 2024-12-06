import time
import timeit

import numpy as np


def get_input(path):
    with open(path) as file: return file.read().splitlines()


def get_grid():
    data = get_input("../input/day6input.txt")
    return [list(row) for row in data if row.strip()]


directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

right_turns = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}


def find_initial_pos_and_dir(grid, rows, cols):
    return next(
        ((row, col), grid[row][col])
        for row in range(rows) for col in range(cols)
        if grid[row][col] in directions
    )


def count_guard_positions(grid):
    rows, cols = len(grid), len(grid[0])
    guard_pos, guard_dir = find_initial_pos_and_dir(grid, rows, cols)
    visited = {guard_pos}
    while True:
        dx, dy = directions[guard_dir]
        new_row, new_col = (guard_pos[0] + dx, guard_pos[1] + dy)
        if not (0 <= new_row < rows and 0 <= new_col < cols):
            break

        if grid[new_row][new_col] == '#':
            guard_dir = right_turns[guard_dir]
        else:
            guard_pos = (new_row, new_col)
            visited.add(guard_pos)

    return len(visited)


def simulate_with_obstacle(grid, rows, cols, obstacle_pos, guard_pos, guard_dir):
    visited_states = set()
    pos, dir = guard_pos, guard_dir
    while (pos, dir) not in visited_states:
        visited_states.add((pos, dir))
        dx, dy = directions[dir]
        new_row, new_col = (pos[0] + dx, pos[1] + dy)

        if not (0 <= new_row < rows and 0 <= new_col < cols):
            return False

        new_pos = (new_row, new_col)
        if new_pos == obstacle_pos or grid[new_row][new_col] == '#':
            dir = right_turns[dir]
        else:
            pos = new_pos

    return True


def part1():
    grid = get_grid()
    return count_guard_positions(grid)


def part2():
    grid = get_grid()
    rows, cols = len(grid), len(grid[0])
    guard_pos, guard_dir = find_initial_pos_and_dir(grid, rows, cols)
    return sum(
        simulate_with_obstacle(grid, rows, cols, (row, col), guard_pos, guard_dir)
        for row in range(rows) for col in range(cols)
        if grid[row][col] == '.' and (row, col) != guard_pos
    )


def solutions():
    part1_solution = part1()
    part2_solution = part2()
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


solutions()
