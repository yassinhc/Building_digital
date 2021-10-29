# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:36:21 2021

@author: user
"""
import os



import sys
sys.path.append('..')

from src import coordinate

import unittest

print(os.getcwd())


class Test_Building(unittest.TestCase):
    def test_coordinates_length(self):
        coordinate1 = coordinate.Coordinate(0,1)
        coordinate2 = coordinate.Coordinate(0,0)
        print(coordinate1.getx())
        nb = coordinate1.getLength(coordinate2)
        self.assertEqual(nb,1)
    
    def test_coordinate_x_y(self):
        coordinate2 = coordinate.Coordinate(1,-2)
        self.assertTrue(coordinate2.getx()==1 and coordinate2.gety()==(-2))
                
 

if __name__ == '__main__':
    unittest.main()