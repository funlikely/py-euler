# Summation of primes
#
# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
from utilities.primes import prime_sieve_up_to


def main():
    num_primes = 2000000
    primes = prime_sieve_up_to(num_primes)
    primes_sum = 0
    for i in range(2, len(primes)):
        if primes[i]:
            primes_sum += i

    print("The sum of the primes less than " + str(num_primes) + " is " + str(primes_sum))


if __name__ == "__main__":
    main()

