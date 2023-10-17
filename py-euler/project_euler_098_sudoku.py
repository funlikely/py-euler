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
            grid = [[int(c) for c in line.strip('\n')] for line in lines[i+1:i+10]]
            grids.append(grid)
    return grids


debug = True


def solve_grid(grid):
    pass


def get_answer():
    sudoku_grids = load_from_file()
    if debug:
        print(f'grids:')
        for grid in sudoku_grids:
            print(f'{grid}')
    
    answer = 0
    for grid in sudoku_grids():
        grid = solve_grid(grid)
        grid_key = grid[0][0]*100+grid[0][1]*10+grid[0][2]
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
