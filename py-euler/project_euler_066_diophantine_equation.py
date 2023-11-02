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

debug = True


def get_minimal_x_value_in_diophantine_equation_solutions(d):
    x = 2
    while x < 10**9:
        if math.sqrt((x*x - 1)/d) % 1 == 0.0:
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


def investigate():
    return 0


def main():
    if debug:
        investigate()

    answer = get_answer()
    print(f"The Answer to Project Euler 066 is {answer}")

    # The Answer to Project Euler 066 is


if __name__ == "__main__":
    main()
