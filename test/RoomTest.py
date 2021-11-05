

import unittest

import sys
sys.path.append('..')


import src.Room as Room
import src.Wall as Wall

import src.coordinate as Coordinate
from test.areaTest import AreaTest


class Test_Room(AreaTest,unittest.TestCase):
    
    global List_Walls
    def createArea(self):  
        global List_Walls
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(10,0)
        c3 = Coordinate.Coordinate(10,10)
        c4 = Coordinate.Coordinate(0,10)
        w1 = Wall.Wall((c1,c2))
        w2 = Wall.Wall((c2,c3))
        w3 = Wall.Wall((c3,c4))
        w4 = Wall.Wall((c4,c1))
        List_Walls = (w1,w2,w3,w4)
        area = Room.Room((w1,w2,w3,w4))
        
        return area
        
    def test_Coordinate(self):
        elements = self.area.getListWalls()        
        self.assertTrue(len(elements)==4)
    
    
    def test_getSurface(self):
        pass
    def test_surface_square(self):
        surface = self.area.getSurface()
        self.assertEqual(surface, 100)
    def test_surface_rectangle(self):
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(10,0)
        c3 = Coordinate.Coordinate(10,5)
        c4 = Coordinate.Coordinate(0,5)
        w1 = Wall.Wall((c1,c2))
        w2 = Wall.Wall((c2,c3))
        w3 = Wall.Wall((c3,c4))
        w4 = Wall.Wall((c4,c1))
        area = Room.Room((w1,w2,w3,w4))
        surface = area.getSurface()
        self.assertEqual(surface,50)

 
    def test_getListWalls(self):
        self.assertEqual(self.area.getListWalls(),List_Walls)
  
if __name__ == '__main__':
    unittest.main()