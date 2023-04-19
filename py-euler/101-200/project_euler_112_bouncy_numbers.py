"""
    Bouncy numbers

    Problem 112

    Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
    for example, 134468.

    Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

    We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

    Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below
    one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches
    50% is 538.

    Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy
    numbers is equal to 90%.

    Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
import math

debug = False


def least_number_for_which_the_proportion_of_bouncy_numbers_is(perc: float) -> int:
    lim = 3*10**6
    b_count = 0
    for i in range(1, lim):
        if is_bouncy(i):
            b_count += 1
        propo = b_count / i
        if i % 400000 == 0 and debug:
            print(f"i: {i}, proportion: {round(propo, 5)}")
        if propo == 0.99:
            if debug:
                print(f"i: {i}, proportion: {propo}")
            return i
    return 0


def is_bouncy(k: int) -> bool:
    if k < 100:
        return False
    up = 0
    down = 0
    k_str = str(k)
    for i in range(len(k_str) - 1):
        if k_str[i+1] > k_str[i]:
            up += 1
            if down > 0:
                return True
        elif k_str[i+1] < k_str[i]:
            down += 1
            if up > 0:
                return True
    return (up != 0) and (down != 0)


def debug_and_investigation():
    lim = 10**3

    bounce_tracker = [False] * lim
    for i in range(lim):
        bounce_tracker[i] = is_bouncy(i)
    for i in range(99, 999, 45):
        print(f"{i} bouncy: {bounce_tracker[i]}")


def main():
    if debug:
        debug_and_investigation()
    answer = least_number_for_which_the_proportion_of_bouncy_numbers_is(0.99)
    print(f"The Answer to Project Euler 112 is {answer}")

    # The Answer to Project Euler 112 is


if __name__ == "__main__":
    main()
