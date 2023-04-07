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
from utilities.primes import PrimeProcessor
import utilities.divisors as div

pp = PrimeProcessor(1000000)
primes = pp.primes_up_to(1000000)


def get_prime_divisors(n):
    prime_factors = div.prime_factors(n)  # this method is failing because it's not going high enough.  test 5086121 for example
    return [p for i, p in enumerate(prime_factors[0]) if prime_factors[1][i] > 0]


def totient(n):
    prime_factors = get_prime_divisors(n)
    prod = 1
    for p in prime_factors[0]:
        prod *= (1-1/p)
    return n * prod


def get_totient_kind_of_maximum():
    int_max = 1000000
    answer = 1
    tot_qot_max = 1
    for n in range(2, int_max):
        if n / totient(n) > tot_qot_max:
            tot_qot_max = n / totient(n)
            answer = n
            print(f"latest max n: {n}, totient: {totient(n)}, quotient: {tot_qot_max}")
    return answer


def main():
    answer = get_totient_kind_of_maximum()
    print(f"The Answer to Project Euler 069 is {answer}")

    # The Answer to Project Euler 069


if __name__ == "__main__":
    main()
