"""
    Permuted multiples

    Problem 52

    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def is_a_super_permuter(num):
    perm_set = set(str(num))
    if perm_set == set(str(2 * num))\
            and perm_set == set(str(2 * num))\
            and perm_set == set(str(3 * num))\
            and perm_set == set(str(4 * num))\
            and perm_set == set(str(5 * num))\
            and perm_set == set(str(6 * num)):
        return True
    else:
        return False


def get_next_candidate_num(num):
    seed = 101111
    if int(str(num)[:2]) > 18:
        return seed * 10**(len(str(num)) - 5)
    else:
        return num + 1


def get_smallest_permuted_multiple(debug):
    num = 123456
    count = 0
    while not is_a_super_permuter(num) and num < 10**10:
        if count % 10000 == 0 and debug:
            print(f"trying {num} now")
        num = get_next_candidate_num(num)
        count += 1
    return num


def main():
    answer = get_smallest_permuted_multiple(False)
    print(f"The Answer to Project Euler 052 is {answer}")

    # The Answer to Project Euler 052 is 142857


if __name__ == "__main__":
    main()
