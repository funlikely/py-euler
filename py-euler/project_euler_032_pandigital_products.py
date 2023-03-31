"""
Pandigital products

Problem 32

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
    the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
    through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Notes

    13*24 = 312
    97*86 = 8342
    99*99 = 9801
    145*23 = 3335
    96*875 = 84000
    100*100 = 10000
    It looks like we NEED (2-digit)*(3-digit)=(4-digit)
"""


def get_pandigital_products():
    products = {0}
    count = 0
    for a in range(1, 10):
        for b in range(1, 10):
            if b == a:
                continue
            for c in range(1, 10):
                if c == a or c == b:
                    continue
                for d in range(1, 10):
                    if d == a or d == b or d == c:
                        continue
                    for e in range(1, 10):
                        if e == a or e == b or e == c or e == d:
                            continue
                        ab = 10*a+b
                        cde = 100*c+10*d+e
                        product = ab * cde
                        if product < 1000 or product > 9999:
                            continue
                        f = int(product/1000)
                        g = int((product % 1000)/100)
                        h = int((product % 100)/10)
                        i = product % 10
                        if {a, b, c, d, e, f, g, h, i} == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                            count += 1
                            products.add(product)
                            print(f"count={count}, {ab} * {cde} = {product}")
    for a in range(1, 10):
        for b in range(1, 10):
            if b == a:
                continue
            for c in range(1, 10):
                if c == a or c == b:
                    continue
                for d in range(1, 10):
                    if d == a or d == b or d == c:
                        continue
                    for e in range(1, 10):
                        if e == a or e == b or e == c or e == d:
                            continue
                        bcde = 1000*b+100*c+10*d+e
                        product = a * bcde
                        if product < 1000 or product > 9999:
                            continue
                        f = int(product/1000)
                        g = int((product % 1000)/100)
                        h = int((product % 100)/10)
                        i = product % 10
                        if {a, b, c, d, e, f, g, h, i} == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                            count += 1
                            products.add(product)
                            print(f"count={count}, {a} * {bcde} = {product}")
    print(f"products set = {products}")
    return products


def main():
    answer = get_pandigital_products()
    print(f"The Answer to Project Euler 032 is {sum(answer)}")

    # The Answer to Project Euler 032 is 45228


if __name__ == "__main__":
    main()
