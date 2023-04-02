"""
    Large sum

    Problem 13

    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

    See data/project_euler_013.txt
"""
from utilities.bignum import *


def read_input_file():
    file = open("data/project_euler_013.txt")
    lines = [line[:-1] for line in file]
    return lines


digits_list = read_input_file()


def add_two_string_ints(a, b):
    carry = 0
    total = []
    for i in range(min(len(a), len(b))):
        digit_sum = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry
        if digit_sum > 9:
            carry = 1
            digit_sum -= 10
        else:
            carry = 0
        total.append(str(digit_sum))
    total.reverse()
    return ''.join(total)


def get_grand_total():
    for i in range(len(digits_list)):
        digits_list[i] = '0000' + digits_list[i]

    grand_total = BigNum(digits_list[0])
    for i in range(1, len(digits_list)):
        grand_total = grand_total.add(BigNum(digits_list[i]))  # add_two_string_ints(grand_total, digits_list[i])
    return grand_total


def main():
    grand_total = get_grand_total()
    print(f"The Answer to Project Euler 013 is {grand_total.value.lstrip('0')[:10]}")

    # The Answer to Project Euler 013 is 5537376230


if __name__ == "__main__":
    main()
