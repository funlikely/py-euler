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


def newton_rooter(n, a):
    return int(int(n) / int(2 * a)) + int(a / 2)


def get_root_digits(n) -> int:
    root_digits = int(math.sqrt(n * 10e501))
    root_digits = root_digits - int(root_digits % 10e88)
    # this is only accurate out to fifteen digits or so, so we need an algorithm to refine this
    i = 10
    while i < 100:
        s = str(root_digits)
        candidates = [int(s[:i] + str(d) + s[(i+1):]) for d in range(10)]
        diff = 10e100
        for c in candidates:
            if 0 < n * 10e200 - c ** 2 < diff:
                root_digits = c
                diff = n * 10e200 - c ** 2
        i += 1

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
