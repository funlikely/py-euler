# 10001st prime
#
# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from utilities.primes import prime_sieve


def main():
    prime_ordinal_we_want = 10001
    primes = prime_sieve(prime_ordinal_we_want)
    primes_ordinal = 1
    for i in range(2, len(primes)):
        if primes[i]:
            if primes_ordinal < 10 or primes_ordinal > prime_ordinal_we_want - 100:
                print('#' + str(primes_ordinal) + ' = ' + str(i))
                if prime_ordinal_we_want == primes_ordinal:
                    answer = i
            primes_ordinal += 1
    print(f"Answer to Project Euler 007 is {answer}")


if __name__ == "__main__":
    main()

