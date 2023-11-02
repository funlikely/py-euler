# continued fractions utilities
import math


def get_convergent_using_formula(cf, n):
    """
    Hardy number theory textbook Theorem 149

    If p(n) and q(n) are defined by
    p(0) = a(0), p(1) - a(1)*a(0) + 1, p(n) = a(n)*p(n-1) + p(n-2)
    q(0) = 1, q(1) = a(1), q(n) = a(n)*q(n-1)+q(n-2)
    then
    [a(0), a(1), ..., a(n)] = p(n)/q(n)

    :param cf:
    :param limit:
    :return:
    """
    p = [cf[0], cf[0] * cf[1] + 1]
    q = [1, cf[1]]
    for i in range(2, n):
        p.append(cf[i] * p[i - 1] + p[i - 2])
        q.append(cf[i] * q[i - 1] + q[i - 2])

    return p, q


def get_period(cf):
    if cf[-1] != 2 * cf[0]:
        return None
    for i in range(1, int(len(cf) / 2) + 1):
        if cf[-i:(len(cf))] == cf[(-2 * i):(-i)]:
            return i
    return None


def get_continued_fraction_for_sqrt(n):
    debug = False

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
        if debug:
            print(f'a={a},b={b},d={d}')
        cf.append(a)

        period = get_period(cf)
        if period is not None:
            return cf[:-period]

        d = (n - b * b) / d
        a = math.floor((math.sqrt(n) + b) / d)
        b = a * d - b
    return None
