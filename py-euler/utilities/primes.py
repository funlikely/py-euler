# Primes utilities
import math
from typing import List


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


def get_primes(n):
    prime_list = []
    sieve = prime_sieve(n)
    for i in range(2, len(sieve)):
        if sieve[i]:
            prime_list.append(i)
    return prime_list


class PrimeProcessor:

    def __init__(self, limit=2):
        self.prime_sieve = [False]
        self.prime_list = []
        self.limit = limit
        self.prime_sieve = self.get_prime_sieve_up_to(limit)
        self.prime_list = self.get_primes_up_to(limit)

    def get_prime_sieve_up_to(self, n):
        """Return a list of booleans representing the primes up to n-1."""
        if sum([1 for x in self.prime_sieve if x]) >= n:
            f = lambda acc, x: acc + 1 if x else acc
            accumulator = 0
            acc_list = [accumulator := f(accumulator, self.prime_sieve[x]) for x in range(len(self.prime_sieve))]
            return self.prime_sieve[0: acc_list.index(n)]
        else:
            self.generate_prime_sieve_and_list_up_to(n)
            self.limit = n
            return self.prime_sieve

    def generate_prime_sieve_and_list_up_to(self, n):
        """Return a list of booleans representing the primes up to n, inclusive."""
        """Also sets self.prime_list based on prime_sieve"""
        sieve = [True] * (n+1)
        sieve[0] = sieve[1] = False
        current_prime_list = []
        primes_found = 0
        sieve_counter = 2
        while sieve_counter < len(sieve):
            if sieve[sieve_counter]:
                primes_found = primes_found + 1
                current_prime_list.append(sieve_counter)
                sieve_action_counter = sieve_counter*2
                while sieve_action_counter < len(sieve):
                    sieve[sieve_action_counter] = False
                    sieve_action_counter += sieve_counter
            sieve_counter += 1
        for sieve_counter in range(sieve_counter, len(sieve)):
            sieve[sieve_counter] = False
        self.prime_list = current_prime_list
        self.prime_sieve = sieve

    def get_primes_up_to(self, n):
        """Primes up to n, inclusive."""
        if len(self.prime_list) > 0 and self.prime_list[-1:][0] >= n:
            return [p for p in self.prime_list if p <= n]
        else:
            self.generate_prime_sieve_and_list_up_to(n)
            return [p for p in self.prime_list if p <= n]

    def prime_factors(self, n: int) -> dict:
        prime_list = self.get_primes_up_to(n)
        prime_list_iter = 0
        prime_factor_list = []
        prime_factor_dict = {}
        while prime_list_iter < len(prime_list) and n > 1:
            prime_factor_list.append(0)
            while n % prime_list[prime_list_iter] == 0:
                n /= prime_list[prime_list_iter]
                prime_factor_list[prime_list_iter] += 1
                prime = prime_list[prime_list_iter]
                if prime not in prime_factor_dict:
                    prime_factor_dict[prime] = 1
                else:
                    prime_factor_dict[prime] += 1
            prime_list_iter += 1
        return prime_factor_dict # [prime_list[:len(prime_factor_list)], prime_factor_list]

    def divisor_counter_fast(self, n):
        prime_factor_dict = self.prime_factors(n)
        for k in prime_factor_dict:
            prime_factor_dict[k] += 1

        return math.prod(prime_factor_dict.values())

    def get_divisors(self, n: int) -> List:
        prime_factor_list = self.prime_factors(n)
        divisor_list = [1]
        for p in prime_factor_list:
            new_divisor_list = []
            for j in range(prime_factor_list[p] + 1):
                for k in range(len(divisor_list)):
                    new_divisor_list.append(int(math.pow(p, j)) * divisor_list[k])
            divisor_list += new_divisor_list
        divisor_list = list(dict.fromkeys(divisor_list))
        divisor_list.sort()
        return divisor_list[:(len(divisor_list) - 1)]
