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
import utilities.primes as p

debug = True

n = 10
m = 100
prime_list = p.get_primes(int(10000))  # that should be enough for now


def get_answer(perc: float) -> int:


    return 0


def is_bouncy(k: int) -> bool:

    return True




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


def main():
    if debug:
        debug_and_investigation(n, m)
    answer = get_answer(0.99)
    print(f"The Answer to Project Euler 823 is {answer}")

    # The Answer to Project Euler 823 is


if __name__ == "__main__":
    main()
