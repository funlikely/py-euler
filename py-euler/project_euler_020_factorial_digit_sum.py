"""
    Factorial digit sum

    Problem 20

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
"""
from utilities.bignum import *


def get_factorial_digit_sum():
    print(BigNum('123').multiply(BigNum('12')).value)
    print(BigNum('99').multiply(BigNum('99')).value)
    print(BigNum('99999999999').multiply(BigNum('99999999999')).value)
    print(BigNum('999999999999999').multiply(BigNum('999999999999999')).value)

    factorial = BigNum('1')
    for i in range(1, 100):
        factorial = factorial.multiply(BigNum(str(i)))

    print(factorial.value)

    factorial_digits_total = 0
    for i in range(len(factorial.value)):
        factorial_digits_total += int(factorial.value[i])
    print("the sum of digits in 100! is " + str(factorial_digits_total))
    return factorial_digits_total


def main():
    answer = get_factorial_digit_sum()
    print(f"The Answer to Project Euler 020 is {answer}")

    # The Answer to Project Euler 020 is 648


if __name__ == "__main__":
    main()
