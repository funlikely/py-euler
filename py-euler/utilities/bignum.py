
class BigNum:

    def __init__(self, value):
        self.value = value

    def add(self, bignum2):
        a = self.value
        b = bignum2.value
        carry = 0
        total = []
        for i in range(min(len(a), len(b))):
            digit_sum = int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry
            if digit_sum > 9:
                carry = 1
                digit_sum -= 10
            else:
                carry = 0
            total.append(str(digit_sum))
        total.reverse()
        return BigNum(''.join(total))
