"""
    Path sum: two ways

    Problem 81

    In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right
    and down, is indicated in bold red and is equal to 2427. Find the minimal path sum from the top left to the bottom
    right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file
    containing an 80 by 80 matrix.
"""
import time


def get_minimal_path_sum():
    return 0


def main():
    start = time.time()
    answer = get_minimal_path_sum()
    end = time.time()
    print(f"time taken: {end-start}")
    print(f"The Answer to Project Euler 081 is {answer}")

    # The Answer to Project Euler 081


if __name__ == "__main__":
    main()
