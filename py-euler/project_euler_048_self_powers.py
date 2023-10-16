"""
    Self powers

    Problem 48

    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

def get_big_prime_digits():
    sequence = [0] * 1001
    for i in range(1, 1001):
        accumulator = 1
        for j in range(1, i+1):
            accumulator *= i
            accumulator %= 10**11
        sequence[i] = accumulator
    answer = str(sum(sequence))[-10:]
    return answer


def main():
    answer = get_big_prime_digits()
    print(f"The Answer to Project Euler 048 is {answer}")

    # The Answer to Project Euler 048 is 9110846700


if __name__ == "__main__":
    main()
