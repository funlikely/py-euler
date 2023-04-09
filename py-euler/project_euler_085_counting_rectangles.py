"""
    Counting rectangles

    Problem 85

    By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

    Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

"""


def get_rec_count(m: int, n: int) -> int:
    total = 0
    for i in range(m):
        for j in range(n):
            total += (m - i) * (n - j)
    return total

def get_area_for_special_rectangle() -> int:
    rec_count = get_rec_count(2, 3)
    return 0

# get_rec_count(3,816)
# 2000016
# is very close to 2 million


def main():
    answer = get_area_for_special_rectangle()
    print(f"The Answer to Project Euler 079 is {answer}")

    # The Answer to Project Euler 079 is 73162890


if __name__ == "__main__":
    main()
