def get_input(path):
    with open(path) as file: return file.read()


def get_grid():
    data = get_input("../input/day4input.txt")
    return [list(row) for row in data.splitlines() if row.strip()]


def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    directions = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0)]
    return sum(
        all(
            0 <= x + dx * i < rows and
            0 <= y + dy * i < cols and
            grid[x + dx * i][y + dy * i] == word[i]
            for i in range(len(word))
        )
        for x in range(rows)
        for y in range(cols)
        if grid[x][y] == word[0]
        for dx, dy in directions
    )


def part1():
    grid = get_grid()
    return count_word_occurrences(grid, "XMAS")


def part2():
    grid = get_grid()
    rows, cols = len(grid), len(grid[0])
    return sum(
        grid[x][y] == 'A' and
        {grid[x - 1][y - 1], grid[x + 1][y + 1]} == {'M', 'S'} and
        {grid[x - 1][y + 1], grid[x + 1][y - 1]} == {'M', 'S'}
        for x in range(1, rows - 1)
        for y in range(1, cols - 1)
    )


def solutions():
    part1_solution = part1()
    part2_solution = part2()
    print(f"Part 1 solution: {part1_solution}")
    print(f"Part 2 solution: {part2_solution}")


solutions()
