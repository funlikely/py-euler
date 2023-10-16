"""
    Distinct primes factors

    Problem 47

    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these
    numbers?
"""
import math
import utilities.primes as pr

debug = True

pp = pr.PrimeProcessor()
prime_list = pp.primes_up_to(50000)


def get_prime_factor_list(n):
    prime_list_iter = 0
    prime_factor_list = []
    while prime_list_iter < len(prime_list) and n > 1:
        prime_factor_list.append(0)
        while n % prime_list[prime_list_iter] == 0:
            n /= prime_list[prime_list_iter]
            prime_factor_list[prime_list_iter] += 1
        prime_list_iter += 1
    return [prime_list[i] for i in range(len(prime_factor_list)) if prime_factor_list[i] > 0]
    # return [prime_list[:len(prime_factor_list)], prime_factor_list]


def have_distinct_prime_factors(s1, s2, s3, s4):
    total_set_count = len(set(s1 + s2 + s3 + s4))
    if len(set(s1)) + len(set(s2 + s3 + s4)) > total_set_count:
        if len(set(s2)) + len(set(s1 + s3 + s4)) > total_set_count:
            if len(set(s3)) + len(set(s1 + s2 + s4)) > total_set_count:
                if len(set(s4)) + len(set(s1 + s2 + s3)) > total_set_count:
                    return True
    return False


def get_special_distinct_primes_answer() -> int:

    prime_factors = [get_prime_factor_list(i) for i in range(50000)]

    if debug:
        print(f'last few primes: {prime_list[-5:]}')
        print(f'last few prime factors: {prime_factors[-5:]}')

    test_num = 644
    answer_found = False
    while not answer_found:
        s1 = prime_factors[test_num]
        s2 = prime_factors[test_num+1]
        s3 = prime_factors[test_num+2]
        s4 = prime_factors[test_num+3]
        if debug and test_num % 1000 == 0:
            print(f'{test_num}: {s1}, {test_num + 1}: {s2}, {test_num+2}: {s3}, {test_num + 3}: {s4}')
        if have_distinct_prime_factors(s1, s2, s3, s4):
            return test_num
        test_num += 1

    return 0


debug = True


def investigate_and_debug():
    lim = 10**6
    pp = pr.PrimeProcessor(5000)
    prime_divisor_count_list = [0] * lim
    for i in range(2, lim):
        prime_divisor_count_list[i] = 1


def main():
    if debug:
        investigate_and_debug()
    answer = get_special_distinct_primes_answer()
    print(f"The Answer to Project Euler 047 is {answer}")

    # The Answer to Project Euler 047 is


if __name__ == "__main__":
    main()
