"""
    Truncatable primes
    
    Problem 37
    
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
    
    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""
import math

import utilities.primes as pr


max_prime = 800000
prime_list = pr.primes_up_to(max_prime)
prime_sieve_list = pr.prime_sieve_up_to(max_prime)


def get_truncatable_primes():
    """
        First solution
        An iterative and imperative method for finding the solution, that does work.
    """
    truncatable_primes = set()  # 3797 should be one of these
    check_count = 0

    for p in prime_list:
        check_count += 1
        if check_count % 10000 == 0:
            print(f'Checking attempt {check_count}')
        if not prime_sieve_list[p % 1000]:
            continue
        if int(p/1000) > 1 and not prime_sieve_list[int(p/1000)]:
            continue
        is_truncatable = check_left_trunc(p) and check_right_trunc(p)
        if is_truncatable and p > 10:
            print(f"#{len(truncatable_primes) + 1} : {p}")
            truncatable_primes.add(p)
        if len(truncatable_primes) == 11:
            break

    return truncatable_primes


def get_truncatable_primes_using_list_comprehension():
    """
        2nd version for the solution
    """
    return [p
            for p in prime_list
            if check_left_trunc_recursive(p) and check_right_trunc_recursive(p) and p > 10]


def get_truncatable_primes_using_a_fold():
    """
        3rd version for the solution
    """
    return [p
            for p in prime_list
            if left_and_right_check(p) and p > 10]


def left_and_right_check(p):
    """helper method for 3rd version"""
    p_left_shorts = [int(p % math.pow(10, i + 1)) for i in range(int(math.log(p, 10)) + 1)]
    p_right_shorts = [int(p / math.pow(10, i)) for i in range(int(math.log(p, 10)) + 1)]
    f = lambda acc, x: acc and x
    accumulator = True
    [accumulator := f(accumulator, prime_sieve_list[x]) for x in p_left_shorts + p_right_shorts]
    return accumulator


def check_left_trunc_recursive(p):
    return prime_sieve_list[p] if p < 10 else prime_sieve_list[p] and check_left_trunc_recursive(left_shorten_p(p))


def check_left_trunc(p):
    is_truncatable = True
    left_p = p
    while left_p > 10:
        left_p = left_shorten_p(left_p)
        if not prime_sieve_list[left_p]:
            is_truncatable = False
    return is_truncatable


def check_right_trunc_recursive(p):
    return prime_sieve_list[p] if p < 10 else prime_sieve_list[p] and check_right_trunc_recursive(right_shorten_p(p))


def check_right_trunc(p):
    is_truncatable = True
    right_p = p
    while right_p > 10:
        right_p = right_shorten_p(right_p)
        if not prime_sieve_list[right_p]:
            is_truncatable = False
    return is_truncatable


def left_shorten_p(left_p):
    return int(left_p % math.pow(10, int(math.log(left_p, 10))))


def right_shorten_p(right_p):
    return int(right_p/10)


def main():
    answer = get_truncatable_primes_using_a_fold()
    print(f"The Answer to Project Euler 037 is {sum(answer)}")

    # The Answer to Project Euler 037 is 748317


if __name__ == "__main__":
    main()
