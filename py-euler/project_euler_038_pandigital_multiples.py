"""
    Pandigital multiples

    Problem 38

    Take the number 192 and multiply it by each of 1, 2, and 3:

        192 × 1 = 192
        192 × 2 = 384
        192 × 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
    product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital,
    918273645, which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
    with (1,2, ... , n) where n > 1?

"""


class PandigitalNumbers:

    def __init__(self):
        pass

    def get_pandigital_numbers2(self):
        """
            First solution. before I remembered that one could use str() on an integer.
        :return:
        """
        pandigital_numbers = []

        for i in range(9000, 9999):
            digit_set = set()
            digit_set.add(i % 10)
            digit_set.add(int(i / 10) % 10)
            digit_set.add(int(i / 100) % 10)
            digit_set.add(int(i / 1000) % 10)
            j = 2 * i
            digit_set.add(j % 10)
            digit_set.add(int(j / 10) % 10)
            digit_set.add(int(j / 100) % 10)
            digit_set.add(int(j / 1000) % 10)
            digit_set.add(int(j / 10000) % 10)

            if digit_set == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                pandigital_numbers.append(str(i) + str(2 * i))
        return pandigital_numbers

    def get_pandigital_numbers3(self):
        """
            Second solution. Wiser than the first.
        :return:
        """

        pandigital_numbers = []

        for i in range(2, 9999):
            if i % 5 == 0:
                continue
            mult = 2
            str_accum = str(i)
            while len(str_accum) < 9:
                str_accum += str(i * mult)
                mult += 1
            if sorted(str_accum) == sorted("123456789"):
                pandigital_numbers.append(str_accum)

        return pandigital_numbers


def main():
    p = PandigitalNumbers()
    answer = p.get_pandigital_numbers2()
    print(f"The Answer to Project Euler 038 is {max(answer)}")

    # The Answer to Project Euler 038 is 932718654


if __name__ == "__main__":
    main()
