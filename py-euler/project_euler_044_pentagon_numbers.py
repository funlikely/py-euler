"""
    Pentagon numbers

    Problem 44

    Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
"""
import math


def is_pentagonal(p):
    p_root = (((1/2)+math.sqrt(1/4 + 6*p))/3)
    return p_root == int(p_root)


def generate_pent_list(size):
    return [int(i * (3 * i - 1) / 2) for i in range(size)]


def get_minimal_pentagonal_difference():
    pent_count = 50000
    pent_list = generate_pent_list(pent_count)
    # pent_bool_list = [False] * (pent_list[-1] + 1)
    # for pent in pent_list:
    #     pent_bool_list[pent] = True

    print(f"some pent numbers: {pent_list[:20]}")

    p_diff = 1  # 119000 tested up to
    is_pair_found = False
    index_pair = (0, 0)
    print()

    while not is_pair_found and p_diff < 166000:
        if p_diff % 10 == 0:
            print(f"checking min diff: {p_diff}")
        max_index_to_test = int(p_diff/3)
        test_index = 1
        while test_index < max_index_to_test:
            j = pent_list[test_index]
            k = j + p_diff

            # NOTE : commented out pent_bool_list code to see if is_pentagonal() would work better

            if is_pentagonal(k) and is_pentagonal(j+k) and is_pentagonal(k-j):
            # if pent_bool_list[k] and pent_bool_list[j + k] and pent_bool_list[k - j]:
                index_pair = (test_index, custom_index(pent_list, lambda x: x == k))
                is_pair_found = True

            test_index += 1

        p_diff += 1

    return index_pair, k-j


def custom_index(ls, f):
    return next((i for i, e in enumerate(ls) if f(e)), -1)


def main():
    index_pair, answer = get_minimal_pentagonal_difference()
    print(f"index pair {index_pair}")
    print(f"The Answer to Project Euler 044 is {answer}")

    # The Answer to Project Euler 044 


if __name__ == "__main__":
    main()
