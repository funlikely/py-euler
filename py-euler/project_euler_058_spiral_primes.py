"""
    Spiral Primes

    Problem 58

    Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

    It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting
    is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

    If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
    If this process is continued, what is the side length of the square spiral for which the ratio of primes along
    both diagonals first falls below 10%?

"""
import math
import time

debug = True

# max_num = 3 * 10 ** 9
# gotta go higher than 3 billion I suppose
max_num = 10 ** 10


def get_diagonal_numbers(n):
    d_nums = [1]

    i = 2
    while d_nums[-1:][0] < n:
        d_nums += [d_nums[-1:][0] + i * j for j in range(1,5)]
        i += 2

    if debug:
        print(f'diagonal numbers up to {n}: (count={len(d_nums)}), {d_nums[:12]}..{d_nums[-12:]}')

    return d_nums


def get_diagonal_prime_candidates(n):
    diag_num = get_diagonal_numbers(n)[1:]
    p_cand = []

    start = time.time()
    time_counter = 1
    max_possible_sieve = int(math.sqrt(diag_num[-1:][0]))
    for i in range(3, max_possible_sieve):
        # i is the sieve variable
        if diag_num[0] == i:
            p_cand += [i]
        diag_num = [a for a in diag_num if a % i != 0]
        if debug and time.time() - start - time_counter > 0:
            print(f'processing primes, {i} out of {max_possible_sieve}')
            time_counter += 8

    if debug:
        print(f'prime diagonal numbers up to {n}: (count={len(p_cand)}), {p_cand[:12]}..{p_cand[-12:]}')

    return p_cand + diag_num


def get_answer_efficient():
    p_cand = get_diagonal_prime_candidates(max_num)

    i = 3

    p = 1
    n = 1
    # find the square side length 'i' such that the ratio p/n drops below 10% where
    # p is the number of primes, and n is the number of diagonal numbers

    start = time.time()
    time_counter = 1
    max_estimator = int(math.sqrt(p_cand[-1:][0]))
    while i * i < p_cand[-1:][0]:
        p = len([a for a in p_cand if a < i * i])
        n = 2 * i - 1

        if float(p)/float(n) < 0.1:
            return i

        if debug and i % 100 == 1:
            print(f'processing ratio, {i} out of {max_estimator}, current ratio: {p}/{n}={round(float(p) / float(n), 4)}')
        if debug and time.time() - start - time_counter > 0:
            print(f'processing ratio, {i} out of {max_estimator}, current ratio: {p}/{n}={round(float(p)/float(n), 4)}')
            time_counter += 1

        i += 2

    return i


def get_answer_inefficient():
    global prime_list

    local_prime_index = 0
    local_prime_list = prime_list[local_prime_index:local_prime_index + 10000]
    local_prime_cut_off = local_prime_list[-1:][0]

    diag_nums = [1]
    ratio = 1
    prime_count = 0.0
    num_count = 1.0
    i = 2
    # 3,5,7,9
    # 13,17,21,25
    # 31,37,43,49
    while ratio > 0.10:
        nums_to_append = [diag_nums[-1:][0] + i * j for j in range(1,5)]

        if nums_to_append[3] > local_prime_cut_off:
            local_prime_index += 5000
            local_prime_list = prime_list[local_prime_index:max(len(prime_list) - 1, local_prime_index + 10000)]
            if len(local_prime_list) == 0:
                print(f'Ran out of primes!!! Max prime = {prime_list[-1:][0]}')
            local_prime_cut_off = local_prime_list[-1:][0]

        diag_nums += nums_to_append
        num_count += 4.0
        prime_count += sum([1 for num in nums_to_append if num in local_prime_list])
        ratio = prime_count / num_count
        i += 2

        if debug and i % 100 == 0:
            print(f'{int(prime_count)}/{int(num_count)} = {ratio}, max diagonal num considered: {nums_to_append[3]}')
            if nums_to_append[3] > max_num:
                print(f'Ran out of primes!! Max prime = {prime_list[-1:][0]}')

    """
        3028/29397 = 0.1030037078613464, max diagonal num considered: 216060601
        3028/29597 = 0.10230766631753219, max diagonal num considered: 219010401
        3028/29797 = 0.10162096855388127, max diagonal num considered: 221980201
        3028/29997 = 0.10094342767610094, max diagonal num considered: 224970001
        3028/30197 = 0.10027486174123257, max diagonal num considered: 227979801
        The Answer to Project Euler 058 is 15142
        
        15142 - 2 = 15140
    """
    return i-1


def main():
    answer = get_answer_efficient()
    print(f"The Answer to Project Euler 058 is {answer}")

    # The Answer to Project Euler 058 is 26241


if __name__ == "__main__":
    main()
