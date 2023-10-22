"""
    Counting rectangles

    Problem 85

    By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

    Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid
    with the nearest solution."""
import time


def get_rec_count(m: int, n: int) -> int:
    total = 0
    for i in range(m):
        for j in range(n):
            total += (m - i) * (n - j)
    return total


def get_area_for_special_rectangle() -> int:
    solution_area = 0
    solution_diff = 2 * 10 ** 6
    attempt_count = 0
    solution_i, solution_j = 0, 0
    for i in range(1, 54):
        j = 1
        rec_count = get_rec_count(i, j)
        while rec_count < 2 * 10 ** 6 + solution_diff:
            if rec_count < 1 * 10 ** 6:
                j = min(j*2, j+100)
                rec_count = get_rec_count(i, j)
                continue
            if abs(rec_count - 2 * 10 ** 6) < solution_diff:
                if solution_diff < 1000:
                    print(f"i: {i}, j: {j}, rec_count: {rec_count}")
                solution_diff = abs(rec_count - 2 * 10 ** 6)
                solution_area = i * j
                solution_i = i
                solution_j = j
            j += 1
            attempt_count += 1
            rec_count = get_rec_count(i, j)

    print(f"solution i: {solution_i}, j: {solution_j}")
    return solution_area


# get_rec_count(53, 53)
# 2047761
# get_rec_count(3,816)
# 2000016
# is very close to 2 million
# get_rec_count(36, 77)
# 1999998

def main():
    start = time.time()
    answer = get_area_for_special_rectangle()
    end = time.time()
    print(f"time taken: {end-start}")
    print(f"The Answer to Project Euler 085 is {answer}")

    # The Answer to Project Euler 085 is 2772


if __name__ == "__main__":
    main()
