

import numpy as np

import sys
sys.path.append('..')

from src import coordinate

import unittest



class Test_Building(unittest.TestCase):
    
    def test_getLenght(self):
        coordinate1 = coordinate.Coordinate(0,1)
        coordinate2 = coordinate.Coordinate(0,0)
        nb = coordinate1.getLength(coordinate2)
        self.assertEqual(nb,1)
    
    def test_getx_gety(self):
        coordinate2 = coordinate.Coordinate(1,-2)
        self.assertTrue(coordinate2.getx()==1 and coordinate2.gety()==(-2))
                
    def test_getVector(self):
        coordinate1 = coordinate.Coordinate(1,1)
        coordinate2 = coordinate.Coordinate(3,0)
        vect = coordinate1.getVector(coordinate2)
        self.assertEqual(vect.all(),np.array([2,-1]).all())

    def test_isAfter(self):
        coordinate1 = coordinate.Coordinate(1,0)
        coordinate2 = coordinate.Coordinate(3,0)
        self.assertTrue(coordinate1.isAfter(coordinate2))
        
    def test_onTheline(self):
        coordinate1 = coordinate.Coordinate(1,0)
        coordinate2 = coordinate.Coordinate(3,0)
        coo = coordinate.Coordinate(2,0)
        self.assertTrue(coordinate1.onTheLine(coordinate2,coo))

if __name__ == '__main__':
    unittest.main()