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
import utilities.primes as pr
import utilities.divisors as div


def get_special_distinct_primes_answer() -> int:
    return 0


debug = True


def investigate_and_debug():
    lim = 10**6
    pp = pr.PrimeProcessor(5000)
    prime_divisor_count_list = [0] * lim
    for i in range(2, lim):
        prime_divisor_count_list[i] = 1


def main():
    if debug:
        investigate_and_debug()
    answer = get_special_distinct_primes_answer()
    print(f"The Answer to Project Euler 047 is {answer}")

    # The Answer to Project Euler 047 is


if __name__ == "__main__":
    main()
