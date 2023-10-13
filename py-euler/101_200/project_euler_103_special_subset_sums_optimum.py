"""
    Special Subset Sums Optimum
    
    Problem 102

    Let S(A) represent the sum of elements in set of size n. We shall call it a special sum set if for any two non-empty
    disjoint subsets, B and C, the following properties are true:

    Sums of subsets cannot be equal.
    If B contains more elements than C, then S(B) > S(C)

    If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special
    sum sets are given below.

    n = 1: {1}
    n = 2: {1, 2}
    n = 3: {2, 3, 4}
    n = 4: {3, 5, 6, 7}
    n = 5: {6, 9, 11, 12, 13}

    It seems that for a given optimum set, A = {a1, a2, ..., an}, the next optimum set is of the form
    B = {b, a1+b, a2+b, ..., an+b}, where b is the "middle" element on the previous row.

    By applying this "rule" we would expect the optimum set for n=6 to be
    A = {11, 17, 20, 22, 23, 24}, with S(A) = 117.

    However, this is not the optimum set,
    as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is
    A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.

    Given that A is an optimum special sum set for n = 7, find its set string.

    NOTE: This problem is related to Problem 105 and Problem 106.
"""

import math
from ast import literal_eval
from typing import List, Set

debug = True


def is_set_special(test_set: Set) -> bool:
    is_special = True
    test_list = list(test_set)
    if len(test_list) > 9:
        print(f"Go back to school, I'm not doing 3^9 comparisons for you")
        return False
    for i in range(3**len(test_list)):
        list_a, list_b, partitioner, place = [], [], i, 0
        while partitioner > 0:
            if partitioner % 3 == 1:
                list_a += [test_list[place]]
            elif partitioner % 3 == 2:
                list_b += [test_list[place]]
            place += 1
            partitioner = int(partitioner/3)
        if len(list_a) > 0 and len(list_b) > 0:
            if sum(list_a) == sum(list_b):
                return False
            if len(list_a) > len(list_b) and sum(list_b) > sum(list_a):
                return False

    return is_special


def debug_and_investigation():
    special_sets = [{1}, {1, 2}, {2, 3, 4}, {3, 5, 6, 7}, {6, 9, 11, 12, 13},
                    {11, 18, 19, 20, 22, 25},
                    {11, 17, 20, 22, 23, 24},
                    {22, 33, 39, 42, 44, 45, 46}]
    non_special_sets = [{2, 4, 5, 7}, {20, 23, 25, 27, 28, 29, 30},
                        {22, 33, 35, 42, 44, 45, 46}]

    for test_set in special_sets:
        is_special = is_set_special(test_set)
        print(f"set: {test_set}, is special: {is_special}")
    for test_set in non_special_sets:
        is_special = is_set_special(test_set)
        print(f"set: {test_set}, is special: {is_special}")


def get_answer():
    return {20, 23, 25, 27, 28, 29, 30}


def main():
    if debug:
        debug_and_investigation()
    answer = get_answer()
    print(f"The Answer to Project Euler 102 is {answer}")

    # The Answer to Project Euler 102 is 228


if __name__ == "__main__":
    main()
