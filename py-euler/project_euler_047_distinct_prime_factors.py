"""
    Distinct primes factors

    Problem 47

    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these
    numbers?
"""
import math

from project_euler_012_highly_divisible_triangular_number import triangle
from project_euler_044_pentagon_numbers import is_pentagonal


def get_special_distinct_primes_answer() -> int:
    return 0


debug = True


def investigate_and_debug():
    pass


def main():
    if debug:
        investigate_and_debug()
    answer = get_special_distinct_primes_answer()
    print(f"The Answer to Project Euler 047 is {answer}")

    # The Answer to Project Euler 047 is


if __name__ == "__main__":
    main()
