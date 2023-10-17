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

MAX_NUM = 1 * 10 ** 7

pp = pr.PrimeProcessor()


def load_prime_list():
    try:
        file = open('data/project_euler_060.txt')
        int_list = [int(line.strip('\n')) for line in file.readlines()]
        if len(int_list) == 0:
            raise ValueError('no primes found')
        if int_list[-1:][0] > MAX_NUM:
            if debug:
                print(f'Loaded primes from file')
            return [i for i in int_list if i <= MAX_NUM]
    except:
        print(f'file not found')
    if debug:
        print(f'calculating primes using PrimeProcessor')
    return pp.primes_up_to(MAX_NUM)


def save_prime_list(prime_list):
    readfile = open('data/project_euler_060.txt', 'r')
    lines = readfile.readlines()
    if len(lines) < len(prime_list):
        file = open('data/project_euler_060.txt', 'w')
        file.writelines([str(p) + '\n' for p in prime_list])
        file.close()
        if debug:
            print(f'Primes saved')
    else:
        print(f'Primes didn''t need to be saved')


def get_answer():
    print(f'calculating / loading prime list up to {MAX_NUM}')
    prime_list = load_prime_list()
    print(f'done calculating prime list')

    save_prime_list(prime_list)

    # primes that are 1 mod 3, or 2 mod 3
    prime_list1 = []
    prime_list2 = []

    counter = 1
    for prime in [p for p in prime_list if p < 10000]:
        if prime % 3 == 1 and int('3' + str(prime)) in prime_list and int(str(prime) + '3') in prime_list:
            prime_list1.append(prime)
        elif prime % 3 == 2 and int('3' + str(prime)) in prime_list and int(str(prime) + '3') in prime_list:
            prime_list2.append(prime)
        if counter % 1000 == 0:
            print(f'counter = {counter}. Generating prime_list1 and prime_list2')
        counter += 1

    # try with the '3', and three other primes from one of prime_list1 or prime_list2
    test1_counter = 1
    test2_counter = 1
    for i in range(min(len(prime_list1), len(prime_list2))):
        prime1_bad = prime2_bad = False
        test_primes1 = [3, prime_list1[i]]
        test_values1 = [int(str(test_primes1[a]) + str(test_primes1[b]))
                        for a in range(2)
                        for b in range(2)
                        if a != b]
        test_values_primeness1 = [num in prime_list for num in test_values1]
        if False in test_values_primeness1:
            prime1_bad = True
        test_primes2 = [3, prime_list2[i]]
        test_values2 = [int(str(test_primes2[a]) + str(test_primes2[b]))
                        for a in range(2)
                        for b in range(2)
                        if a != b]
        test_values_primeness2 = [num in prime_list for num in test_values2]
        if False in test_values_primeness2:
            prime2_bad = True
        for j in range(i):
            if not prime1_bad:
                test_primes1 = [3, prime_list1[i], prime_list1[j]]
                test_values1 = [int(str(test_primes1[a]) + str(test_primes1[b]))
                                for a in range(3)
                                for b in range(3)
                                if a != b]
                test_values_primeness1 = [num in prime_list for num in test_values1]
                if False in test_values_primeness1:
                    prime1_bad = True
            if not prime2_bad:
                test_primes2 = [3, prime_list2[i], prime_list2[j]]
                test_values2 = [int(str(test_primes2[a]) + str(test_primes2[b]))
                                for a in range(3)
                                for b in range(3)
                                if a != b]
                test_values_primeness2 = [num in prime_list for num in test_values2]
                if False in test_values_primeness2:
                    prime2_bad = True
            for k in range(j):
                if not prime1_bad:
                    test_primes1 = [3, prime_list1[i], prime_list1[j], prime_list1[k]]
                    test_values1 = [int(str(test_primes1[a]) + str(test_primes1[b]))
                                    for a in range(4)
                                    for b in range(4)
                                    if a != b]
                    test_values_primeness1 = [num in prime_list for num in test_values1]
                    if False in test_values_primeness1:
                        prime1_bad = True
                if not prime2_bad:
                    test_primes2 = [3, prime_list2[i], prime_list2[j], prime_list2[k]]
                    test_values2 = [int(str(test_primes2[a]) + str(test_primes2[b]))
                                    for a in range(4)
                                    for b in range(4)
                                    if a != b]
                    test_values_primeness2 = [num in prime_list for num in test_values2]
                    if False in test_values_primeness2:
                        prime2_bad = True
                for m in range(k):
                    if not prime1_bad:
                        test_primes1 = [3, prime_list1[i], prime_list1[j], prime_list1[k], prime_list1[m]]
                        test_values1 = [int(str(test_primes1[a]) + str(test_primes1[b]))
                                        for a in range(4)
                                        for b in range(4)
                                        if a != b]
                        test_values_primeness1 = [num in prime_list for num in test_values1]
                        if False not in test_values_primeness1:
                            return test_primes1
                        test1_counter += 1
                    if not prime2_bad:
                        test_primes2 = [3, prime_list2[i], prime_list2[j], prime_list2[k], prime_list2[m]]
                        test_values2 = [int(str(test_primes2[a]) + str(test_primes2[b]))
                                        for a in range(5)
                                        for b in range(5)
                                        if a != b]
                        test_values_primeness2 = [num in prime_list for num in test_values2]
                        if False not in test_values_primeness2:
                            return test_primes2
                        test2_counter += 1
                    if debug and not prime1_bad and test1_counter % 100 < 2:
                        print(f'Test1 #{test1_counter}. Tested {test_primes1}')
                        true_count1 = len([x for x in test_values_primeness1 if x])
                        if true_count1 > 9:
                            print(f'almost there! pairs that worked: {true_count1}')
                    if debug and not prime2_bad and test2_counter % 100 < 2:
                        print(f'Test2 #{test2_counter}. Tested {test_primes2}')
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
