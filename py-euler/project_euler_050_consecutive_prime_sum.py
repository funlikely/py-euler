"""
    Consecutive prime sum

    Problem 50

    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
from utilities.primes import PrimeProcessor


def get_consecutive_prime_sum():
    pp = PrimeProcessor(100000)
    primes = pp.primes_up_to(1000000)
    solution_i = 0
    solution_length = 0
    solution = 0
    print(f"number of primes under 1 million = {len(primes)}")
    for i in range(len(primes)):
        if i % 1000 == 0:
            print(f"i = {i}")
        if i > len(primes) - solution_length:
            continue
        if solution_length * primes[i] > 1000000:
            continue
        for j in range(650):
            if j < solution_length:
                continue
            test = sum(primes[i:j+1])
            if test in primes and j-i+1 > solution_length:
                solution_length = j-i+1
                solution = test
                print(f"current max: {primes[i]} + ... + {primes[j]} = {solution}, (number of terms = {solution_length})")
    return solution


def main():
    answer = get_consecutive_prime_sum()
    print(f"The Answer to Project Euler 050 is {answer}")

    # The Answer to Project Euler 050 is 997651


if __name__ == "__main__":
    main()
