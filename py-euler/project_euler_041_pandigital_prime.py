"""
    Pandigital prime
    
    Problem 41
    
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
    
    What is the largest n-digit pandigital prime that exists?
"""
import utilities.primes as pr


def is_pandigital(counter):
    return sorted(str(counter)) == sorted([str(i+1) for i in range(len(str(counter)))])


def get_largest_n_digit_pandigital_prime(size):
    """
    One shortcut is to realize is that any 9 digit or 8 digit pandigital number will be divisible by 3.
    The greatest n-digit pandigital prime will have n < 8.
    :return:
    """
    if size > 7:
        size = 7
    max_num = int(''.join([str(i) for i in range(size, 0, -1)]))
    pp = pr.PrimeProcessor(max_num + 1)
    counter = len(pp.prime_sieve)

    while counter > 0:
        if counter % 2 == 1 and is_pandigital(counter) and pp.prime_sieve[counter]:
            break
        counter -= 1
    return counter


def main():
    answer = get_largest_n_digit_pandigital_prime(9)
    print(f"The Answer to Project Euler 041 is {answer}")

    # musing: could use Euler 024 lexicographical permutations to speed the runtime of this program

    # The Answer to Project Euler 041 is 7652413


if __name__ == "__main__":
    main()
