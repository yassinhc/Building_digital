import numpy as np
from math import atan2

def lowest_coordinate(points):
    """ Returns the anchor point (pt with the lowest coordinates) in a list of points

    Parameters
    ----------
    points : numpy array of 2D
        array of points 

    Returns
    -------
    numpy array of 1D
        anchor point of the list of points (passed in argument)
    """
    anchor_point = points[0]
    for i, point in enumerate(points):
        if point[1] < anchor_point[1]:                                        # find a point with the lowest y-coordinate
            anchor_point = point
        elif point[1] == anchor_point[1] and point[0] < anchor_point[0]:      # if ==, pick the one with the loest x-coordinate
            anchor_point = point
    return anchor_point


def polar_angle(p0, p1):
    """returns the polar angle between 2 points (2 vectors)

    Parameters
    ----------
    p0 : numpy array of 1D 
        1st point
    p1 : numpy array of 1D 
        2nd point

    Returns
    -------
    float : 
        - polar angle between p0, p1 if not horitontal
        - -10. otherwise
    """
    y_span=p0[1]-p1[1]
    x_span=p0[0]-p1[0]
    if round(atan2(y_span,x_span), 2) == 3.14:     # used to fix special case of 2 points that are horizontal
        return -10.  
    return atan2(y_span,x_span)



def sort_angle(points):
    """ Sorts the points based on the angle they make with the x-axis

    Parameters
    ----------
    points : numpy array of 3D
        array of points

    Returns
    -------
    numpy array
        sorted points with respect to the polar angle 
    """
    point_angles = []
    anchor_point = lowest_coordinate(points)
    for i, point in enumerate(points):
        point_angles.append([point[0], point[1], polar_angle(anchor_point, point)])

    point_angles = np.array(point_angles)                            
    point_angles = point_angles[point_angles[:, 2].argsort()]       # sorted list of points with respect to angles

    sorted_points = point_angles[:, (0,1)]                          # sorted list of polar angles

    return sorted_points


def right_turn(a, b, c):
    """ Returns a boolean value that assert if moving from a to c 
        passing by b defines a right turn

    Parameters
    ----------
    a, b, c : 
        numpy arrays of 1D - points

    Returns
    -------
    boolean
        True  : if a, b, c define a right turn
        False : otherwise
    """
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]) <=0
    

def convex_hull(points):
    """ Returns the set of points that define the convex hull of the passed points in argument 

    Parameters
    ----------
    points : numpy array of 2D
        array of points

    Returns
    -------
    numpy array of 2D
        array of points defining the convex hull of points in argument 
    """
    anchor_point = lowest_coordinate(points)         # anchor point
    sorted_points = sort_angle(points)               # sorting points with respect to the polar angle

    
    cv_hull = [anchor_point, sorted_points[0]]       # initial convex_hull 

    for point in sorted_points[1:]:
        while right_turn(cv_hull[-2], cv_hull[-1], point) and len(cv_hull)>2:   # if right_turn --> delete the previous point
            del cv_hull[-1]
        cv_hull.append(point)                        # else --> add the point to convex hull

    return cv_hull


if __name__ == "__main__":

    import random 
    import matplotlib.pyplot as plt
    import numpy as np

    number_points = 20
    points = np.random.randint(1, 100, size = (number_points, 2))
    cv_hull = np.array(convex_hull(points))

    plt.scatter(points[:, 0], points[:, 1])
    plt.plot(cv_hull[:, 0], cv_hull[:, 1], c = "r")
    plt.show()
