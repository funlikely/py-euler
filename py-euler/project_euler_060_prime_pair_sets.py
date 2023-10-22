"""
    Prime Pair Sets

    Problem 60

    The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in
    any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime.
    The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
    <p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from sympy import isprime
from ast import literal_eval
import utilities.primes as pr

debug = True

MAX_NUM = 8 * 10 ** 4

pp = pr.PrimeProcessor()


def get_answer():
    print(f'calculating / loading prime list up to {MAX_NUM}')
    prime_list = [3] + pp.primes_up_to(MAX_NUM)[3:]
    print(f'done calculating prime list')

    test_counter = 1
    for i in range(len(prime_list)):
        for j in range(i+1, len(prime_list)):
            test_vals = [prime_list[i], prime_list[j]]
            if any([not isprime(num) for num in (get_test_values(test_vals))]) or sum(test_vals) > 76721:
                continue
            for k in range(j+1, len(prime_list)):
                test_vals = [prime_list[i], prime_list[j], prime_list[k]]
                if any([not isprime(num) for num in (get_test_values(test_vals))]) or sum(test_vals) > 76721:
                    continue
                for m in range(k+1, len(prime_list)):
                    test_vals = [prime_list[i], prime_list[j], prime_list[k], prime_list[m]]
                    if any([not isprime(num) for num in (get_test_values(test_vals))]) or sum(test_vals) > 76721:
                        continue
                    for n in range(m+1, len(prime_list)):
                        test_vals = [prime_list[i], prime_list[j], prime_list[k], prime_list[m], prime_list[n]]
                        if sum(test_vals) > 76721:
                            continue
                        if all([isprime(num) for num in (get_test_values(test_vals))]):
                            return test_vals
                        test_counter += 1
                        if debug and test_counter % 1000 == 0:
                            print(f'test #{test_counter}; testing candidates for {test_vals}')

    # test_counter = 1
    # for i in range(len(prime_list)):
    #     test_primes1 = [7, prime_list[i]]
    #     test_values_primeness1 = [isprime(num) for num in (get_test_values(test_primes1))]
    #     test1_bad = not all(test_values_primeness1)
    #     for j in range(len(prime_list)):
    #         if test1_bad:
    #             break
    #         if not test1_bad:
    #             test_primes1 = [7, prime_list[i], prime_list[j]]
    #             test_values_primeness1 = [isprime(num) for num in (get_test_values(test_primes1))]
    #             test1_bad = not all(test_values_primeness1)
    #         for k in range(len(prime_list)):
    #             if test1_bad:
    #                 break
    #             if not test1_bad:
    #                 test_primes1 = [7, prime_list[i], prime_list[j], prime_list[k]]
    #                 test_values_primeness1 = [isprime(num) for num in (get_test_values(test_primes1))]
    #                 test1_bad = not all(test_values_primeness1)
    #             for m in range(len(prime_list)):
    #                 if test1_bad:
    #                     break
    #                 if not test1_bad:
    #                     test_primes1 = [7, prime_list[i], prime_list[j], prime_list[k], prime_list[m]]
    #                     test_values_primeness1 = [isprime(num) for num in (get_test_values(test_primes1))]
    #                     if False not in test_values_primeness1:
    #                         return test_primes1
    #                     test_counter += 1
    #                 if debug and not test1_bad and test_counter % 100 < 2:
    #                     print(f'Test1 #{test_counter}. Tested {test_primes1}')
    #                     true_count1 = len([x for x in test_values_primeness1 if x])
    #                     if true_count1 > 9:
    #                         print(f'almost there! pairs that worked: {true_count1}')
    print(f'Answer not found')
    return None


def get_test_values(test_primes):
    return [int(str(test_primes[a]) + str(test_primes[b]))
            for a in range(len(test_primes))
            for b in range(len(test_primes))
            if a != b]


def get_answer_using_four_known_values(param):
    return 0


def main():
    answer = get_answer()
    # [733, 883, 991, 18493, 55621] is a prime pair set.
    # However, sum([733, 883, 991, 18493, 55621]) = 76721 fails to be the answer. Search harder for an answer!
    # Use 76721 as a guide, perhaps
    print(f"The Answer to Project Euler 060 is {answer}")

    # The Answer to Project Euler 060 is


if __name__ == "__main__":
    main()
