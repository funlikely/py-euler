"""
    Coded triangle numbers

    Problem 42

    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""


def read_input_file():
    file = open("data/project_euler_042.txt")
    word_list = [word.strip('"') for word in file.readline().split(',')]
    return word_list


def is_triangle(word):
    triangle_numbers_list = [int(n * (n+1) / 2) for n in range(200)]
    return sum([ord(i.upper()) - 64 for i in word]) in triangle_numbers_list


def get_triangle_word_count():
    word_list = read_input_file()

    return sum([1 for x in word_list if is_triangle(x)])


def main():
    answer = get_triangle_word_count()
    print(f"The Answer to Project Euler 042 is {answer}")

    # The Answer to Project Euler 042 is 162


if __name__ == "__main__":
    main()
