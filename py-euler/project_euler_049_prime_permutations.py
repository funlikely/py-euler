"""
    Prime permutations

    Problem 49

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?

"""
from utilities.primes import PrimeProcessor


def get_prime_permutation_solution():
    pp = PrimeProcessor(9999)
    prime_sieve = pp.prime_sieve
    primes = [p for p in pp.primes_up_to(9999) if 9999 > p > 1488]
    diff = 2
    solutions = [(p, p+d, p+2*d)
                 for p in primes
                 for d in range(2, 4500, 2)
                 if ((p+d) in primes) and ((p+2*d) in primes) and set(str(p)) == set(str(p+d)) and set(str(p)) == set(str(p+2*d))]
    solution = solutions[0]
    return str(solution[0]) + str(solution[1]) + str(solution[2])


def main():
    answer = get_prime_permutation_solution()
    print(f"The Answer to Project Euler 049 is {answer}")

    # The Answer to Project Euler 049 is 296962999629


if __name__ == "__main__":
    main()
