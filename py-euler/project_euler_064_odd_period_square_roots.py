"""
    Odd Period Square Roots

    Problem 64
    
    All square roots are periodic when written as continued fractions and can be written in the form:

    $\displaystyle \quad \quad \sqrt{N}=a_0+\frac 1 {a_1+\frac 1 {a_2+ \frac 1 {a3+ \dots}}}$

    The first ten continued fraction representations of (irrational) square roots are:
    
    $\quad \quad \sqrt{2}=[1;(2)]$, period=$1$
    $\quad \quad \sqrt{3}=[1;(1,2)]$, period=$2$
    $\quad \quad \sqrt{5}=[2;(4)]$, period=$1$
    $\quad \quad \sqrt{6}=[2;(2,4)]$, period=$2$
    $\quad \quad \sqrt{7}=[2;(1,1,1,4)]$, period=$4$
    $\quad \quad \sqrt{8}=[2;(1,4)]$, period=$2$
    $\quad \quad \sqrt{10}=[3;(6)]$, period=$1$
    $\quad \quad \sqrt{11}=[3;(3,6)]$, period=$2$
    $\quad \quad \sqrt{12}=[3;(2,6)]$, period=$2$
    $\quad \quad \sqrt{13}=[3;(1,1,1,1,6)]$, period=$5$
    
    Exactly four continued fractions, for $N \le 13$, have an odd period.
    How many continued fractions for $N \le 10\,000$ have an odd period?
"""
import math


debug = True


def get_period(cf):
    if cf[-1] != 2 * cf[0]:
        return None
    for i in range(1, int(len(cf)/2)+1):
        if cf[-i:(len(cf))] == cf[(-2*i):(-i)]:
            return i
    return None


def get_continued_fraction_for_sqrt(n):
    a = math.floor(math.sqrt(n))
    b = a
    d = 1
    cf = []
    # let's process d / (sqrt(n) - b)
    # d / (sqrt(n) - b) = (sqrt(n) + b) / d'                    where d' = (n - b^2) / d
    #                   = a' + (sqrt(n) + b - a' * d') / d'     where a' = floor((sqrt(n) + b) / d')
    #                   = a' + (sqrt(n) - b') / d'              where b' = a' * d' - b
    # and then you can process d' / (sqrt(n) - b') to get the next values for a, b, d

    for i in range(1000):
        print(f'a={a},b={b},d={d}')
        cf.append(a)

        period = get_period(cf)
        if period is not None:
            return cf[:-period]

        d = (n - b * b) / d
        a = math.floor((math.sqrt(n) + b) / d)
        b = a * d - b
    return None


def get_answer():
    results = []
    cf_dict = {}
    for i in range(2, 10001):
        if int(math.sqrt(i)) ** 2 == i:
            continue
        else:
            cf = get_continued_fraction_for_sqrt(i)
            cf_dict[i] = cf
    counter = 0
    for i in cf_dict:
        if len(cf_dict[i]) % 2 == 0:
            counter += 1
    for i in cf_dict:
        print(f'{i}: {cf_dict[i]}')
    return counter


def investigate():
    n = 23
    a = math.floor(math.sqrt(n))
    b = a
    d = 1
    cf = []
    # let's process d / (sqrt(n) - b)
    # d / (sqrt(n) - b) = (sqrt(n) + b) / d'                    where d' = (n - b^2) / d
    #                   = a' + (sqrt(n) + b - a' * d') / d'     where a' = floor((sqrt(n) + b) / d')
    #                   = a' + (sqrt(n) - b') / d'              where b' = a' * d' - b
    # and then you can process d' / (sqrt(n) - b') to get the next values for a, b, d

    for i in range(10):
        print(f'a={a},b={b},d={d}')
        cf.append(a)
        d = (n - b * b) / d
        a = math.floor((math.sqrt(n) + b) / d)
        b = a * d - b


def main():
    # if debug:
    #     investigate()

    answer = get_answer()
    print(f"The Answer to Project Euler 064 is {answer}")

    # The Answer to Project Euler 064 is 1322


if __name__ == "__main__":
    main()
