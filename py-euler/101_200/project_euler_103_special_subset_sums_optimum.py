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

debug = False


def is_set_special(test_set: Set) -> bool:
    is_special = True
    test_list = list(test_set)
    if len(test_list) > 9:
        if debug:
            print(f"Go back to school, I'm not doing more than 3^9 comparisons for you")
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
                if debug:
                    print(f"Set {test_set} is not special because sum({set(list_a)}) = sum({set(list_b)})")
                return False
            if len(list_a) > len(list_b) and sum(list_b) > sum(list_a):
                if debug:
                    print(f"Set {test_set} is not special because sum({set(list_b)}) > sum({set(list_a)})")
                return False

    return is_special


def debug_and_investigation():
    special_sets = [{1}, {1, 2}, {2, 3, 4}, {3, 5, 6, 7}, {6, 9, 11, 12, 13},
                    {11, 18, 19, 20, 22, 25},
                    {11, 17, 20, 22, 23, 24},
                    {22, 33, 39, 42, 44, 45, 46}]
    non_special_sets = [{2, 4, 5, 7}, {20, 23, 25, 27, 28, 29, 30},
                        {22, 33, 35, 42, 44, 45, 46}, {22, 33, 36, 42, 44, 45, 46},
                        {3, 4, 36, 42, 44, 45, 46},
                        {53, 59, 77, 88, 90, 91, 92, 93},
                        {43, 58, 77, 96, 97, 102},
                        {301, 302, 303, 460, 465},
                        {3, 4, 36, 42, 44, 45, 46, 55, 77, 88}]

    for test_set in special_sets:
        is_special = is_set_special(test_set)
        print(f"set: {test_set}, is special: {is_special}")
    for test_set in non_special_sets:
        is_special = is_set_special(test_set)
        print(f"set: {test_set}, is special: {is_special}")


def increment_test_list(test_list: List, max_element: int) -> List:
    if sum(test_list) < max_element:
        return test_list[:-1] + [test_list[-1:][0] + 1]
    else:
        partial_increment_list = increment_test_list(test_list[:-1], max_element)
        return partial_increment_list + [partial_increment_list[-1:][0] + 1]
    return test_list


def get_answer():
    non_optimal_special_set = {22, 33, 39, 42, 44, 45, 46}
    non_optimal_sum = sum(non_optimal_special_set)

    optimal_candidate = list(non_optimal_special_set)

    print(f"non optimal sum = {non_optimal_sum}")

    counter = 1
    # test_list = [i for i in range(14, 21)]
    test_list = [20, 30, 34, 35, 36, 45, 46]  # something of a lucky guess given that the solution started with 20, 31
    # test_list = [20, 30, 39, 40, 42, 45, 31]
    while test_list[0] < 25:
        if counter % 10000 == 0:
            print(f"test {counter}, set {test_list}")
        if is_set_special(set(test_list)) and sum(test_list) < sum(optimal_candidate):
            optimal_candidate = test_list
            print(f"found optimal candidate {optimal_candidate}, sum = {sum(optimal_candidate)}")
            test_list[0] = 25
        test_list = increment_test_list(test_list, sum(optimal_candidate))
        counter += 1

    return "".join([str(i) for i in sorted(optimal_candidate)])


def main():
    if debug:
        debug_and_investigation()
    answer = get_answer()
    print(f"The Answer to Project Euler 102 is {answer}")

    # The Answer to Project Euler 103 is 20313839404245


if __name__ == "__main__":
    main()
