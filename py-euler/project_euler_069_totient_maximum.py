"""
    Totient maximum

    Problem 69

    Euler's Totient function, [sometimes called the phi function], is defined as the number of positive integers not
    exceeding which are relatively prime to . For example, as , , , , , and , are all less than or equal to nine and
    relatively prime to nine,

    Find the value of n <= 1000000 for which is n/phi(n) a maximum.

    NOTE: phi(n) = n * prod(1 - 1/p) for all p primes dividing n
    E.g., phi(26) = 26 * 1/2 * 12/13 = 12
"""
import math

from utilities.primes import PrimeProcessor
import utilities.divisors as div


debug = True
MAX_NUMBER = 10 ** 6
pp = PrimeProcessor(MAX_NUMBER)
primes = pp.get_primes_up_to(MAX_NUMBER)


def get_prime_divisors(n):
    results = [p for p in primes if n % p == 0]
    return results


def totient(x):
    prime_factors = get_prime_divisors(x)
    n = 1
    d = 1
    for p in prime_factors:
        n *= (p-1)
        d *= p
    return int(x * n / d)


def get_maximum_totient_ratio():

    answer = 1
    tot_qot_max = 1
    for n in range(2, MAX_NUMBER):
        if n / totient(n) > tot_qot_max:
            tot_qot_max = n / totient(n)
            answer = n
            print(f"latest max n: {n}, totient: {totient(n)}, quotient: {tot_qot_max}")
    return answer


def investigate():
    print(f'some primes: {primes[0:12]}')
    print(f'some primes: {primes[-5:]}')
    print(f'some totients:')
    for i in range(2, 25):
        print(f'phi({i}) = {totient(i)}')


def main():
    if debug:
        investigate()

    answer = get_maximum_totient_ratio()
    print(f"The Answer to Project Euler 069 is {answer}")

    # The Answer to Project Euler 069


if __name__ == "__main__":
    main()
