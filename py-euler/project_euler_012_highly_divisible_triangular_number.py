"""
    Highly divisible triangular number

    Problem 12

    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1
    + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

         1: 1
         3: 1,3
         6: 1,2,3,6
        10: 1,2,5,10
        15: 1,3,5,15
        21: 1,3,7,21
        28: 1,2,4,7,14,28

    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
"""

from utilities.primes import PrimeProcessor


def triangle(z):
    return int(z * (z + 1) / 2)


def get_target_triangle_number(debug):
    max_divisor_count = 2
    pp = PrimeProcessor(5000)
    # prime_list = pp.prime_list
    for i in range(12000, 12376):
        current_divisor_count = pp.divisor_counter_fast(triangle(i))
        if current_divisor_count > 500:
            return int(triangle(i))
        if current_divisor_count > max_divisor_count:
            max_divisor_count = current_divisor_count
            if debug:
                print(f'New leader in divisors is triangle({i}) with {max_divisor_count} divisors')
    return 0


def main():
    debug = True
    result = get_target_triangle_number(debug)
    print(f"The Answer to Project Euler 012 is {result}")

    # The Answer to Project Euler 012 is 76576500


if __name__ == "__main__":
    main()
