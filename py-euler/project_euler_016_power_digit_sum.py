"""
    Power digit sum

    Problem 16

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
"""
from utilities.bignum import *


def get_power_digit_sum():
    n = BigNum('0' * 320 + '1')

    for i in range(1000):
        n = n.add(n)
        print(f'{str(i + 1).rjust(4, " ")} : {n.value}')

    power_digit_sum = 0
    for i in range(len(n.value)):
        power_digit_sum += int(n.value[i])

    print(f"power digit sum = {power_digit_sum}")
    return power_digit_sum


def main():
    answer = get_power_digit_sum()
    print(f"The Answer to Project Euler 016 is {answer}")

    # The Answer to Project Euler 016 is 1366


if __name__ == "__main__":
    main()
