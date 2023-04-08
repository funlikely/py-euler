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


def precedes(login: str, c: chr, d: chr) -> bool:
    return len([x for i, x in enumerate(login) for j, y in enumerate(login) if i < j and x == c and y == d]) > 0


def follows(login: str, c: chr, d: chr) -> bool:
    return len([x for i, x in enumerate(login) for j, y in enumerate(login) if i > j and x == c and y == d]) > 0


def get_shortest_passcode() -> str:
    data = get_data_from_file()

    print(f"data: {data}")

    char_set = set([c for login in data for c in login])
    print(f"charset: {char_set}")

    before_dict = {d: set([c for login in data for c in login if precedes(login, c, d)]) for d in char_set}
    for d in before_dict:
        print(f"before {d}: {before_dict[d]}")
    after_dict = {d: set([c for login in data for c in login if follows(login, c, d)]) for d in char_set}
    for d in after_dict:
        print(f"after {d}: {after_dict[d]}")

    # try 73162890

    passcode = '73162890'

    failure = False
    for login in data:
        a = login[0]
        b = login[1]
        c = login[2]
        if not precedes(passcode, a, b) or not precedes(passcode, b, c):
            failure = True
    if failure:
        return 'failure'
    else:
        return passcode


def main():
    answer = get_shortest_passcode()
    print(f"The Answer to Project Euler 079 is {answer}")

    # The Answer to Project Euler 079 is 73162890


if __name__ == "__main__":
    main()
