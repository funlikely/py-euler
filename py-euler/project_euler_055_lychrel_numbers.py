"""
    Lychrel Numbers

    Problem 55
    
    If we take $47$, reverse and add, $47 + 74 = 121$, which is palindromic.
    Not all numbers produce palindromes so quickly. For example,
    \begin{align}
    349 + 943 &amp;= 1292\\
    1292 + 2921 &amp;= 4213\\
    4213 + 3124 &amp;= 7337

    That is, $349$ took three iterations to arrive at a palindrome. Although no one has proved it yet, it is thought
    that some numbers, like $196$, never produce a palindrome. A number that never forms a palindrome through the
    reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the
    purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are
    given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty
    iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a
    palindrome. In fact, $10677$ is the first number to be shown to require over fifty iterations before producing a
    palindrome: $4668731596684224866951378664$ ($53$ iterations, $28$-digits). Surprisingly, there are palindromic
    numbers that are themselves Lychrel numbers; the first example is $4994$. How many Lychrel numbers are there
    below ten-thousand? <p class="smaller">NOTE: Wording was modified slightly on 24 April 2007 to emphasise the
    theoretical nature of Lychrel numbers.
"""


debug = True


def is_lychrel(n):
    tries = 50
    while tries > 0:
        n = n + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
        tries -= 1
    return True


def is_lychrel_using_accumulator(n):
    return len([n := n + int(str(n)[::-1]) for i in range(50) if str(n := n + int(str(n)[::-1])) == str(n)[::-1]]) == 0


def get_answer():
    return sum([1 for i in range(10000) if is_lychrel(i)])


def get_answer_using_accumulator():
    return sum([1 for i in range(10000) if is_lychrel_using_accumulator(i)])


def main():

    answer = get_answer_using_accumulator()
    print(f"The Answer to Project Euler 055 is {answer}")

    # The Answer to Project Euler 055 is 249


if __name__ == "__main__":
    main()
