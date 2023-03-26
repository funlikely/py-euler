"""
Digit fifth powers
Problem 030
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


"""
import math


def get_fifth_power_sums():
    powers = [math.pow(i, 5) for i in range(0, 10)]
    fifth_power_sums = [100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f
                        for a in range(10)
                        for b in range(10)
                        for c in range(10)
                        for d in range(10)
                        for e in range(10)
                        for f in range(10)
                        if (100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f == powers[a] + powers[b] + powers[c] + powers[d] + powers[e] + powers[f])
                        and 100000 * a + 10000 * b + 1000 * c + 100 * d + 10 * e + f > 1]
    return fifth_power_sums


def main():
    fifth_power_sums = get_fifth_power_sums()
    print(f"The Answer to Project Euler 030 is {sum(fifth_power_sums)}")

    # The Answer to Project Euler 030 is 443839

if __name__ == "__main__":
    main()
