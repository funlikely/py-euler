"""
    Coin Partitions


    Problem 78

    Let p(n) represent the number of different ways in which n coins can be separated into piles. For example,
    five coins can be separated into piles in exactly seven different ways, so p(5) = 7

    OOOOO
    OOOO   O
    OOO   OO
    OOO   O   O
    OO   OO   O
    OO   O   O   O
    O   O   O   O   O

    Find the least value of n
    for which p(n) is divisible by one million.

    Let's define p(n) = P(n,n) where P(n,m) is the number of ways to partition n coins using a maximum
    partition size of m.

    Specially define P(n,0) = 1

    Some examples:
    P(n,0) = 1
    P(n,1) = 1

    P(n,m) = sum(P(i, min(i, n-i))) for i from 1 to n

    p(7) = P(7,7)
    =  P(0,0)
     + P(1,1)
     + P(2,2)
     + P(3,3)
     + P(4,3) + P(1,1)
     + P(5,2) + P(3,2) + P(1,1)
     + P(6,1)
     + P(7,0)

    P(4,3)
    =  xxx x, xx xx, xx x x, x x x x
    =  P(1,1)
     + P(4,2)
     + P(4,1)

    P(5,2)
    =  xx xx x, xx x x x, x x x x x
    = P(1,1) + P(3,1) + P(1,1)
"""


def get_answer():
    return 1


def main():
    answer = get_answer()
    print(f"The Answer to Project Euler 078 is {answer}")

    # The Answer to Project Euler 078 is


if __name__ == "__main__":
    main()
