import numpy as np
from math import atan2

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def lowest_coordinate(points):
    # find a point with lowest y-coordinate
    # # # if there is 2, pick the one with lowest x-coordinate
    anchor_point = points[0]
    for i, point in enumerate(points):
        if point[1] < anchor_point[1]:
            anchor_point = point
        elif point[1] == anchor_point[1] and point[0] < anchor_point[0]:
            anchor_point = point
    return anchor_point

def polar_angle(p0, p1):
    y_span=p0[1]-p1[1]
    x_span=p0[0]-p1[0]
    return atan2(y_span,x_span)

def sort_angle(points):
    # sorting the points based on the angle they make with the x-axis
    # we will use a heap sort 
    point_angles = []
    anchor_point = lowest_coordinate(points)
    for i, point in enumerate(points):
        point_angles.append([point[0], point[1], polar_angle(anchor_point, point)])


    point_angles = np.array(point_angles)    
    point_angles = point_angles[point_angles[:, 2].argsort()]

    sorted_points = point_angles[:, (0,1)]

    return sorted_points

    
def convex_hull(points):
    """Computes the convex hull of a set of 2D points.
    """
    # sorting the points based on the angle they make with the x-axis
    points = sort_angle(points)

    # Base case: no points or a single point, possibly repeated multiple times.
    if len(points) <= 1:
        return points

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.


    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    result = np.array(lower[:-1] + upper[:-1])
    result = sort_angle(result)
    result = np.append(result, [result[0]], axis = 0)
    return result


if __name__ == "__main__":

    import random 
    import matplotlib.pyplot as plt
    import numpy as np

    number_points = 10
    points = np.random.randint(1, 100, size = (number_points, 2))
    cv_hull = convex_hull(points)
    print(type(cv_hull))

    plt.scatter(points[:, 0], points[:, 1])
    plt.plot(cv_hull[:, 0], cv_hull[:, 1], c = "r")
    plt.show()
