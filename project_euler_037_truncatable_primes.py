"""
    Truncatable primes
    
    Problem 37
    
    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
    
    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""


def get_truncatable_primes():
    truncatable_primes = [3797, 797, 97, 7]

    return truncatable_primes

def main():
    answer = get_truncatable_primes()
    print(f"The Answer to Project Euler 037 is {sum(answer)}")

    # The Answer to Project Euler 037 


if __name__ == "__main__":
    main()
