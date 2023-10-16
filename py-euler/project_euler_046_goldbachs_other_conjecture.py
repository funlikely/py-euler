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


debug = True


def get_goldbach_counterexample():
    pp = PrimeProcessor()
    prime_list = pp.primes_up_to(500000)

    if debug:
        print(f"prime_list length = {len(prime_list)}, and last couple primes: {prime_list[-5:]}")

    counter = 0
    max_guess = 5000000
    test_num = 9
    while test_num < max_guess:
        has_goldbach_combination = False
        i = 1
        while i ** i < test_num and not has_goldbach_combination and test_num not in prime_list:
            if (test_num - 2 * i * i) in prime_list:
                if debug and counter % 100 == 0:
                    print(f'{test_num} = {(test_num - 2 * i * i)} + 2 * {i} ^ 2')
                counter += 1
                has_goldbach_combination = True
            i += 1

        if not has_goldbach_combination and test_num not in prime_list:
            return test_num
        test_num += 2

    return 0


def main():
    answer = get_goldbach_counterexample()
    print(f"The Answer to Project Euler 046 is {answer}")

    # The Answer to Project Euler 046


if __name__ == "__main__":
    main()
