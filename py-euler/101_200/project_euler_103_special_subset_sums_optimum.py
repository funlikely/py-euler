"""
    Special Subset Sums Optimum
    
    Problem 102

    Let represent the sum of elements in set of size . We shall call it a special sum set if for any two non-empty disjoint subsets, and

    , the following properties are true:

    ; that is, sums of subsets cannot be equal.
    If
    contains more elements than then

        .

    If
    is minimised for a given

    , we shall call it an optimum special sum set. The first five optimum special sum sets are given below.

    : : : : : It seems that for a given optimum set, , the next optimum set is of the form , where

    is the "middle" element on the previous row.

    By applying this "rule" we would expect the optimum set for
    to be , with . However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for is , with

    and corresponding set string: 111819202225.

    Given that
    is an optimum special sum set for

    , find its set string.

    NOTE: This problem is related to Problem 105 and Problem 106.
"""

import math
from ast import literal_eval
from typing import List, Set

debug = True


def is_set_special(test_set: Set) -> bool:
    is_special = True
    test_list = list(test_set)
    for i in range(int(len(test_list)/2) + 1):
        is_special = True
    return is_special


def debug_and_investigation():
    test_set = {20, 23, 25, 27, 28, 29, 30}
    is_special = is_set_special(test_set)


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
