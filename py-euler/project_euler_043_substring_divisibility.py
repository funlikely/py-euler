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


def generate_permutation_pattern(a, n):
    result = []
    remainder = n
    for i in range(a - 1, 0, -1):
        result.append(int(remainder / math.factorial(i)))
        remainder %= math.factorial(i)
    return result


# generate the nth lexicographical permutation of string or list l
def generate_permutation(l, n):
    result = []
    a = len(l)
    l = sorted(l)
    pattern = generate_permutation_pattern(a, n)
    for i in range(a - 1):
        selected = l[pattern[i]]
        result.append(selected)
        l.remove(selected)
    result += l
    return result


def is_interestingly_divisible(perm):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    f = lambda acc, m, n: acc and m % n == 0
    accumulator = True
    [accumulator := f(accumulator, perm, n) for n in divisors]
    return accumulator


def get_substring_divisible_pandigitals():
    interestingly_divisible_list = []
    seed_string = "0123456789"
    start_permutation = math.factorial(9)
    count = 0
    for i in range(math.factorial(9), math.factorial(10)):
        perm = int(''.join(generate_permutation(seed_string, i)))
        if count < 10 or count % 10000 == 0:
            print(f"permutation #{i}: {perm}")
        if is_interestingly_divisible(perm):
            interestingly_divisible_list.append(perm)
        count += 1
    return interestingly_divisible_list


def main():
    pandigitals = get_substring_divisible_pandigitals()
    print(f"the pandigitals: {pandigitals}")
    print(f"The Answer to Project Euler 043 is {sum(pandigitals)}")

    # The Answer to Project Euler 043


if __name__ == "__main__":
    main()
