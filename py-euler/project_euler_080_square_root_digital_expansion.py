"""
    Square Root Digital Expansion

    Problem 80

    It is well known that if the square root of a natural number is not an integer, then it is irrational. The
    decimal expansion of such square roots is infinite without any repeating pattern at all.

    The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits
    is 475.

    For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal
    digits for all the irrational square roots.

"""
import math
from typing import List


def get_root_digits(i) -> int:
    root_digits = int(math.sqrt(i * 10 ** 200))

    # this is only accurate out to fifteen digits or so, so we need an algorithm to refine this

    return root_digits


def get_answer():
    total = 0
    for i in range(1, 101):
        if i in [1, 4, 9, 16, 25, 36, 49, 64, 81]:
            continue
        root_digits = get_root_digits(i)
        root_digit_sum = sum([int(s) for s in str(root_digits)])
        print(f'root({i}): {root_digits}, sum of digits: {root_digit_sum}')
        total += root_digit_sum

    return total


def main():
    answer = get_answer()
    print(f"The Answer to Project Euler 080 is {answer}")

    # The Answer to Project Euler 080 is -


if __name__ == "__main__":
    main()
