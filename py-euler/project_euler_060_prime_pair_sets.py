"""
    Prime Pair Sets

    Problem 60

    The primes $3$, $7$, $109$, and $673$, are quite remarkable. By taking any two primes and concatenating them in
    any order the result will always be prime. For example, taking $7$ and $109$, both $7109$ and $1097$ are prime.
    The sum of these four primes, $792$, represents the lowest sum for a set of four primes with this property.</p>
    <p>Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import time

from sympy import isprime
from ast import literal_eval
import utilities.primes as pr

debug = True

MAX_NUM = 26034

pp = pr.PrimeProcessor()


def get_answer():
    MAX_PRIME=10000
    print(f'calculating / loading prime list up to {MAX_PRIME}')
    prime_list = [3] + pp.primes_up_to(MAX_PRIME)[3:]
    print(f'done calculating prime list')

    start = time.time()
    possible_answers = []
    test_counter = 1
    for i in range(len(prime_list)):
        for j in range(i+1, len(prime_list)):
            test_vals = [prime_list[i], prime_list[j]]
            if any([not isprime(num) for num in (get_test_values(test_vals))]) or sum(test_vals) + test_vals[-1]*3 >= MAX_NUM:
                continue
            for k in range(j+1, len(prime_list)):
                test_vals = [prime_list[i], prime_list[j], prime_list[k]]
                if debug and time.time() - start > 10:
                    print(f'testing sets with {test_vals} in them')
                    start = time.time()
                if any([not isprime(num) for num in (get_test_values(test_vals))]) or sum(test_vals) + test_vals[-1]*2 >= MAX_NUM:
                    continue
                for m in range(k+1, len(prime_list)):
                    test_vals = [prime_list[i], prime_list[j], prime_list[k], prime_list[m]]
                    if any([not isprime(num) for num in (get_test_values(test_vals))]) or sum(test_vals) + test_vals[-1] >= MAX_NUM:
                        continue
                    for n in range(m+1, len(prime_list)):
                        test_vals = [prime_list[i], prime_list[j], prime_list[k], prime_list[m], prime_list[n]]
                        if sum(test_vals) >= MAX_NUM:
                            continue
                        if all([isprime(num) for num in (get_test_values(test_vals))]):
                            if debug:
                                print(f'Found candidate, {test_vals}, sum = {sum(test_vals)}')
                            possible_answers += [test_vals]
                        test_counter += 1
                        if debug and test_counter % 10000 == 0:
                            print(f'test #{test_counter}; testing candidates for {test_vals}')

    print(f'Answer not found')
    return min([sum(p) for p in possible_answers])


def get_test_values(test_primes):
    return [int(str(test_primes[a]) + str(test_primes[b]))
            for a in range(len(test_primes))
            for b in range(len(test_primes))
            if a != b]


def get_answer_using_four_known_values(param):
    return 0


def main():
    start_time = time.time()
    answer = get_answer()
    print(f'Time taken: {time.time() - start_time} seconds')
    # [733, 883, 991, 18493, 55621] is a prime pair set.
    # However, sum([733, 883, 991, 18493, 55621]) = 76721 fails to be the answer. Search harder for an answer!
    # Use 76721 as a guide, perhaps
    # sum([3, 5323, 10357, 29587, 31231]) = 76501
    # sum([7, 1237, 2341, 12409, 18433]) = 34427
    # sum([13, 5197, 5701, 6733, 8389]) = 26033
    print(f"The Answer to Project Euler 060 is {answer}")

    # The Answer to Project Euler 060 is 26033


if __name__ == "__main__":
    main()
