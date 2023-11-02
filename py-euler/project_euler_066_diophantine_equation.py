"""
    Diophantine Equation

    Problem 66

    Consider quadratic Diophantine equations of the form:

    x^2 - D*y^2 = 1

    <p>For example, when $D=13$, the minimal solution in $x$ is $649^2 - 13 \times 180^2 = 1$.</p>
    <p>It can be assumed that there are no solutions in positive integers when $D$ is square.</p>
    <p>By finding minimal solutions in $x$ for $D = \{2, 3, 5, 6, 7\}$, we obtain the following:</p>
    \begin{align}
    3^2 - 2 \times 2^2 &amp;= 1\\
    2^2 - 3 \times 1^2 &amp;= 1\\
    {\color{red}{\mathbf 9}}^2 - 5 \times 4^2 &amp;= 1\\
    5^2 - 6 \times 2^2 &amp;= 1\\
    8^2 - 7 \times 3^2 &amp;= 1
    \end{align}

    Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained
"""
import math
import time
from utilities.continued_fractions import get_convergent_using_formula, get_continued_fraction_for_sqrt


debug = True


def get_minimal_x_value_in_diophantine_equation_solutions(d):
    x = 2
    while x < 10**9:
        if is_square((x*x - 1)/d):
            return x
        x += 1
    if debug:
        print(f'X Finder Failed on d={d}')
    return -1


def get_answer():
    exes = [0 for i in range(1001)]

    squares = [i*i for i in range(32)]

    start_time = time.time()

    for i in range(1001):
        if i in squares:
            continue
        exes[i] = get_minimal_x_value_in_diophantine_equation_solutions(i)
        if time.time() - start_time > 3 and debug:
            print(f'last exes computed: exes[{i-3}] - exes[{i}] = {exes[(i-3):i+1]}')
            start_time = time.time()

    if debug:
        print(f'collection of exes: {exes}')

    return max([i for i in range(len(exes)) if exes[i] == max(exes)])


def is_square(i):
    return math.sqrt(i) % 1 == 0


def investigate():
    """
    Some notes:

        Collection of exes from previous run, contained in data/project_euler_data_066.txt
        X Finder Failed on d=463
        X Finder Failed on d=617
        X Finder Failed on d=691
        X Finder Failed on d=778
        X Finder Failed on d=797
        X Finder Failed on d=835
        X Finder Failed on d=857
        X Finder Failed on d=883
        X Finder Failed on d=921
        X Finder Failed on d=949
        X Finder Failed on d=967
        X Finder Failed on d=971
        The Answer to Project Euler 066 is 796
        but that's only because it was so close to 10**9 without going over (x = 994933333)

        The current plan is to use a Pell's Equation solving algorithm, and then probably just
        validate that some of the values are the same as the ones from data/project_euler_data_066.txt

        The Pell's Equation solving algorithm should be able to run quickly.

        Algorithm overview:
            1. Generate continued fraction for each sqrt(D) for 2 < D <= 1000 (D not square)
            2. If the CF has an even period, use the convergent up to the first period
               If the CF has an odd period, use the convergent up to the second period
            3. Observe/test that the convergent p/q can be used as a solution to the Pell's equation
               I don't remember if it was x = p+sqrt(D)*q or if it was x=p and y=q
               But we can probably find that pretty easily, either checking online or testing for
                small values of D like 2,3,5,6
    """

    count = 200

    cfs = [get_continued_fraction_for_sqrt(i) for i in range(count)]

    convergents = [0 for i in range(count)]

    for i in range(2, count):
        if is_square(i):
            continue
        print(f'cf for root({i}) = {cfs[i]}')
        if len(cfs[i][1:]) % 2 != 0:
            solution_cf = cfs[i][:-1] + cfs[i][:-1]
        else:
            solution_cf = cfs[i][:-1]
        p, q = get_convergent_using_formula(solution_cf, len(solution_cf))
        convergents[i] = (p, q)
        print(f'continued fraction that will give the solution to the diophantine equation: {solution_cf}')
        print(f'convergents for root({i}): {convergents[i]}')
        x = convergents[i][0][-1]
        y = convergents[i][1][-1]
        print(f'({x})**2 - {i}*({y})**2 = {x**2-i*y**2}')

    return 0


def main():
    if debug:
        investigate()

    answer = get_answer()
    print(f"The Answer to Project Euler 066 is {answer}")

    # The Answer to Project Euler 066 is


if __name__ == "__main__":
    main()
