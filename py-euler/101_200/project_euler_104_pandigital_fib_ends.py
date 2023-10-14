"""
    Pandigital Fibonacci Ends

    Problem 104

    Let F be the Fibonacci sequence, F1 = 1, F2 = 1, F3 = 2, .., so that F = 1, 1, 2, 3, 5, . . .

    It turns out that F541 which contains 113 digits, is the first Fibonacci number for which the last nine digits
    are 1-9 pandigital (contain all the digits 1-9, but not necessarily in order). And F2749, which contains 575
    digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

    Given that Fk
    is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""
from utilities.bignum import *


def get_answer() -> (int, BigNum):
    fib_a = fib_b = BigNum('1')
    counter = 2
    check = True
    first_nine = last_nine = ''

    while check:
        fib_c = fib_a.add(fib_b)
        fib_b = fib_a
        fib_a = fib_c

        if len(str(fib_a.value)) > 18:
            first_nine = str(fib_a.value)[:9]
            last_nine = str(fib_a.value)[-9:]
        counter += 1

        if counter % 6000 == 0 and debug:
            print(f"Fib({counter}): {first_nine}...{last_nine}")

        if set(first_nine) == set(last_nine) == set('123456789'):
            check = False

    return counter, fib_a.value


debug = True


def debug_and_investigation():
    pass


def main():
    if debug:
        debug_and_investigation()
    answer, fib_number = get_answer()
    print(f"The Answer to Project Euler 104 is {answer}")
    if debug:
        print(f"The fibonacci number starts with {fib_number.value[:30]} and is {len(fib_number.value)} digits long.")

    # The Answer to Project Euler 104 is __


if __name__ == "__main__":
    main()
