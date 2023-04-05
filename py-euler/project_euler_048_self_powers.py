"""
    Self powers

    Problem 48

    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
import utilities.bignum as bg


def get_big_prime_digits():
    a = bg.BigNum(1)
    for i in range(2, 200):
        a = bg.BigNum(1)
    return 0


def main():
    answer = get_big_prime_digits()
    print(f"The Answer to Project Euler 048 is {answer}")

    # The Answer to Project Euler 048


if __name__ == "__main__":
    main()
