"""
    Sum square difference

    Problem 6

    The sum of the squares of the first ten natural numbers is,

    The square of the sum of the first ten natural numbers is,

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the
    sum.
"""


def get_square_sum_difference():
    sum_of_square = 0
    our_sum = 0
    for i in range(1, 101):
        sum_of_square += i * i
        our_sum += i
    print(our_sum * our_sum - sum_of_square)
    return our_sum * our_sum - sum_of_square


def main():
    answer = get_square_sum_difference()
    print(f"The Answer to Project Euler 006 is {answer}")

    # The Answer to Project Euler 006 is 25164150


if __name__ == "__main__":
    main()
