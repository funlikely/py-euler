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

start_fresh = False

# consider using
# sys.set_int_max_str_digits(50000)
# sys.set_int_max_str_digits(4300)
# sys.get_int_max_str_digits()


def initialize_fib_numbers_with_data_file_if_possible():
    if start_fresh:
        return 2, BigNum('1'), BigNum('1')
    f = open("data/project_euler_104.txt")
    lines = f.readlines()
    counter = int(lines[-3])
    fib_a = BigNum(lines[-2].strip('\n'))
    fib_b = BigNum(lines[-1].strip('\n'))
    return counter, fib_a, fib_b


def get_answer() -> (int, BigNum):
    counter, fib_a, fib_b = initialize_fib_numbers_with_data_file_if_possible()

    check = True
    first_nine = last_nine = ''
    first_nine_count = last_nine_count = 0

    while check:
        fib_c = fib_a.add(fib_b)
        fib_b = fib_a
        fib_a = fib_c

        fib_a_digit_count = len(str(fib_a.value))
        if fib_a_digit_count > 18:
            first_nine = str(fib_a.value)[:9]
            last_nine = str(fib_a.value)[-9:]
        counter += 1

        if counter % 8000 == 0 and debug:
            print(f'Fib({counter}): {first_nine}...{last_nine}, {fib_a_digit_count} digits long. {first_nine_count} \
instances of first nine digits being pandigital, and {last_nine_count} instances of last nine digits being \
pandigital')

        if set(first_nine) == set('123456789'):
            first_nine_count += 1
        if set(last_nine) == set('123456789'):
            last_nine_count += 1
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
