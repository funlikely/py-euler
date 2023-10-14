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
import sys
import time

from utilities.bignum import *

start_fresh = False

# consider using
# sys.set_int_max_str_digits(90000)
# sys.set_int_max_str_digits(4300) # default
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
    start_time = time.time()

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
pandigital. Elapsed time = {round(time.time() - start_time, 1)} seconds')

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


def get_answer_using_fib_skip_algorithm() -> (int, int):
    """
        This uses the knowledge that if we know F(a-1) and F(a) and wish to know F(b-1) and F(b) where b > a

            F(b-1) = [F(b-a-1)] * F(a-1) + [F(b-a)] * F(a)
            F(b)   = [F(b-a)] * F(a-1) + [F(b-a+1)] * F(a)

        Which means, as long as we have a cache of all the 'low' Fibonacci numbers that could be represented by

            F(b-a-1), F(b-a), and F(b-a+1)

        We can skip across finding any Fibonacci values we want, without needing to process intermediate Fib values
    """
    sys.set_int_max_str_digits(90000)

    a, b, c = 1, 1, 1
    pan_digital_enders = []
    counter = 3
    while counter < 10**6:
        c = a + b % 10**9
        b = a
        a = c
        if counter > 500 and set(str(a)[-9:]) == set('123456789'):
            pan_digital_enders += [counter]
        counter += 1

    if debug:
        print(f"Fibonacci indices for which the ends are 1-9 pandigital = {pan_digital_enders}")

    return 1, 1


def main():
    if debug:
        debug_and_investigation()

    use_big_num = False

    if use_big_num:
        answer, fib_number = get_answer()
        fib_number_string = fib_number.value
    else:
        answer, fib_number = get_answer_using_fib_skip_algorithm()
        fib_number_string = str(fib_number)

    print(f"The Answer to Project Euler 104 is {answer}")
    if debug:
        print(f"The fibonacci number starts with {fib_number_string[:30]} and is {len(fib_number_string)} digits long.")

    # The Answer to Project Euler 104 is __


def initialize_fib_numbers_with_data_file_if_possible_without_bignum() -> (int, int, int):
    if start_fresh:
        return 2, 1, 1
    f = open("data/project_euler_104.txt")
    lines = f.readlines()
    counter = int(lines[-3])
    fib_a = int(lines[-2].strip('\n'))
    fib_b = int(lines[-1].strip('\n'))
    return counter, fib_a, fib_b


def get_answer_without_bignum() -> (int, int):
    start_time = time.time()

    counter, fib_a, fib_b = initialize_fib_numbers_with_data_file_if_possible_without_bignum()

    check = True
    first_nine = last_nine = ''
    first_nine_count = last_nine_count = 0

    while check:
        fib_c = fib_a + fib_b
        fib_b = fib_a
        fib_a = fib_c

        fib_a_digit_count = len(str(fib_a))
        if fib_a_digit_count > 18:
            first_nine = str(fib_a)[:9]
            last_nine = str(fib_a)[-9:]
        counter += 1

        if counter % 8000 == 0 and debug:
            print(f'Fib({counter}): {first_nine}...{last_nine}, {fib_a_digit_count} digits long. {first_nine_count} \
instances of first nine digits being pandigital, and {last_nine_count} instances of last nine digits being \
pandigital. Elapsed time = {round(time.time() - start_time, 1)} seconds')

        if set(first_nine) == set('123456789'):
            first_nine_count += 1
        if set(last_nine) == set('123456789'):
            last_nine_count += 1
        if set(first_nine) == set(last_nine) == set('123456789'):
            check = False

    return counter, fib_a


def main_without_bignum():
    # The default is 4300
    sys.set_int_max_str_digits(90000)
    answer, fib_number = get_answer_without_bignum()
    print(f"The Answer to Project Euler 104 is {answer}")
    if debug:
        print(f"The fibonacci number starts with {str(fib_number)[:30]} and is {len(str(fib_number))} digits long.")


if __name__ == "__main__":
    # main_without_bignum()
    main()
