# Primes utilities
import math



def old_get_prime_sieve_up_to(n):
    return prime_sieve_up_to(n)


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


def primes_up_to(n):
    primes = prime_sieve_up_to(n)
    return [x for x in range(len(primes)) if primes[x]]


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


class PrimeProcessor:

    def __init__(self, limit=2):
        self.prime_sieve = [False]
        self.limit = limit
        self.prime_sieve = self.get_prime_sieve_up_to(limit)

    def get_prime_sieve_up_to(self, n):
        """Return a list of booleans representing the first n primes."""
        if sum([1 for x in self.prime_sieve if x]) >= n:
            f = lambda acc, x: acc + 1 if x else acc
            accumulator = 0
            acc_list = [accumulator := f(accumulator, self.prime_sieve[x]) for x in range(len(self.prime_sieve))]
            return self.prime_sieve[0: acc_list.index(n)]
        else:
            self.prime_sieve = old_get_prime_sieve_up_to(n)
            return self.prime_sieve


def main():
    tryout = PrimeProcessor(12)
    print(tryout.prime_sieve)
    tryout.get_prime_sieve_up_to(6)
    print(tryout.prime_sieve)
    tryout.get_prime_sieve_up_to(22)
    print(tryout.prime_sieve)

    tryout2 = PrimeProcessor()
    print(tryout2.prime_sieve)
    tryout2.get_prime_sieve_up_to(6)
    print(tryout2.prime_sieve)
    tryout2.get_prime_sieve_up_to(22)
    print(tryout2.prime_sieve)


if __name__ == "__main__":
    main()