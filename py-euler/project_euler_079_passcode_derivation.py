"""
    Passcode derivation
    
    Problem 79
    
    A common security method used for online banking is to ask the user for three random characters from a passcode. For 
    example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 
    317.
    
    The text file, keylog.txt, contains fifty successful login attempts.
    
    Given that the three characters are always asked for in order, analyse the file so as to determine the shortest 
    possible secret passcode of unknown length.

"""
from typing import List


def get_data_from_file() -> List[str]:
    file = open('data/project_euler_079.txt')
    return [x.strip('\n') for x in file.readlines()]


def get_shortest_passcode() -> str:
    data = get_data_from_file()

    print(f"data: {data}")

    char_set = set([c for substring in data for c in substring])
    print(f"charset: {char_set}")
    return ''


def main():
    answer = get_shortest_passcode()
    print(f"The Answer to Project Euler 079 is {answer}")

    # The Answer to Project Euler 079 is


if __name__ == "__main__":
    main()
