import math


class BigNum:

    def __init__(self, value):
        self.value = value

    def add(self, bignum2):
        a = self.value
        b = bignum2.value
        carry = 0
        total = []
        max_length = max(len(a), len(b))
        a = a.rjust(max_length, '0')
        b = b.rjust(max_length, '0')
        for i in range(max_length):
            digit_sum = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry
            if digit_sum > 9:
                carry = 1
                digit_sum -= 10
            else:
                carry = 0
            total.append(str(digit_sum))
        if carry == 1:
            total.append(str(carry))
        total.reverse()
        return BigNum(''.join(total))

    def multiply(self, bignum2):
        s = self.value
        t = bignum2.value
        a = []
        for i in range(len(s)):
            a.append(int(s[len(s) - 1 - i]))
        b = []
        for i in range(len(t)):
            b.append(int(t[len(t) - 1 - i]))
        product_list = [0] * (len(a) + len(b))
        for i in range(len(a)):
            for j in range(len(b)):
                product_list[i + j] += a[i] * b[j]
        temp_product = 0
        for i in range(len(product_list)):
            temp_product += int(product_list[i] * math.pow(10, i))
        width = len(product_list) + 1
        sub_product_list = [''] * width
        for i in range(len(product_list)):
            sub_product_list[i] = str(product_list[i]).rjust(width - i, '0').ljust(width, '0')
        result = BigNum(sub_product_list[0])
        for i in range(1, len(sub_product_list) - 1):
            result = result.add(BigNum(sub_product_list[i]))  # add_two_string_ints(result, sub_product_list[i])

        return BigNum(result.value.lstrip('0'))

    def int_divide(self, n: int):
        """
        This is division of a BigNum by an int
        :param n: divisor
        :return: BigNum(self.value / n)

        Oh I am going to need to be able to divide by a BigNum aren't I . . .
        """

        i = 0
        r = 0
        d = 1
        while i < len(self.value):
            if r > n:
                d += int(r / n)
                r = r % n

            i += 1
            d *= 10
            r *= 10
            r += int(self.value[i])

        return BigNum('0')
