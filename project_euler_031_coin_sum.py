"""
Coin sum
Problem 031

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

"""
import math


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist if type(sublist) is list]


def map_cons(x, ys):
    if type(ys[0]) is list:
        return [[x] + y for y in ys]
    else:
        return [x] + ys


def get_coin_sums(target, denominations):
    """
        15 [5, 1]
        [0, 15], [1, 10], [2, 5], [3, 0]
        [[x] + get_coin_sums(target - x * top, denominations[1:]
    """
    top = denominations[0]
    if target < top:
        return [0]
    elif len(denominations) == 1:
        return [int(target / top)]
    else:
        a_coin_sum = [map_cons(x, get_coin_sums(target - x * top, denominations[1:]))
                      for x
                      in range(0, int(target / top) + 1)
                      if x * top < target]
        print(f"top = {top}, target = {target}, a_coin_sum = {a_coin_sum}")
        return a_coin_sum
        # if type(a_coin_sum[0]) is list:
        # else:
        #     return a_coin_sum  # [a_coin_sum[:1] + y for y in a_coin_sum[1:]]


def get_num_coin_sum():
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    denominations = [10, 5, 2, 1]
    target = 200
    target = 16
    ways_to_200 = get_coin_sums(target, denominations)

    return len(ways_to_200)


def main():
    answer = get_num_coin_sum()
    print(f"The Answer to Project Euler 031 is {answer}")


if __name__ == "__main__":
    main()
