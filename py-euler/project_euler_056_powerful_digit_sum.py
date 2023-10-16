"""
    Powerful Digit Sum

    Problem 56

    A googol () is a massive number: one followed by one-hundred zeros; is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only

    Considering natural numbers of the form,
    , where , what is the maximum digital sum?
"""


debug = True


def get_answer():
    max_sum = 0

    for a in range(1,100):
        for b in range(1, 100):
            ab_sum = sum([int(c) for c in str(a**b)])
            if ab_sum > max_sum:
                max_sum = ab_sum
                if debug:
                    print(f'new max sum, {a}**{b} = {a**b}, and digit sum = {max_sum}')
    return max_sum


def main():

    answer = get_answer()
    print(f"The Answer to Project Euler 056 is {answer}")

    # The Answer to Project Euler 056


if __name__ == "__main__":
    main()
