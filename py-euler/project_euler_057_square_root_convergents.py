"""
    Square Root Convergents
    Problem 57

    sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))

    Fractions in the partial series are

    3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, ...

    1393/985 is the first example where the number of digits in the numerator exceeds the number of digits in the
    denoninator.

    In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""


debug = True


def get_answer():
    """
    The series is c = 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, ...
    If we let
        c(n) = a(n)/b(n),
    then
        c(n+1) = a(n+1)/b(n+1)
    where
        a(n+1) = a(n) + 2*b(n)
        b(n+1) = a(n) + b(n)

    So the answer will just be a matter of calculating a(i) and b(i) for 1 <= i <= 1000, and comparing the number
    of digits
    """

    counter = 0
    a = 3
    b = 2
    for i in range(1000):
        if len(str(a)) > len(str(b)):
            counter += 1
        a_next = a + 2 * b
        b_next = a + b
        a = a_next
        b = b_next

    return counter


def main():

    answer = get_answer()
    print(f"The Answer to Project Euler 057 is {answer}")

    # The Answer to Project Euler 057 is 153


if __name__ == "__main__":
    main()
