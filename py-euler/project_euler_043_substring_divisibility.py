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


def generate_permutation_pattern(a, remainder):
    result = []
    for i in range(a - 1, 0, -1):
        result.append(int(remainder / math.factorial(i)))
        remainder %= math.factorial(i)
    return result


def generate_permutation(xs, n):
    """
        Generate the nth lexicographical permutation of string or list.
    :param xs:
    :param n:
    :return:
    """
    result = []
    xs = sorted(xs)
    pattern = generate_permutation_list(len(xs))[n]  # generate_permutation_pattern(len(xs), n)
    for i in range(len(xs) - 1):
        selected = xs[pattern[i]]
        result.append(selected)
        xs.remove(selected)
    result += xs
    return result


def generate_permutation_list(xs):
    xs = sorted(xs)
    permutation_list = []
    for j in range(math.factorial(len(xs))):
        remainder = j
        permutation = []
        for i in range(len(xs) - 1, 0, -1):
            permutation.append(int(remainder / math.factorial(i)))
            remainder %= math.factorial(i)

        result = []
        working_list = xs
        for i in range(len(xs) - 1):
            selected = working_list[permutation[i]]
            result.append(selected)
            working_list.remove(selected)

        permutation_list.append(result)
    return permutation_list


def get_next_level_of_permutations(a, n):
    return [a + [i] for i in range(n) if i not in a]


def flatten(xs):
    return [item for sublist in xs for item in sublist]


def generate_permutation_patterns2(n):
    """
        Generate a list of permutation patterns of size n!

        Want to be able to do the following,

        > perm_list
        [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
        > s
        'asd'
        > [''.join([s[i] for i in a]) for a in pie]
        ['asd', 'ads', 'sad', 'sda', 'das', 'dsa']
    :param n:
    :return:
    """
    patterns = [[i] for i in range(n)]
    for i in range(n-1):
        # [0, 1, 2] --> [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]]
        new_patterns = [get_next_level_of_permutations(a, n) for a in patterns]
        patterns = flatten(new_patterns)
    #
    #     patterns = patterns + [i] * math.factorial(n - 1)
    # for i in range(1, n):
    #     for j in range(len(patterns)):
    #         patterns[j].append(get_n_not_yet_in_pattern(patterns[j], n))
    return patterns


def get_n_not_yet_in_pattern(pattern, n):
    for i in range(n):
        if i not in pattern:
            return i
    return -1


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
    seed_string = "123456789"
    count = 0
    for i in range(math.factorial(9)):
        perm_string = ''.join(generate_permutation(seed_string, i))
        perm = int(perm_string[:5] + '0' + perm_string[5:])
        if count < 10 or count % 10000 == 0:
            print(f"permutation #{i}: {perm}")
        if is_interestingly_divisible(perm):
            interestingly_divisible_list.append(perm)
        count += 1
    seed_string = "123406789"
    for i in range(math.factorial(9)):
        perm_string = ''.join(generate_permutation(seed_string, i))
        perm = int(perm_string[:5] + '5' + perm_string[5:])
        if count < 10 or count % 10000 == 0:
            print(f"permutation #{i}: {perm}")
        if is_interestingly_divisible(perm):
            interestingly_divisible_list.append(perm)
        count += 1
    return interestingly_divisible_list


def main():

    patterns = generate_permutation_patterns2(3)

    pandigitals = get_substring_divisible_pandigitals_using_permutations()
    print(f"the pandigitals: {pandigitals}")
    print(f"The Answer to Project Euler 043 is {sum(pandigitals)}")

    # The Answer to Project Euler 043 is 16695334890


if __name__ == "__main__":
    main()
