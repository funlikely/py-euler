"""
    Summation of primes

    Problem 10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
"""
from utilities.primes import *


def get_prime_sum(limit):
    pp = PrimeProcessor(limit)
    primes = pp.prime_sieve
    primes_sum = sum([i for i in range(len(primes)) if primes[i] and i < limit])
    return primes_sum


def main():
    primes_sum = get_prime_sum(2000000)
    print(f"The Answer to Project Euler 010 is {primes_sum}")

    # The Answer to Project Euler 010 is 142913828922


if __name__ == "__main__":
    main()
