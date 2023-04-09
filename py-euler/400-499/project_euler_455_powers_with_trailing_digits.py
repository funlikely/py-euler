"""
    Powers With Trailing Digits

    Problem 455

    Let f(n) be the largest positive integer x less than 10**9 such that the last 9 digits of n**x form the number x
    (including leading zeros), or zero if no such integer exists.

    For example:

        f(4) = 411728896 (4**411728896 = ...490411728896)
        f(10) = 0
        f(157) = 743757 (157**743757 = ...567000743757)
        ∑f(n), 2 ≤ n ≤ 10**3 = 442530011399

    Find ∑f(n), 2 ≤ n ≤ 10**6.
"""

digits_to_care_for = 6


def f(n: int) -> int:
    power = n
    trailing_digits = f'{power % 10 ** digits_to_care_for:0{digits_to_care_for}}'
    trailing_digits_list = [trailing_digits]
    length_of_cycle = 10 ** digits_to_care_for
    length_up_to_cycle = 10 ** digits_to_care_for
    for i in range(100000):
        power *= n
        power %= 10 ** digits_to_care_for

        trailing_digits = f'{power % 10 ** digits_to_care_for:0{digits_to_care_for}}'
        if trailing_digits not in trailing_digits_list:
            trailing_digits_list.append(trailing_digits)
        else:
            trailing_digits_list.append(trailing_digits)
            first_repeat_index = [i for i, e in enumerate(trailing_digits_list) if e == trailing_digits_list[-1:][0]][0]
            length_of_cycle = len(trailing_digits_list) - 1 - first_repeat_index
            length_up_to_cycle = first_repeat_index + 1
            break

        # print(trailing_digits)

    display_trailing_digits_list = []
    if len(trailing_digits_list) < 100:
        display_trailing_digits_list = trailing_digits_list
    else:
        display_trailing_digits_list = (trailing_digits_list[:50] + ['...'] + trailing_digits_list[-50:])
    print(
        f'f({n}) cycle, {length_up_to_cycle} singles and then {length_of_cycle}-long cycle: {display_trailing_digits_list}')
    return 0


def get_sum_of_powers() -> int:
    for i in range(2, 81):
        f(i)
    return 0


def main():
    answer = get_sum_of_powers()
    print(f"The Answer to Project Euler 455 is {answer}")

    # The Answer to Project Euler 455


if __name__ == "__main__":
    main()
