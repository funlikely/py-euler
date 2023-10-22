"""
    Sudoku

    Problem 98
"""
import time


def load_from_file():
    file = open('data/project_euler_098.txt')
    lines = file.readlines()
    grids = []
    for i in range(len(lines)):
        if lines[i].startswith('Grid'):
            grid = [[int(c) for c in line.strip('\n')] for line in lines[i + 1:i + 10]]
            grids.append(grid)
    return grids


debug = True


def update_constraints_on_grid(grid):
    new_grid = [[0 for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0 or len(str(grid[i][j])) > 2:
                row_values = ''.join([str(x) for x in grid[i] if len(str(x)) < 2])
                col_values = ''.join([str(y) for y in [grid[b][j] for b in range(9)] if len(str(y)) < 2])
                cel_values = ''.join(
                    [str(z) for z in [grid[3 * int(i / 3) + a][3 * int(j / 3) + b] for a in range(3) for b in range(3)]
                     if len(str(z)) < 2])
                constraints = [c for c in '123456789' if c not in row_values + col_values + cel_values]
                if len(constraints) == 0:
                    grid, False, False
                constraints_string = ''.join([c for c in '123456789' if c not in row_values + col_values + cel_values])
                new_grid[i][j] = int(constraints_string)
            else:
                new_grid[i][j] = grid[i][j]
    is_solved = 0 == len([new_grid[i][j] for i in range(9) for j in range(9) if len(str(new_grid[i][j])) > 1])
    return new_grid, True, is_solved


def get_test_datum(grid):
    option_count = 2
    while option_count < 8:
        test_data = [{'i': i, 'j': j, 'choices': grid[i, j]} for i in range(3) for j in range(3) if
                     len(str(grid[i, j])) == option_count]
        if len(test_data) != 0:
            return test_data[0]
        option_count += 1


def solve_grid_with_test_data(test_data, grid):
    return 0


def solve_grid(grid):
    grid, is_valid, is_solved = update_constraints_on_grid(grid)
    if is_solved:
        return grid
    if not is_valid:
        return None

    test_datum = get_test_datum(grid)
    if len(test_datum['choices']) == 1:
        return grid
    if len(test_datum['choices']) == 2:
        return solve_grid_with_test_data([test_datum], grid)

    if debug:
        print(f'updated constraints, grid: {grid}')

    return grid


def get_answer():
    sudoku_grids = load_from_file()
    if debug:
        print(f'grids:')
        for grid in sudoku_grids:
            print(f'{grid}')

    answer = 0
    for grid in sudoku_grids:
        grid = solve_grid(grid)
        grid_key = grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
        answer += grid_key

    return answer


def main():
    start = time.time()
    answer = get_answer()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Project Euler 085 is {answer}")

    # The Answer to Project Euler 085 is 2772


if __name__ == "__main__":
    main()
