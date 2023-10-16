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

MAX_NUM = 2 * 10 ** 5

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
    if debug and original_n > 1000 and original_n % 20000 < 6 and original_n not in prime_list:
        print(f'prime_factors({original_n})={ret_val}')
    return ret_val
    # return [prime_list[:len(prime_factor_list)], prime_factor_list]


def get_single_factor_nums():
    return [i for i in range(2, 1000) if len(get_distinct_prime_factors(i)) == 1]


def get_double_factor_nums():
    return [i for i in range(2, 1000) if len(get_distinct_prime_factors(i)) == 2]


def reduce_candidates(candidates_helper: List[bool], sieve_nums: List[int]) -> List[bool]:
    for i in prime_list:
        if i < len(candidates_helper):
            candidates_helper[i] = False
    for j in range(len(sieve_nums)):  # sieve in sieve_nums:
        sieve = sieve_nums[j]
        if debug and j % 100 == 0:
            print(f'taking out primes*sieve where sieve={sieve}')
        i = 1
        multiple = prime_list[i]
        while sieve * multiple < len(candidates_helper):
            candidates_helper[sieve * multiple] = False
            i += 1
            multiple = prime_list[i]
    return candidates_helper


def get_special_distinct_primes_answer() -> int:
    candidates_helper = [True] * MAX_NUM

    single_factor_nums = get_single_factor_nums()
    double_factor_nums = get_double_factor_nums()

    if debug:
        print(f'prime_list = {prime_list[:10]}...{prime_list[-10:]}, count = {len(prime_list)}')
        print(
            f'single factor nums = {single_factor_nums[:10]}...{single_factor_nums[-10:]}, count = {len(single_factor_nums)}')
        print(
            f'double factor nums = {double_factor_nums[:10]}...{double_factor_nums[-10:]}, count = {len(double_factor_nums)}')

    candidates_helper = reduce_candidates(candidates_helper, single_factor_nums + double_factor_nums)

    numbers_with_four_prime_factors = [i for i in range(len(candidates_helper)) if
                                       candidates_helper[i] and len(get_distinct_prime_factors(i)) == 4]

    if debug:
        print(
            f'possible four-prime-factor numbers: {numbers_with_four_prime_factors[:10]}...{numbers_with_four_prime_factors[-3:]}, count = {len(numbers_with_four_prime_factors)}')

    candidates = [numbers_with_four_prime_factors[i] for i in range(len(numbers_with_four_prime_factors) - 3) if
                  numbers_with_four_prime_factors[i + 3] - numbers_with_four_prime_factors[
                      i] == 3]

    if debug:
        print(f'answer candidates: {candidates[:3]}...{candidates[:-3]}, count = {len(candidates)}')

    # answers = [i for i in candidates if ]

    if debug:
        print(f'last few primes: {prime_list[-5:]}')
        print(f'last few prime factors: {numbers_with_four_prime_factors[-5:]}')

        print(f'prime factors for {candidates[0]}: {get_distinct_prime_factors(candidates[0])}')
        print(f'prime factors for {candidates[0] + 1}: {get_distinct_prime_factors(candidates[0] + 1)}')
        print(f'prime factors for {candidates[0] + 2}: {get_distinct_prime_factors(candidates[0] + 2)}')
        print(f'prime factors for {candidates[0] + 3}: {get_distinct_prime_factors(candidates[0] + 3)}')

    return candidates[0]


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

    # The Answer to Project Euler 047 is 134043


if __name__ == "__main__":
    main()
