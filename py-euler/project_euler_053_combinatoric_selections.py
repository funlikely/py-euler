"""
    Combinatoric selections

    Problem 53

    There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    How many, not necessarily distinct, values of
    for n-choose-r, are greater than one-million?
"""


def get_combination_count():
    count = 0
    for i in range(1,101):
        count += 1
    return 0


def main():
    answer = get_combination_count()
    print(f"The Answer to Project Euler 053 is {answer}")

    # The Answer to Project Euler 053 is


if __name__ == "__main__":
    main()
