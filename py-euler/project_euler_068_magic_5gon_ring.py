"""
    Magic 5-gon Ring

    Problem 68

    Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What
    is the maximum 16-digit string for a "magic" 5-gon ring?
"""
import math
from typing import List


def is_magic(gon):
    if sum(gon[0:3]) == sum(gon[3:6]) == sum(gon[6:9]) == sum(gon[9:12]) == sum(gon[12:15]):
        return True
    return False


def is_valid(gon):
    if gon[2] == gon[4] and gon[5] == gon[7] and gon[8] == gon[10] and gon[11] == gon[13] and gon[14] == gon[1]:
        if set(gon) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}:
            return True
    return False


def get_best_5gon_string():
    example = [1, 2, 3, 4, 3, 5, 6, 5, 7, 8, 7, 9, 10, 9, 2]
    print(f'example {example} is magic: {is_magic(example)}')
    print(f'example {example} is valid: {is_valid(example)}')

    counter = 0
    results = [1]
    for a in range(1, 11):
        for b in range(1, 11):
            if a == b:
                continue
            for c in range(1, 11):
                if a == c or b == c:
                    continue
                for d in range(1, 11):
                    if a == d or b == d or c == d:
                        continue
                    for e in range(1, 11):
                        if a == e or b == e or c == e or d == e:
                            continue
                        for f in range(1, 11):
                            if a == f or b == f or c == f or d == f or e == f:
                                continue
                            for g in range(1, 11):
                                if a == g or b == g or c == g or d == g or e == g or f == g:
                                    continue
                                for h in range(1, 11):
                                    if a == h or b == h or c == h or d == h or e == h or f == h or g == h:
                                        continue
                                    for i in range(1, 11):
                                        if a == i or b == i or c == i or d == i or e == i or f == i or g == i or h == i:
                                            continue
                                        for j in range(1, 11):
                                            if a == j or b == j or c == j or d == j or e == j or f == j or g == j or h == j or i == j:
                                                continue
                                            gon = [a, b, c, d, c, e, f, e, g, h, g, i, j, i, b]
                                            counter += 1
                                            if counter % 400000 == 0:
                                                print(f'testing {gon}')
                                            if not is_valid(gon):
                                                continue
                                            if is_magic(gon):
                                                print(f'{gon} is magic')
                                                gon_chain = int(''.join([str(s) for s in gon]))
                                                results.append(gon_chain)
                                                if gon_chain == max([r for r in results if r < 10**16]):
                                                    print(f'{gon_chain} is the new current maximum')

    return max([r for r in results if r < 10**16])


def main():
    answer = get_best_5gon_string()
    print(f"The Answer to Project Euler 068 is {answer}")

    # The Answer to Project Euler 068 is


if __name__ == "__main__":
    main()
