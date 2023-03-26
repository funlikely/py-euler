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
        #while type(ys[0][0]) is list:
        #    ys = test_flatten(ys)
        # print(f"map_cons({x},{ys})")
        result = [[x] + y for y in ys]
    else:
        result = [[x] + ys]
    print(f"map_cons({x},{ys}) = {result}")
    return result


def test_flatten(ys):
    result = [item for sublist in ys for item in sublist]
    return result


def get_coin_sums(target, denominations):
    """
        15 [5, 1]
        [0, 15], [1, 10], [2, 5], [3, 0]
        [[x] + get_coin_sums(target - x * top, denominations[1:]
    """
    top = denominations[0]
    if len(denominations) == 1:
        return [int(target / top)]
    elif target < top:
        return map_cons(0, get_coin_sums(target, denominations[1:]))
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
    # denominations = [2, 1]
    target = 200
    target = 16
    # target = 1
    ways_to_200 = get_coin_sums(target, denominations)

    return len(ways_to_200)


def get_coin_sums_iterative(target, denominations):
    count = 0
    for a in range(0, target + 1, denominations[0]):
        for b in range(0, target + 1, denominations[1]):
            for c in range(0, target + 1, denominations[2]):
                for d in range(0, target + 1, denominations[3]):
                    for e in range(0, target + 1, denominations[4]):
                        for f in range(0, target + 1, denominations[5]):
                            for g in range(0, target + 1, denominations[6]):
                                # for h in range(0, target + 1, denominations[7]):
                                # if a + b + c + d + e + f + g + h == target:
                                if a + b + c + d + e + f + g <= target:
                                    h = target - (a + b + c + d + e + f + g)
                                    if count % 10000 == 0:
                                        print(f"count = {count}, a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}")
                                    count += 1
    return count


def get_num_coin_sum_iterative():
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    # denominations = [10, 5, 2, 1]
    target = 200
    # target = 16
    count = get_coin_sums_iterative(target, denominations)

    return count


def get_num_coin_sum_quick_dirty():

    denominations = [200, 100, 50, 20, 10, 5, 2, 10]
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]

    target = 200
    ways_to_200 = [1 # (a, b, c, d, e, f, g, h)
                   for a in range(0, target + 1, denominations[0])
                   for b in range(0, target + 1, denominations[1])
                   for c in range(0, target + 1, denominations[2])
                   for d in range(0, target + 1, denominations[3])
                   for e in range(0, target + 1, denominations[4])
                   for f in range(0, target + 1, denominations[5])
                   for g in range(0, target + 1, denominations[6])
                   for h in range(0, target + 1, denominations[7])
                   if a + b + c + d + e + f + g + h == target]

    return len(ways_to_200)


def main():
    # answer = get_num_coin_sum()
    answer = get_num_coin_sum_iterative()
    print(f"The Answer to Project Euler 031 is {answer}")

    #  The Answer to Project Euler 031 is 73682


if __name__ == "__main__":
    main()
