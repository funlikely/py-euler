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
    prime_list = pp.primes_up_to(50000)
    print(f"prime_list length = {len(prime_list)}, and last couple primes: {prime_list[-5:]}")
    square_list = [i*i for i in range(1, 5000)]
    print(f"last couple squares: {square_list[-5:]}")

    max_guess = 50000
    test_num = 9
    goldbached = False
    while test_num < max_guess and not goldbached:
        total = 0
        if False and test_num % 1001 == 0:
            print(f"testing {test_num}")
        goldbached = False
        for square in square_list:
            if square > test_num or goldbached:
                break
            for prime in prime_list:
                if square + 2*prime > test_num or goldbached:
                    break
                if square + 2*prime == test_num:
                    goldbached = True
        test_num += 2

    return 0


def main():
    answer = get_goldbach_counterexample()
    print(f"The Answer to Project Euler 046 is {answer}")

    # The Answer to Project Euler 046


if __name__ == "__main__":
    main()
