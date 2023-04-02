"""
    Prime digit replacements

    Problem 51

    By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23,
    43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having
    seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773,
    and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same
    digit, is part of an eight prime value family.
"""
import utilities.primes as pr

max_try = 10 ** 6
pp = pr.PrimeProcessor(max_try)
sieve = pp.prime_sieve
primes = pp.primes_up_to(max_try)


def custom_index(ls, f):
    return next((i for i, e in enumerate(ls) if f(e)), -1)


def is_prime(param):
    return sieve[param]


def is_highly_replaceable(prime, target):
    for d in set(str(prime)):
        prime_count = len([1 for i in range(10) if
                           str(prime).replace(d, str(i))[0] != '0' and is_prime(int(str(prime).replace(d, str(i))))])
        if prime_count >= target:
            return True
    return False


def get_least_highly_replaceable_prime(target):
    print(f"number of primes being considered: {len(primes)}")

    print(f"some primes: {primes[:4]}")

    min_try = 12345  # this custom index method is neat but we don't need it a lot
    min_index = custom_index(primes, lambda x: x > min_try)
    print(f"min_prime: {primes[min_index]}")

    i = min_index
    counter = 0
    answer_found = False
    while i < len(primes):
        if counter % 1000 == 0:
            print(f"attempt #{counter}")
        if is_highly_replaceable(primes[i], target):
            answer_found = True
            break
        i += 1
        counter += 1

    if answer_found:
        return primes[i]
    else:
        return 0


def main():
    answer = get_least_highly_replaceable_prime(8)
    print(f"The Answer to Project Euler 051 is {answer}")

    # The Answer to Project Euler 051 is 121313


if __name__ == "__main__":
    main()
