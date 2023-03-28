"""
    Double-base palindromes
    
    Problem 36
    
    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
    
    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
    
    (Please note that the palindromic number, in either base, may not include leading zeros.)


"""


def is_palindrome(param):
    return param == param[::-1]


def binary_str(n):
    result = ""
    while n > 1:
        if n % 2 == 1:
            result = "1" + result
        else:
            result = "0" + result
        n = int(n/2)
    if n % 2 == 1:
        result = "1" + result
    else:
        result = "0" + result
    return result


def get_doubledromes():
    result = []

    for i in range(1000000):
        if is_palindrome(str(i)) and is_palindrome(binary_str(i)):
            result.append(i)

    return result


def main():
    answer = get_doubledromes()
    print(f"The Answer to Project Euler 036 is {sum(answer)}")

    # The Answer to Project Euler 036 is 872187


if __name__ == "__main__":
    main()
