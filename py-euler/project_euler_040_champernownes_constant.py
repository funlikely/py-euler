"""
    Champernowne's constant

    Problem 40

    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
import math


def champernowne_challenge():
    ranges = [int(9 * x * math.pow(10, x - 1)) for x in range(1, 7)]
    intervals = [sum(ranges[:y]) for y in range(0, 7)]
    digits_count_total = 7
    digit_index = 1
    digits = []
    while len(digits) < digits_count_total:
        intervals_index, intervals_offset = get_champer_intervals_index_and_offset(digit_index, intervals)
        champer_digit = get_champer_digit(intervals_index, intervals_offset)
        digits.append(champer_digit)
        digit_index *= 10
    return math.prod(digits)


def get_champer_intervals_index_and_offset(digit_index, intervals):
    return [(i, digit_index - intervals[i-1]) for i in range(len(intervals)) if digit_index < intervals[i]][0]


def get_champer_digit(intervals_index, intervals_offset):
    if intervals_index == 1:
        return intervals_offset
    num_pos = intervals_offset % intervals_index
    num_string = str(int(math.pow(10, intervals_index-1)) + int(intervals_offset / intervals_index))
    return int(num_string[num_pos-1])


def main():
    answer = champernowne_challenge()
    print(f"The Answer to Project Euler 040 is {answer}")

    # The Answer to Project Euler 040 is 210


if __name__ == "__main__":
    main()
