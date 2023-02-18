# Quadratic primes
#
# Problem 27
#
# Euler discovered the remarkable quadratic formula:
#   n*n + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values . However, when is divisible
# by 41, and certainly when
#
# is clearly divisible by 41.
#
# The incredible formula
# was discovered, which produces 80 primes for the consecutive values
#
# . The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
# n*n + an + b
# , where abs(a) < 1000 and abs(b) < 1000
#
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
# primes for consecutive values of , starting with n = 0.
#


# 1. get list of first couple thousand primes
#   a. If we can get 500 consecutive primes, that would be at max 500*500 + 500*999 + 999 = 750499
#   b. Let's just say the first 8300 primes. That goes up to about 750,000.
# 2. loop from -1000 to 1000, for both a and b
# 3. test the quadratic values

from utilities.primes import prime_sieve


def prime_generator(n, a, b):
    return n * n + a * n + b


def test_on_original_prime_quadratic(tests_and_logs):
    if not tests_and_logs:
        return

    prime_sieve_027 = prime_sieve(8300)

    print(f"the first and last couple elements of the prime sieve are {prime_sieve_027[:5]} and {prime_sieve_027[-5:]}")

    a = 1
    b = 41
    n = 1
    prime_count = 0
    index = prime_generator(n, a, b)

    while prime_sieve_027[index]:
        prime_count += 1

        if prime_count % 10 == 0:
            print(f"{prime_count}th generated prime is {index}")

        n += 1
        index = prime_generator(n, a, b)

    print(f"The number of consecutive primes generated for a = {a} and b = {b} is {prime_count}")


def get_prime_count_on_quadratic(a, b, prime_sieve):
    n = 1
    prime_count = 0
    index = prime_generator(n, a, b)

    while prime_sieve[index]:
        prime_count += 1

        if prime_count % 10 == 0:
            print(f"{prime_count}th generated prime is {index}")

        n += 1
        index = prime_generator(n, a, b)

    return prime_count


def find_best_prime_quadratic(tests_and_logs):
    prime_sieve_027 = prime_sieve(8300)
    best_a = 1
    best_b = 1
    best_prime_count = 1

    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            prime_count = get_prime_count_on_quadratic(a, b, prime_sieve_027)
            if prime_count > best_prime_count:
                if prime_count > best_prime_count + 30 and tests_and_logs:
                    print(f"latest great updated quadratic, n*n + {a}*n + {b}, with {prime_count} primes")
                best_a = a
                best_b = b
                best_prime_count = prime_count

    return best_a, best_b, best_prime_count


def main():
    tests_and_logs = False

    test_on_original_prime_quadratic(tests_and_logs)
    a, b, prime_count = find_best_prime_quadratic(tests_and_logs)
    print(f"The best quadratic is n*n + {a}*n + {b}, with {prime_count} primes.")
    print(f"The Answer to Euler 027 is a * b = {a * b}.")


if __name__ == "__main__":
    main()