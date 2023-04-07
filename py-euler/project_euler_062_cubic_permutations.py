"""
    Cubic permutations
    
    Problem 62
    
    The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). In
    fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
    
    Find the smallest cube for which exactly five permutations of its digits are cube.
"""
import math


def find_smallest_special_cube(specialness):
    mag = 2
    max_mag = 30
    # cubes = [n**3 for n in range(10**max_mag)]
    while mag < max_mag:
        sub_cubes = [i**3 for i in range(int(math.pow(10**mag, 1/3)+1), int(math.pow(10**(mag+1), 1/3)+1))]
        print(f"checking from {sub_cubes[0]} to {sub_cubes[-1:][0]}")
        pizza = {}
        for sub_cube in sub_cubes:
            sub_cube_string = ''.join(sorted(str(sub_cube)))
            if sub_cube_string not in pizza:
                pizza[sub_cube_string] = 1
            else:
                pizza[sub_cube_string] += 1
        found_results = [val for i, val in enumerate(pizza.values()) if val >= specialness]
        if len(found_results) > 0:
            found_cubes = [sub_cube for sub_cube in sub_cubes if pizza[''.join(sorted(str(sub_cube)))] >= specialness]
            print(f"found cubes: {found_cubes}")
            return min(sorted(found_cubes))
        mag += 1
    print(f"failed to find cubes : (")
    return -1


def main():
    answer = find_smallest_special_cube(5)
    print(f"The Answer to Project Euler 062 is {answer}")

    # The Answer to Project Euler 062 is 127035954683


if __name__ == "__main__":
    main()
