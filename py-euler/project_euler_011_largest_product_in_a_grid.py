"""
    Largest product in a grid

    Problem 11

    In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
      ... see data/project_euler_011.txt
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same direction (up, down, left, right,
    or diagonally) in the 20×20 grid?
"""
import math


def read_input_file():
    file = open("data/project_euler_011.txt")
    lines = [line[:-1] for line in file]
    return lines


listOfGridNumbers = read_input_file()


def get_largest_product():
    # Load number grid
    number_grid = []
    for i in range(20):
        number_grid.append([])
        for j in range(20):
            number_grid[i].append(int(listOfGridNumbers[i][3 * j:3 * j + 2]))
    print(number_grid)

    # Max horizontal product
    max_sets = [[0, 0, 1, "horizontal"]]
    for i in range(20):
        for j in range(16):
            if math.prod(number_grid[i][j:j + 4]) > max_sets[0][2]:
                max_sets[0][0] = i
                max_sets[0][1] = j
                max_sets[0][2] = math.prod(number_grid[i][j:j + 4])
    max_sets[0].append(number_grid[max_sets[0][0]][max_sets[0][1]:max_sets[0][1] + 4])

    # Max vertical product
    max_sets.append([0, 0, 1, "vertical"])
    for i in range(16):
        for j in range(20):
            if math.prod([number_grid[i][j], number_grid[i + 1][j], number_grid[i + 2][j], number_grid[i + 3][j]]) > \
                    max_sets[1][2]:
                max_sets[1][0] = i
                max_sets[1][1] = j
                max_sets[1][2] = math.prod(
                    [number_grid[i][j], number_grid[i + 1][j], number_grid[i + 2][j], number_grid[i + 3][j]])
    max_sets[1].append([number_grid[max_sets[1][0]][max_sets[1][1]], number_grid[max_sets[1][0] + 1][max_sets[1][1]],
                        number_grid[max_sets[1][0] + 2][max_sets[1][1]],
                        number_grid[max_sets[1][0] + 3][max_sets[1][1]]])

    # Max downward sloping product
    max_sets.append([0, 0, 1, "downward sloping"])
    for i in range(16):
        for j in range(16):
            if math.prod([number_grid[i][j], number_grid[i + 1][j + 1], number_grid[i + 2][j + 2],
                          number_grid[i + 3][j + 3]]) > max_sets[2][2]:
                max_sets[2][0] = i
                max_sets[2][1] = j
                max_sets[2][2] = math.prod([number_grid[i][j], number_grid[i + 1][j + 1], number_grid[i + 2][j + 2],
                                            number_grid[i + 3][j + 3]])
    max_sets[2].append(
        [number_grid[max_sets[2][0]][max_sets[2][1]], number_grid[max_sets[2][0] + 1][max_sets[2][1] + 1],
         number_grid[max_sets[2][0] + 2][max_sets[2][1] + 2], number_grid[max_sets[2][0] + 3][max_sets[2][1] + 3]])

    # Max upward sloping product
    max_sets.append([0, 0, 1, "upward sloping"])
    for i in range(4, 20):
        for j in range(16):
            if math.prod([number_grid[i][j], number_grid[i - 1][j + 1], number_grid[i - 2][j + 2],
                          number_grid[i - 3][j + 3]]) > max_sets[3][2]:
                max_sets[3][0] = i
                max_sets[3][1] = j
                max_sets[3][2] = math.prod([number_grid[i][j], number_grid[i - 1][j + 1], number_grid[i - 2][j + 2],
                                            number_grid[i - 3][j + 3]])
    max_sets[3].append(
        [number_grid[max_sets[2][0]][max_sets[2][1]], number_grid[max_sets[2][0] - 1][max_sets[2][1] + 1],
         number_grid[max_sets[2][0] - 2][max_sets[2][1] + 2], number_grid[max_sets[2][0] - 3][max_sets[2][1] + 3]])

    print(max_sets)
    return max([a[2] for a in max_sets])


def main():
    answer = get_largest_product()
    print(f"The Answer to Project Euler 011 is {answer}")

    # The Answer to Project Euler 011 is 70600674


if __name__ == "__main__":
    main()
