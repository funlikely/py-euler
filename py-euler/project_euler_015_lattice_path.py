"""
    Lattice paths

    Problem 15

    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?

"""

size = 21
count_table = []
for i in range(size):
    count_table.append([[]] * size)


def count_paths(m, n):
    if n < 0 or m < 0:
        return 0
    if n == 0 or m == 0:
        if not isinstance(count_table[m][n], int):
            count_table[m][n] = 1
        return 1
    if isinstance(count_table[m][n], int):
        return count_table[m][n]
    else:
        result = count_paths(m - 1, n) + count_paths(m, n - 1)
        count_table[m][n] = result
        return result


def get_route_count():
    answer = count_paths(20, 20)
    for i in range(size):
        for j in range(size):
            print("i = {0}, j = {1}, count paths = {2}".format(str(i), str(j), str(count_table[i][j])))

    print(count_table)
    return answer


def main():
    answer = get_route_count()
    print(f"The Answer to Project Euler 015 is {answer}")

    # The Answer to Project Euler 015 is 137846528820


if __name__ == "__main__":
    main()
