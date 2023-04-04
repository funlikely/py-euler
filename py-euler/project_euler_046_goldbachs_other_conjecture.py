"""
    Goldbach's other conjecture

    Problem 46

    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

    9 = 7 + 2×12
    15 = 7 + 2×22
    21 = 3 + 2×32
    25 = 7 + 2×32
    27 = 19 + 2×22
    33 = 31 + 2×12

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from utilities.primes import PrimeProcessor


def get_goldbach_counterexample():
    pp = PrimeProcessor()
    prime_list = pp.primes_up_to(5000)
    square_list = [i*i for i in range(5000)]
    return 0


def main():
    answer = get_goldbach_counterexample()
    print(f"The Answer to Project Euler 046 is {answer}")

    # The Answer to Project Euler 046


if __name__ == "__main__":
    main()
