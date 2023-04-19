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
from ast import literal_eval
from typing import List

debug = True


def debug_and_investigation():
    pass


def triangle_contains_origin(triangle: tuple) -> bool:
    """
        check to see if 2 of the 3 line segments comprising the triangle go above or below the origin,
        and the other line segment goes below or above in opposition


        point slope form, given points (x1, y1) and (x2, y2):

            S(x-x1) = (y-y1) where S = (y2-y1)/(x2-x1)

        then look at x=0 and solve for y:

            y = -x1*(y2-y1)/(x2-x1) + y1

        Check if (y>0) are not all the same, for the three line segments of the triangle
    """
    above_count = 0
    below_count = 0
    combos = [[0, 1], [1, 2], [2, 0]]
    for combo in combos:
        x1 = triangle[combo[0]][0]
        y1 = triangle[combo[0]][1]
        x2 = triangle[combo[1]][0]
        y2 = triangle[combo[1]][1]
        if x2 - x1 == 0:
            """in this house we obey the laws of not dividing by zero!"""
            print(f"we have a vertical side on triangle {triangle}")
            # todo: and this needs to be handled. look for if the vertical side is at x=0, and etc.
            continue
        y = -x1*(y2-y1)/(x2-x1) + y1
        if y == 0:
            return True
        elif y > 0:
            above_count += 1
        else:
            below_count += 1
    return above_count > 0 and below_count > 0


def count_of_triangles_containing_origin(triangles: List[tuple]) -> int:
    count = 0
    for triangle in triangles:
        if triangle_contains_origin(triangle):
            count += 1
    return count


def load_triangles() -> List[tuple]:
    file = open("data/project_euler_102.txt")
    triangle_datum_list = file.readlines()
    triangle_points = [list(map(int,datum.split(','))) for datum in triangle_datum_list]
    triangles = [((r[0], r[1]), (r[2], r[3]), (r[4], r[5])) for r in triangle_points]
    return triangles


def main():
    if debug:
        debug_and_investigation()
    triangles = load_triangles()
    answer = count_of_triangles_containing_origin(triangles)
    print(f"The Answer to Project Euler 112 is {answer}")

    # The Answer to Project Euler 112 is


if __name__ == "__main__":
    main()
