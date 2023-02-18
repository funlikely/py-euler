# Primes utilities
import math


def prime_sieve(n):
    """Return a list of booleans representing the first n primes."""
    sieve = [True] * n * int(n ** 0.5 + 1)
    sieve[0] = sieve[1] = False
    prime_list = []
    primes_found = 0
    sieve_counter = 2
    while sieve_counter < len(sieve) and primes_found < n:
        if sieve[sieve_counter]:
            primes_found = primes_found + 1
            prime_list.append(sieve_counter)
            sieve_action_counter = sieve_counter * 2
            while sieve_action_counter < len(sieve):
                sieve[sieve_action_counter] = False
                sieve_action_counter += sieve_counter
        sieve_counter += 1
    for sieve_counter in range(sieve_counter, len(sieve)):
        sieve[sieve_counter] = False

    # print(str(primes_found) + ' primes found!')
    return sieve


def prime_sieve_up_to(n):
    """Return a list of booleans representing the primes up to n-1"""
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    prime_list = []
    primes_found = 0
    sieve_counter = 2
    while sieve_counter < len(sieve):
        if sieve[sieve_counter]:
            primes_found = primes_found + 1
            prime_list.append(sieve_counter)
            sieve_action_counter = sieve_counter*2
            while sieve_action_counter < len(sieve):
                sieve[sieve_action_counter] = False
                sieve_action_counter += sieve_counter
        sieve_counter += 1
    for sieve_counter in range(sieve_counter, len(sieve)):
        sieve[sieve_counter] = False

    # print(str(primes_found) + ' primes found!')
    return sieve


def get_primes(n):
    prime_list = []
    sieve = prime_sieve(n)
    for i in range(2, len(sieve)):
        if sieve[i]:
            prime_list.append(i)
    return prime_list


def prime_factors(n):
    prime_list = get_primes(int(500))  # that should be enough for now
    prime_list_iter = 0
    prime_factor_list = []
    while prime_list_iter < len(prime_list) and n > 1:
        prime_factor_list.append(0)
        while n % prime_list[prime_list_iter] == 0:
            n /= prime_list[prime_list_iter]
            prime_factor_list[prime_list_iter] += 1
        prime_list_iter += 1
    return [prime_list[:len(prime_factor_list)], prime_factor_list]


def divisor_counter_fast(n):
    prime_factor_list = prime_factors(n)[1]
    for k in range(len(prime_factor_list)):
        prime_factor_list[k] += 1
    return math.prod(prime_factor_list)
