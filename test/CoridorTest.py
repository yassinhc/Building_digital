

import unittest

import sys
sys.path.append('..')


import src.coridor as Corridor
import src.Wall as Wall
import src.coordinate as Coordinate
from areaTest import AreaTest


class Test_Coridor(AreaTest,unittest.TestCase):
    global List_Walls
    
    def createArea(self):    
        global List_Walls
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(10,0)
        c3 = Coordinate.Coordinate(10,5)
        c4 = Coordinate.Coordinate(0,5)
        w1 = Wall.Wall((c1,c2))
        w2 = Wall.Wall((c3,c4))
        List_Walls=(w1,w2)
        area = Corridor.Corridor((w1,w2))
        return area
        
    def test_getSurface(self):
        pass
    def test_surface_square(self):
        surface = self.area.getSurface()
        self.assertEqual(surface, 50)
        
    def test_surface_parallelogram(self):
        c1 = Coordinate.Coordinate(1,0)
        c2 = Coordinate.Coordinate(1,8)
        c3 = Coordinate.Coordinate(5,0)
        c4 = Coordinate.Coordinate(5,8)
        w1 = Wall.Wall((c1,c2))
        w2 = Wall.Wall((c3,c4))
        area = Corridor.Corridor((w1,w2))
        surface = area.getSurface()
        self.assertEqual(surface,32)
    def test_getListWalls(self):
        self.assertEqual(self.area.getListWalls(),List_Walls)
        
        
if __name__ == '__main__':
    unittest.main()