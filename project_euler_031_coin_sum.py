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


def get_coin_sums(target, denominations):
    top = denominations[0]
    if target < top:
        return []
    else:
        return 0



def get_num_coin_sum():
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]

    ways_to_200 = get_coin_sums(200, denominations)

    return len(ways_to_200)


def main():
    answer = get_num_coin_sum()
    print(f"The Answer to Project Euler 031 is {answer}")


if __name__ == "__main__":
    main()
