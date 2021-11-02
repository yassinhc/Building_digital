

import unittest

import sys
sys.path.append('..')


import src.Room as Room
import src.Wall as Wall
import src.door as door
import src.window as window
import src.coordinate as Coordinate
import src.Area as Area
from areaTest import AreaTest


class Test_Room(AreaTest,unittest.TestCase):
    
    
    def createArea(self):        
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(10,0)
        c3 = Coordinate.Coordinate(10,10)
        c4 = Coordinate.Coordinate(0,10)
        w1 = Wall.Wall((c1,c2))
        w2 = Wall.Wall((c2,c3))
        w3 = Wall.Wall((c3,c4))
        w4 = Wall.Wall((c4,c1))
        area = Room.Room((w1,w2,w3,w4))
        
        return area
        
    def test_Coordinate(self):
        elements = self.area.getListElement()        
        self.assertTrue(len(elements)==4)
    
    
    def getSurface(self):
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

 
    def getListElement(self):
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(10,0)        
        c3 = Coordinate.Coordinate(5,0)
        c4 = Coordinate.Coordinate(0,5)
        c5 = Coordinate.Coordinate(1,2)
        c6 = Coordinate.Coordinate(-3,-1)        
        element_door = door.Door((c1,c2))
        element_wall = Wall.Wall((c3,c4))
        element_window = window.Window((c5,c6)) 
        List_Element= [element_door,element_wall,element_window]
        area= Area(List_Element)
        self.assertEqual(area.getListElement(),List_Element)
      
if __name__ == '__main__':
    unittest.main()