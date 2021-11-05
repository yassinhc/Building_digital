

import unittest

import sys
sys.path.append('..')


import src.Wall as Wall
import src.coordinate as Coordinate
import src.window as Window

from test.elementTest import ElementTest


class Test_Wall(ElementTest,unittest.TestCase):
    
    
    def createElement(self):        
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(10,0)        
        element = Wall.Wall((c1,c2))
        return element
        
    
    def test_length(self):
        length = self.element.getLength()
        self.assertEqual(length, 10)
        
    def test_listWindowDoorEmpty(self):
        self.assertEqual(self.element.getListDoor(),[])
        self.assertEqual(self.element.getListWindow(),[])
        
    def test_addWindow(self):
        c3 = Coordinate.Coordinate(2,0)
        c4 = Coordinate.Coordinate(4,0)
        window = Window.Window((c3,c4))
        self.assertEqual(self.element.getListWindow(),[])
        self.element.addWindow(window)
        self.assertEqual(self.element.getListWindow(),[window])
        self.assertEqual(self.element.getListCanBeContain(),[[self.element.getCoordinates()[0],c3],[c4,self.element.getCoordinates()[1]]])
        
        
    def test_addWindowFail1(self):
        c3 = Coordinate.Coordinate(12,0)
        c4 = Coordinate.Coordinate(4,0)
        window = Window.Window((c3,c4))
        self.assertEqual(self.element.getListWindow(),[])
        self.element.addWindow(window)
        self.assertEqual(self.element.getListWindow(),[])
        self.assertEqual(self.element.getListCanBeContain(),[[self.element.getCoordinates()[0],self.element.getCoordinates()[1]]])
        
        
    def test_addWindowFail2(self):
        c3 = Coordinate.Coordinate(2,0)
        c4 = Coordinate.Coordinate(4,1)
        window = Window.Window((c3,c4))
        self.assertEqual(self.element.getListWindow(),[])
        self.element.addWindow(window)
        self.assertEqual(self.element.getListWindow(),[])
        
    def test_addWindowFail3(self):
        c3 = Coordinate.Coordinate(2,0)
        c4 = Coordinate.Coordinate(4,0)
        window = Window.Window((c3,c4))
        self.assertEqual(self.element.getListWindow(),[])
        self.element.addWindow(window)
        self.assertEqual(self.element.getListWindow(),[window])
        self.assertEqual(self.element.getListCanBeContain(),[[self.element.getCoordinates()[0],c3],[c4,self.element.getCoordinates()[1]]])
        window1 = Window.Window((c3,c4))
        self.element.addWindow(window1)
        self.assertEqual(self.element.getListWindow(),[window])
    
        
if __name__ == '__main__':
    unittest.main()