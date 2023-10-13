"""
    Factor Shuffle

    Problem 823

    A list initially contains the numbers 2, 3, ..., n At each round, every number in the list is divided by its
    smallest prime factor. Then the product of these smallest prime factors is added to the list as a new number.
    Finally, all numbers that become are removed from the list.

    For example, below are the first three rounds for n = 5:



    Let S(n,m) be the sum of all numbers in the list after m rounds.
    For example, S(5,3) = 15 + 2 + 4 = 21. Also S(10, 100) = 257

    Find S(10**4, 10**16), modulo 1234567891.
"""
import ast
import math

import numpy as numpy

import utilities.primes as p

debug = True


def prime_factor_list_of(n: int, prime_list: list):
    prime_factor_list = []
    for current_prime in prime_list:
        if n == 0:
            break
        while n % current_prime == 0:
            n /= current_prime
            prime_factor_list.append(current_prime)
    return prime_factor_list


def debug_and_investigation(n: int, m: int, prime_list: list):
    # temp_prime_list = initialize_prime_list(35156)
    # print(f"Prime factors of 1234567891: {prime_factor_list_of(1234567891, temp_prime_list)}")
    # print(f"Prime factors of 1234567890: {prime_factor_list_of(1234567890, temp_prime_list)}")
    # print(f"Prime factors of 1234567800: {prime_factor_list_of(1234567800, temp_prime_list)}")
    factors = [prime_factor_list_of(i, prime_list) for i in range(2, n + 1)]

    print(f"Factors of 2, ..., {n} are: {factors}")


def factor_shuffle(factors):
    new_combo = sorted([f[0] for f in factors])
    new_factors = [f[1:] for f in factors if len(f) > 1]
    new_factors.append(new_combo)
    return new_factors


def format_factors(factors, size):
    # let's make some factor strings shorter
    s = str(factors)
    half_size = int(size/2)
    if len(s) > size:
        return s[:half_size] + '...' + s[-half_size:]
    else:
        return s


def get_answer(n: int, m: int, prime_list: list):
    factors = [prime_factor_list_of(i, prime_list) for i in range(2, n + 1)]
    factors_dict = {}
    period = -1
    period_start_index = -1
    period_found = False
    key = ""
    period_initial_factors = ""

    for i in range(m):
        if i % 50000 == 0:
            print(f"factors {i}: {format_factors(factors, 150)}")
        factors = factor_shuffle(factors)
        key = str(factors)
        if key in factors_dict and not period_found:
            period = i + 1 - factors_dict[key]
            period_start_index = factors_dict[key]
            period_found = True
            period_initial_factors = key
        factors_dict[key] = i + 1
        if period_found:
            print(f"break at index {i}")
            break

    prime_to_mod_by = 1234567891

    if period_found:
        print(f"Cycle period = {period}, period start index = {period_start_index}")
        print(f"Cycle starts with factors {period_initial_factors}")
        # answer for S(n,m) is the same as S(n, k) if k and m are the same mod p, where p is the period and
        #   if k > period_start_index
        k = (m - period_start_index) % period + period_start_index
        print(f"Calculating S(n,m) using the observed repetition, S({n}, {m}) == S({n}, {k})")
        answer_factors = ast.literal_eval(list(factors_dict.keys())[list(factors_dict.values()).index(k)])
        print(f"Answer factors: {answer_factors}")
        answer = get_mod_sum_of_factors(answer_factors, prime_to_mod_by)
    else:
        answer = get_mod_sum_of_factors(factors, prime_to_mod_by)

    return answer % prime_to_mod_by


def get_mod_sum_of_factors(answer_factors, prime_to_mod_by):
    return sum([product_mod(f, prime_to_mod_by) for f in answer_factors]) % prime_to_mod_by


def product_mod(f, prime_to_mod_by):
    product_accumulator = 1
    for i in f:
        product_accumulator = product_accumulator * i % prime_to_mod_by
    return product_accumulator


def initialize_prime_list(n):
    return p.get_primes(int(n))


def main():
    n, m = 10, 100

    prime_list = initialize_prime_list(n)

    if debug:
        debug_and_investigation(n, m, prime_list)

    answer = get_answer(n, m, prime_list)
    print(f"S({n}, {m}) = {answer}")

    n, m = 5, 3
    answer = get_answer(n, m, prime_list)
    print(f"S({n}, {m}) = {answer}")


    n, m = 78, 10**10
    # n, m = 88, 10**10
    # n, m = 155, 10**10
    prime_list = initialize_prime_list(n)
    answer = get_answer(n, m, prime_list)
    print(f"S({n}, {m}) = {answer}")

    print(f"The Answer to Project Euler 823 is {answer}")

    # The Answer to Project Euler 823 is


if __name__ == "__main__":
    main()
