"""
    Sub-string divisibility

    Problem 43

    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some
    order, but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

        d2d3d4=406 is divisible by 2
        d3d4d5=063 is divisible by 3
        d4d5d6=635 is divisible by 5
        d5d6d7=357 is divisible by 7
        d6d7d8=572 is divisible by 11
        d7d8d9=728 is divisible by 13
        d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import math
import time


def get_permutation(xs, pattern):
    """
        Generate the nth permutation of a list 'xs', given the permutation pattern.
    """
    xs = sorted(xs)
    result = [xs[pattern[i]] for i in range(len(pattern))]
    return result


def get_next_level_of_permutations(a, n):
    return [a + [i] for i in range(n) if i not in a]


def flatten(xs):
    return [item for sublist in xs for item in sublist]


def generate_permutation_pattern_list(n):
    """ Generate a list of permutation patterns of size n! """
    patterns = [[i] for i in range(n)]
    for i in range(n-1):
        new_patterns = [get_next_level_of_permutations(a, n) for a in patterns]
        patterns = flatten(new_patterns)
    return patterns


def is_interestingly_divisible(perm):
    if int(str(perm)[-3:]) % 17 != 0:
        return False
    divisors = [2, 3, 5, 7, 11, 13, 17]
    f = lambda acc, m, n: acc and m % n == 0
    accumulator = True
    [accumulator := f(accumulator, int(str(perm)[i + 1:i + 4]), divisors[i]) for i in range(7)]
    return accumulator


def get_substring_divisible_pandigitals_using_permutations():
    interestingly_divisible_list = []
    count = 0
    permutation_pattern_list = generate_permutation_pattern_list(9)

    # We know the fifth digit needs to be '0' or '5', so we don't need all 10! permutations.
    # Only 2 * 9! permutations.
    for seed_string, extra_char in [("123456789", '0'), ("123406789", '5')]:
        for i in range(math.factorial(9)):
            perm_string = ''.join(get_permutation(seed_string, permutation_pattern_list[i]))
            perm = int(perm_string[:5] + extra_char + perm_string[5:])
            if count < 4 or count % 100000 == 0:
                print(f"attempt #{count}: {perm}")
            if is_interestingly_divisible(perm):
                interestingly_divisible_list.append(perm)
            count += 1

    return interestingly_divisible_list


def main():
    start_time = time.time()
    pandigitals = get_substring_divisible_pandigitals_using_permutations()
    end_time = time.time()
    print(f"time: {end_time - start_time}")
    print(f"the pandigitals: {pandigitals}")
    print(f"The Answer to Project Euler 043 is {sum(pandigitals)}")

    # the pandigitals: [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]
    # The Answer to Project Euler 043 is 16695334890


if __name__ == "__main__":
    main()
