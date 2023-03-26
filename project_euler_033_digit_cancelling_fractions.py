"""
    Digit cancelling fractions

    Problem 33

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
    incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
    digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""
import math
import fractions as f


def get_digit_cancelling_fractions():
    fractions = []

    fractions_1 = [[10*a+b, 10*b+c]
                   for a in range(1, 10)
                   for b in range(1, 10)
                   for c in range(1, 10)
                   if f.Fraction(10*a+b, 10*b+c) == f.Fraction(a, c) and f.Fraction(a, c) < 1]
    fractions_2 = [[10*b+a, 10*c+b]
                   for a in range(1, 10)
                   for b in range(1, 10)
                   for c in range(1, 10)
                   if f.Fraction(10*b+a, 10*c+b) == f.Fraction(a, c) and f.Fraction(a, c) < 1]
    return fractions_1 + fractions_2


def main():
    answer = get_digit_cancelling_fractions()
    fractions = [f.Fraction(a,b) for [a, b] in answer]
    print(f"The Answer to Project Euler 033 is {math.prod(fractions).denominator}")

    # The Answer to Project Euler 033 is 100


if __name__ == "__main__":
    main()
