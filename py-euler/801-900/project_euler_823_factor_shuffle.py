"""
    Factor Shuffle

    Problem 823

    A list initially contains the numbers 2, 3, ..., n At each round, every number in the list is divided by its
    smallest prime factor. Then the product of these smallest prime factors is added to the list as a new number.
    Finally, all numbers that become are removed from the list.

    For example, below are the first three rounds for n = 5:



    Let S(n,m) be the sum of all numbers in the list after m rounds.
    For example, S(5,3) = 15 + 2 + 4 = 21. Also S(10, 100) = 257

    Find S(10**4, 10**16), modulo 1234567891.
"""
import math

debug = False


def get_answer(perc: float) -> int:


    return 0


def is_bouncy(k: int) -> bool:

    return True


def debug_and_investigation():
    lim = 10**3

    bounce_tracker = [False] * lim
    for i in range(lim):
        bounce_tracker[i] = is_bouncy(i)
    for i in range(99, 999, 45):
        print(f"{i} bouncy: {bounce_tracker[i]}")


def main():
    if debug:
        debug_and_investigation()
    answer = get_answer(0.99)
    print(f"The Answer to Project Euler 823 is {answer}")

    # The Answer to Project Euler 823 is


if __name__ == "__main__":
    main()
