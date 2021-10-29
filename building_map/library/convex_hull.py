import numpy as np
from math import atan2


def lowest_coordinate(points):
    # find a point with lowest y-coordinate
    # if there is 2, pick the one with lowest x-coordinate
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


def right_turn(a, b, c):
    # returns if moving from a to c passing by b defines a right turn
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]) <=0
    

def convex_hull(points):
    #1 : sorting the points with respect of their angle with the x-axis
    anchor_point = lowest_coordinate(points)
    sorted_points = sort_angle(points)

    # initializing the convex hull with the anchor_point and the first point in the sorted list 
    # of points with respect to angles 
    cv_hull = [anchor_point, sorted_points[0]]  

    for point in sorted_points[1:]:
        # if right turn --> delete the previous point
        while right_turn(cv_hull[-2], cv_hull[-1], point):
            del cv_hull[-1]
        cv_hull.append(point)

    return cv_hull



import random 
import matplotlib.pyplot as plt


number_points = 50
points = np.random.randint(1, 100, size = (number_points, 2))
cv_hull = np.array(convex_hull(points))

plt.scatter(points[:, 0], points[:, 1])
plt.plot(cv_hull[:, 0], cv_hull[:, 1], c = "r")
plt.show()
