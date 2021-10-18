# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:36:21 2021

@author: user
"""


import numpy as np

import sys
sys.path.append('..')

from src import coordinate

import unittest



class Test_Building(unittest.TestCase):
    
    def test_coordinates_length(self):
        coordinate1 = coordinate.Coordinate(0,1)
        coordinate2 = coordinate.Coordinate(0,0)
        nb = coordinate1.getLength(coordinate2)
        self.assertEqual(nb,1)
    
    def test_coordinate_x_y(self):
        coordinate2 = coordinate.Coordinate(1,-2)
        self.assertTrue(coordinate2.getx()==1 and coordinate2.gety()==(-2))
                
    def test_vector(self):
        coordinate1 = coordinate.Coordinate(1,1)
        coordinate2 = coordinate.Coordinate(3,0)
        vect = coordinate1.getVector(coordinate2)
        self.assertEqual(vect.all(),np.array([2,-1]).all())

    def test_isAfter(self):
        coordinate1 = coordinate.Coordinate(1,0)
        coordinate2 = coordinate.Coordinate(3,0)
        self.assertTrue(coordinate1.isAfter(coordinate2))
        

if __name__ == '__main__':
    unittest.main()