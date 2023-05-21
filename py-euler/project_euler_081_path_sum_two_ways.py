"""
    Path sum: two ways

    Problem 81

    In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right
    and down, is indicated in bold red and is equal to 2427. Find the minimal path sum from the top left to the bottom
    right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file
    containing an 80 by 80 matrix.
"""
import time

debug_and_test = True


def read_dummy_matrix():
    matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]
    return matrix


def read_matrix():
    file = open('data/project_euler_081.txt')
    matrix = []
    for line in file.readlines():
        matrix.append([int(a.strip('\n')) for a in line.split(',')])
    if debug_and_test:
        for i in range(3):
            print(matrix[i][0:3])
    return matrix


def get_minimal_path_sum():
    data = read_dummy_matrix()
    return 0


def main():
    start = time.time()
    answer = get_minimal_path_sum()
    end = time.time()
    print(f"time taken: {end - start}")
    print(f"The Answer to Project Euler 081 is {answer}")

    # The Answer to Project Euler 081


if __name__ == "__main__":
    main()
