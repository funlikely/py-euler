"""
    Prime Pair Sets

    Problem 60

    The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in
    any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime.
    The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
    <p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from typing import List
import utilities.primes as pr

debug = True

MAX_NUM = 2 * 10 ** 5

pp = pr.PrimeProcessor()
prime_list = pp.primes_up_to(MAX_NUM)


def get_answer():
    # primes that are 1 mod 3, or 2 mod 3
    prime_list1 = []
    prime_list2 = []

    for prime in prime_list:
        if prime % 3 == 1:
            prime_list1.append(prime)
        elif prime % 3 == 2:
            prime_list2.append(prime)

    # try with the '3', and three other primes from one of prime_list1 or prime_list2
    test_counter = 1
    for i in range(min(len(prime_list1), len(prime_list2))):
        for j in range(i):
            for k in range(j):
                test_primes1 = [3, prime_list1[i], prime_list1[j], prime_list1[k]]
                test_values1 = [int(str(test_primes1[a]) + str(test_primes1[b]))
                                for a in range(4)
                                for b in range(4)
                                if a != b]
                test_values_primeness1 = [num in prime_list for num in test_values1]
                if False not in test_values_primeness1:
                    return test_primes1
                test_counter += 1
                test_primes2 = [3, prime_list2[i], prime_list2[j], prime_list2[k]]
                test_values2 = [int(str(test_primes2[a]) + str(test_primes2[b]))
                                for a in range(4)
                                for b in range(4)
                                if a != b]
                test_values_primeness2 = [num in prime_list for num in test_values2]
                if False not in test_values_primeness2:
                    return test_primes2
                test_counter += 1
                if debug and test_counter % 1000 < 2:
                    print(f'Test #{test_counter}. Tested {test_primes1}, and {test_primes2}')
                    true_count1 = len([x for x in test_values_primeness1 if x])
                    if true_count1 > 9:
                        print(f'almost there! pairs that worked: {true_count1}')
                    true_count2 = len([x for x in test_values_primeness2 if x])
                    if true_count2 > 9:
                        print(f'almost there! pairs that worked: {true_count2}')
    return 1


def main():
    answer = get_answer()
    print(f"The Answer to Project Euler 060 is {answer}")

    # The Answer to Project Euler 060 is


if __name__ == "__main__":
    main()
