"""
    Circular primes

    Problem 35

    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?

"""
import math

from utilities.primes import prime_sieve_up_to


def rotate(a):
    dig_count = int(math.log(a, 10))
    return int(a / 10) + int((a % 10) * math.pow(10, dig_count))


def contains_even_digit(n):
    while n > 10:
        if n % 2 == 0:
            return True
        n = int(n/10)
    return n % 2 == 0


def get_circular_primes():
    circ_primes = [2]
    prime_sieve = prime_sieve_up_to(1000000)
    for a0 in range(3, 1000000, 2):
        if contains_even_digit(a0):
            continue
        a = a0
        is_circ_prime = True
        for b in range(0, int(math.log(a0, 10)) + 1):
            if not prime_sieve[a]:
                is_circ_prime = False
            a = rotate(a)
        if is_circ_prime:
            circ_primes.append(a0)
            if len(circ_primes) % 100 == 0:
                print(a0)
    return circ_primes


def main():
    answer = get_circular_primes()
    print(f"The Answer to Project Euler 035 is {len(answer)}")

    # The Answer to Project Euler 035 is 55


if __name__ == "__main__":
    main()
