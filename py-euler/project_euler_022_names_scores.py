"""
    Names scores

    Problem 22

    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first
    names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
    is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
"""

file = open("data/project_euler_022.txt")
name_list = [name.strip('"') for name in file.readline().split(',')]
name_list.sort()

print(name_list)


def get_score_list():
    score_list = []
    for i in range(len(name_list)):
        letter_sum = 0
        for j in range(len(name_list[i])):
            letter_sum += ord(name_list[i][j]) - 64
        score_list.append(letter_sum * (i + 1))
    return score_list


def main():
    score_list = get_score_list()
    print(f"The Answer to Project Euler 022 is {sum(score_list)}")

    # The Answer to Project Euler 022 is 871198282


if __name__ == "__main__":
    main()
