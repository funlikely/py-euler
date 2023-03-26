"""
    Digit factorials

    Problem 34

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: As 1! = 1 and 2! = 2 are not sums they are not included.

"""
import math


def sum_of_digit_factorials(x):
    result = math.factorial(x % 10)
    while x > 10:
        x = int(x/10)
        result += math.factorial(x % 10)
    return result


def get_digit_factorials():
    result = []
    for x in range(3,3628000):
        if x == sum_of_digit_factorials(x):
            result.append(x)
            print(f"{x}")
    return result


def main():
    answer = get_digit_factorials()
    print(f"The Answer to Project Euler 034 is {sum(answer)}")

    # The Answer to Project Euler 034 is 40730


if __name__ == "__main__":
    main()
