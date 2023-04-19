"""
    Triangle containment
    
    Problem 102
    
    Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a 
    triangle is formed.
    
    Consider the following two triangles:
    
    A(-340,495), B(-153,-910), C(835,-947)
    
    X(-175,41), Y(-421,-714), Z(574,-645)
    
    It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
    
    Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of 
    one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
    
    NOTE: The first two examples in the file represent the triangles in the example given above.
"""
import math
from typing import List

debug = True


def debug_and_investigation():
    pass


def count_of_triangles_containing_origin(triangles: List) -> int:
    return 0


def load_triangles() -> List:
    file = open("data/project_euler_102.txt")
    return []


def main():
    if debug:
        debug_and_investigation()
    triangles = load_triangles()
    answer = count_of_triangles_containing_origin(triangles)
    print(f"The Answer to Project Euler 112 is {answer}")

    # The Answer to Project Euler 112 is


if __name__ == "__main__":
    main()
