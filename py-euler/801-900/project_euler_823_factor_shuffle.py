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
from itertools import product

import numpy as numpy

import utilities.primes as p

debug = True

# n = 5
# m = 3
n = 10
m = 100
prime_list = p.get_primes(int(n))  # that should be enough for now


def prime_factor_list_of(n):
    prime_factor_list = []
    for current_prime in prime_list:
        if n == 0:
            break
        while n % current_prime == 0:
            n /= current_prime
            prime_factor_list.append(current_prime)
    return prime_factor_list


def debug_and_investigation(n: int, m: int):
    factors = [prime_factor_list_of(i) for i in range(2, n + 1)]

    print(f"Factors of 2, ..., {n} are: {factors}")


def factor_shuffle(factors):
    new_combo = sorted([f[0] for f in factors])
    new_factors = [f[1:] for f in factors if len(f) > 1]
    new_factors.append(new_combo)
    return new_factors


def get_answer(n: int, m: int):
    factors = [prime_factor_list_of(i) for i in range(2, n + 1)]

    for i in range(m):
        print(f"factors {i}: {factors}")
        factors = factor_shuffle(factors)

    answer = sum([numpy.prod(f) for f in factors])

    return answer % 1234567891


def main():
    if debug:
        debug_and_investigation(n, m)
    answer = get_answer(n, m)
    print(f"The Answer to Project Euler 823 is {answer}")

    # The Answer to Project Euler 823 is


if __name__ == "__main__":
    main()
