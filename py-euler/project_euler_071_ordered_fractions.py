"""
    Ordered Fractions
    Problem 71

    What n will give the closest value of n/d to 3/7 if
        n/d is a reduced fration and
        n/d<3/7 and
        d is between 1 and 10^6?

"""
import math
import fractions

debug = True


def get_answer():
    n = 1
    d = 1
    min_diff = 1
    for new_d in range(1, 10 ** 6 + 1):
        new_n = math.floor(3.0 * new_d / 7.0)
        diff_to_test = 3.0/7.0 - float(new_n)/float(new_d)
        if diff_to_test < min_diff and new_d % 7 != 0:
            if debug:
                print(f'{new_n}/{new_d} is closer to 3/7 than {n}/{d}, diff = {diff_to_test}')
            n = new_n
            d = new_d
            min_diff = diff_to_test

    n = fractions.Fraction(n, d).numerator

    return n


def main():
    answer = get_answer()
    print(f"The Answer to Project Euler 071 is {answer}")

    # The Answer to Project Euler 071 is 428570


if __name__ == "__main__":
    main()
