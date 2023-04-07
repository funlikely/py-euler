"""
    Totient maximum

    Problem 69

    Euler's Totient function, $\phi(n)$ [sometimes called the phi function], is defined as the number of positive
    integers not exceeding $n$ which are relatively prime to $n$. For example, as $1$, $2$, $4$, $5$, $7$, and $8$,
    are all less than or equal to nine and relatively prime to nine, $\phi(9)=6$. $n$ 	Relatively Prime 	$\phi(n)$
    	$n/\phi(n)$ 2 	1 	1 	2 3 	1,2 	2 	1.5 4 	1,3 	2 	2 5 	1,2,3,4 	4 	1.25 6 	1,
    	5 	2 	3 7 	1,2,3,4,5,6 	6 	1.1666... 8 	1,3,5,7 	4 	2 9 	1,2,4,5,7,8 	6 	1.5 10 	1,3,7,
    	9 	4 	2.5

    It can be seen that $n = 6$ produces a maximum $n/\phi(n)$ for $n\leq 10$.

    Find the value of $n\leq 1\,000\,000$ for which $n/\phi(n)$ is a maximum.

    NOTE: phi(n) = n * prod(1 - 1/p) for all p primes dividing n
    E.g., phi(26) = 26 * 1/2 * 12/13 = 12
"""
from utilities.primes import PrimeProcessor
import utilities.divisors as div

pp = PrimeProcessor(1000000)
primes = pp.primes_up_to(1000000)


def totient(n):
    prime_factors = div.prime_factors(n)
    prod = 1
    for p in prime_factors:
        prod *= (1-1/p)
    return n * prod


def get_totient_kind_of_maximum():
    int_max = 1000000

    return 0


def main():
    answer = get_totient_kind_of_maximum()
    print(f"The Answer to Project Euler 069 is {answer}")

    # The Answer to Project Euler 069


if __name__ == "__main__":
    main()
