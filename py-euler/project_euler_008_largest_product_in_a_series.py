"""
    Largest product in a series

    Problem 8

    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

    73167176531330624919225119674426574742355349194934
     ... see project_euler_008.txt
    71636269561882670428252483600823257530420752963450

    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of
    this product?
"""


def read_input_file():
    file = open("data/project_euler_008.txt")
    lines = [line[:-1] for line in file]
    return lines


def get_product(sequence, start, length):
    product = 1
    for j in range(0, length):
        product *= int(sequence[start + j])
    return product


def get_string_describing_product(sequence, start, length):
    result = ''
    for j in range(0, length):
        result += sequence[start + j] + '*'
    return result[:-1]


def get_greatest_product():
    lines = read_input_file()
    sequence_of_digits = ''.join(lines)
    len_of_product = 13  # constant
    len_of_sequence_of_digits = len(sequence_of_digits)

    print('the digits list has ' + str(len_of_sequence_of_digits) + ' digits in it.')

    product_of_digits = [0] * (len(sequence_of_digits) - (len_of_product - 1))
    string_of_digits = [''] * (len(sequence_of_digits) - (len_of_product - 1))
    current_max = 0

    for i in range(0, len(sequence_of_digits) - (len_of_product - 1)):
        product_of_digits[i] = get_product(sequence_of_digits, i, len_of_product)
        string_of_digits[i] = get_string_describing_product(sequence_of_digits, i, len_of_product)
        if product_of_digits[i] > current_max:
            print("your current maximum is the " + str(i) + "th product, which is  is " + str(
                product_of_digits[i]) + " = " + str(string_of_digits[i]))
            current_max = product_of_digits[i]
    return current_max


def main():
    answer = get_greatest_product()
    print(f"The Answer to Project Euler 008 is {answer}")

    # The Answer to Project Euler 008 is 23514624000


if __name__ == "__main__":
    main()
