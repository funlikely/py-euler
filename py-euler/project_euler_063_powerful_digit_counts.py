"""
    Powerful Digit Counts
    
    Problem 63
    
    The $5$-digit number, $16807=7^5$, is also a fifth power. Similarly, the $9$-digit number, $134217728=8^9$, is a ninth power.</p>
<p>How many $n$-digit positive integers exist which are also an $n$th power?
"""
import math


def main():
    answer = sum([10 - math.ceil(math.pow(10 ** (n-1), 1.0 / n)) for n in range(1, 22)])
    print(f"The Answer to Project Euler 063 is {answer}")

    # The Answer to Project Euler 063 is 49


if __name__ == "__main__":
    main()
