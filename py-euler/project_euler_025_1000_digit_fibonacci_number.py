"""
    1000-digit Fibonacci number

    Problem 25

    The Fibonacci sequence is defined by the recurrence relation:

        Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

    Hence the first 12 terms will be:

        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144

    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
from utilities.bignum import *


def get_fibonacci_challenge():
    fibonacci_list = [BigNum('0'), BigNum('1'), BigNum('1')] + [BigNum('0')] * 12497

    for n in range(3, 12500):
        fibonacci_list[n] = (fibonacci_list[n - 1]).add(fibonacci_list[n - 2])
        if n < 6 or n % 500 == 0:
            print(f"fibonacci({n}) = {(fibonacci_list[n]).value}")
        if len((fibonacci_list[n]).value) >= 1000:
            print("1000 digits mark, fibonacci({0}) = ".format(str(n)))
            print(fibonacci_list[n].value)
            break
    return n


def main():
    answer = get_fibonacci_challenge()
    print(f"The Answer to Project Euler 025 is {answer}")

    # The Answer to Project Euler 025 is


if __name__ == "__main__":
    main()
