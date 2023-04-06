"""
    Combinatoric selections

    Problem 53

    There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    How many, not necessarily distinct, values of
    for n-choose-r, are greater than one-million?
"""
from math import factorial as f


def get_combination_count():
    count = 0
    for i in range(1, 101):
        for j in range (1, i):
            if f(i)/(f(j)*f(i-j)) > 10**6:
                count += 1
    return count


def main():
    answer = get_combination_count()
    print(f"The Answer to Project Euler 053 is {answer}")

    # The Answer to Project Euler 053 is 4075


if __name__ == "__main__":
    main()
