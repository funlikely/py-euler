"""
    Problems 1-5

    1
    Sum of all multiples of 3 or 5 below 1000

    2
    Find sum of Fibonacci numbers whose values do not exceed four million and which are even.

    3
    What is the largest prime factor of the number 600851475143?

    4
    Largest palindromic number made from the product of two 3-digit numbers

    5
    What is the smallest positive number that is evenly divisible by all the numbers from 1-20
"""
from utilities.divisors import get_divisors


def get_answers():
    answers = [sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])]
    fib1 = fib2 = 1
    a2 = 0
    while fib1 < 4 * 10 ** 6:
        if fib1 % 2 == 0:
            a2 += fib1
        new_fib = fib1 + fib2
        fib2 = fib1
        fib1 = new_fib
    answers.append(a2)

    n = 600851475143
    i = 2
    a3 = 2
    while i <= n:
        if n % i == 0:
            n = n / i
            if i > a3:
                a3 = i
        i += 1

    answers.append(a3)
    answers.append(max([a * b for a in range(1000) for b in range(1000) if a != b and str(a*b) == str(a*b)[::-1]]))
    answers.append(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)
    return answers


def main():
    answer = get_answers()
    print(f"The Answers to Project Euler 001-005 are {answer}")

    # The Answers to Project Euler 001-005 are


if __name__ == "__main__":
    main()
