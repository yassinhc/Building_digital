import unittest
import numpy as np
import math

import sys
sys.path.append('..')


import library.convex_hull as convex_hull



class Test_Convex_Hull(unittest.TestCase):

    def test_anchor_point(self):
        """ Tests if lowest_coordinate() returns the right anchor point
        """
        nb_points = 5
        points = np.array([[1, 2], [2, 1], [3, 7], [7, 2]])      # example of points

        anchor_point = convex_hull.lowest_coordinate(points)     # anchor point
        right_anchor_point = [2, 1]                              # the right anchor points

        self.assertTrue((anchor_point == right_anchor_point).all())


    def test_polar_angle_normal_case(self):
        """ Tests the polar angle between 2 points (vectors) in normal case (non-horizontal)
        """
        point1 = np.array([1, 1])
        point2 = np.array([2, 2])
        pol_angle =  convex_hull.polar_angle(point2, point1)

        self.assertEqual(round(math.tan(pol_angle)), 1)


    def test_polar_angle_special_case(self):
        """ Tests the polar angle between 2 points (vectors) in special case of horizontal vectors
        """

        point1 = np.array([2, 1])
        point2 = np.array([1, 1])
        pol_angle = convex_hull.polar_angle(point2, point1)

        self.assertEqual(pol_angle, -10.)


    def test_sort_angles(self):
        """ Tests if sort_angle() function returns the passed points in the right order with 
            respect to polar angles 
        """

        nb_points = 5
        points = np.array([[1, 2], [1, 1], [2, 1], [3, 7], [7, 2]])      # example of points

        sorted_points = convex_hull.sort_angle(points)                   # sorted points 
        right_sorted_points = np.array([[2, 1], [7, 2], [3, 7], [1, 2], [1, 1]])

        self.assertTrue((sorted_points == right_sorted_points).all())


    def test_right_turn_true(self):
        """ Tests if 3 points form a right turn angle 
        """
        point1  = np.array([1, 1])
        point2  = np.array([2, 2])
        point3  = np.array([3, 1])

        right_angle1 = convex_hull.right_turn(point1, point2, point3)   # first right turn angle (boolean)
        right_angle2 = convex_hull.right_turn(point1, point3, point2)   # second right turn angle (boolean)

        self.assertTrue(right_angle1 and not right_angle2)

    
    def test_conv_full(self):
        """ Tests if the right convex hul of an example set of points is retuned
            by the function convex_hull()
        """

        points = np.array([[1, 4], [2, 1], [3, 2], [3, 3], [3, 5], [4, 2], [5, 1], [5, 3]])  # example of points 
        
        cv_hull = convex_hull.convex_hull(points)                       # convex hull returned by the function 

        right_conv_hull = np.array([[2, 1], [5, 1], [5, 3], [3, 5], [1, 4], [2, 1] ])        # right convex hull
        self.assertTrue((right_conv_hull == cv_hull).all())
    

if __name__ == "__main__":
    unittest.main()

