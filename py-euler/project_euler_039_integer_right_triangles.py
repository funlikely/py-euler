"""
    Integer right triangles

    Problem 39

    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
"""


def get_triangles(perimeter):
    triangles = [(b, perimeter - c - b, c) for c in range(1, int(perimeter / 2)) for b in range(1, int(c * 0.75)) if
                 c * c == b * b + (perimeter - c - b) * (perimeter - c - b)]
    return triangles


def get_perimeter_that_maximizes_integer_right_triangles(max_perimeter, debug_and_log):
    max_tri_count = 0
    max_tri_i = 10
    for i in range(10, max_perimeter + 1):
        tri_count = len(get_triangles(i))
        if tri_count > max_tri_count:
            if debug_and_log:
                print(f"i = {i}, triangles = {get_triangles(i)}")
            max_tri_count = tri_count
            max_tri_i = i
        if i % 50 == 0 and debug_and_log:
            print(f"trying round {i}")
    return max_tri_i


def main():
    answer = get_perimeter_that_maximizes_integer_right_triangles(1000, True)
    print(f"The Answer to Project Euler 039 is {answer}")

    # The Answer to Project Euler 039 is 840


if __name__ == "__main__":
    main()
