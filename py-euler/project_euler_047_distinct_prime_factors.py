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
from typing import List

import utilities.primes as pr

debug = True

MAX_NUM = 10 ** 7

pp = pr.PrimeProcessor()
prime_list = pp.primes_up_to(MAX_NUM)


def get_distinct_prime_factors(n):
    if n in prime_list:
        return [n]
    original_n = n
    prime_list_iter = 0
    prime_factor_list = []
    while prime_list_iter < len(prime_list) and n > 1:
        prime_factor_list.append(0)
        while n % prime_list[prime_list_iter] == 0:
            n /= prime_list[prime_list_iter]
            prime_factor_list[prime_list_iter] += 1
        prime_list_iter += 1
    ret_val = [prime_list[i] for i in range(len(prime_factor_list)) if prime_factor_list[i] > 0]
    if debug and original_n % 1000 < 20 and original_n not in prime_list:
        print(f'prime_factors({original_n})={ret_val}')
    return ret_val
    # return [prime_list[:len(prime_factor_list)], prime_factor_list]


def get_single_factor_nums():
    return [i for i in range(2, 1000) if len(get_distinct_prime_factors(i)) == 1]


def get_double_factor_nums():
    return [i for i in range(2, 1000) if len(get_distinct_prime_factors(i)) == 2]


def reduce_candidates(candidates_helper: List[bool], sieve_nums: List[int]) -> List[bool]:
    for sieve in sieve_nums:
        multiple = 1
        while sieve * multiple < len(candidates_helper):
            candidates_helper[sieve * multiple] = False
            multiple += 1
    return candidates_helper


def get_special_distinct_primes_answer() -> int:
    candidates_helper = [True] * MAX_NUM

    single_factor_nums = get_single_factor_nums()
    double_factor_nums = get_double_factor_nums()

    candidates_helper = reduce_candidates(candidates_helper, single_factor_nums + double_factor_nums)

    if debug:
        print(
            f'single factor nums = {single_factor_nums[:10]}...{single_factor_nums[-10:]}, count = {len(single_factor_nums)}')
        print(
            f'double factor nums = {double_factor_nums[:10]}...{double_factor_nums[-10:]}, count = {len(double_factor_nums)}')

    prime_factors = [i for i in range(len(candidates_helper)) if
                     candidates_helper[i] and len(get_distinct_prime_factors(i)) == 4]

    if debug:
        print(
            f'possible four-prime-factor numbers: {prime_factors[:10]}...{prime_factors[:-3]}, count = {len(prime_factors)}')

    candidates = [i for i in range(len(prime_factors)) if
                  prime_factors[i] and prime_factors[i + 1] and prime_factors[i + 2] and prime_factors[
                      i + 3]]

    if debug:
        print(f'answer candidates: {candidates[:3]}...{candidates[:-3]}, count = {len(candidates)}')

    # answers = [i for i in candidates if ]

    if debug:
        print(f'last few primes: {prime_list[-5:]}')
        print(f'last few prime factors: {prime_factors[-5:]}')

    test_num = 644
    answer_found = False
    while not answer_found and test_num+3 < len(prime_factors):
        s1 = prime_factors[test_num]
        s2 = prime_factors[test_num + 1]
        s3 = prime_factors[test_num + 2]
        s4 = prime_factors[test_num + 3]
        if debug and test_num % 1000 == 0:
            print(f'{test_num}: {s1}, {test_num + 1}: {s2}, {test_num + 2}: {s3}, {test_num + 3}: {s4}')
        if len(set(s1)) == len(set(s2)) == len(set(s3)) == len(set(s4)) == 4:
            return test_num
        test_num += 1

    return 0


debug = True


def investigate_and_debug():
    lim = 10 ** 6
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
