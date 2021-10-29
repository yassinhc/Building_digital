

import unittest

import sys
sys.path.append('..')


import src.Wall as Wall
import src.coordinate as Coordinate
import src.Wall as Wall
import src.Room as Room
import src.patio as Patio
import src.coridor as Coridor
import src.SubArea as SubArea

class Test_SubArea(unittest.TestCase):
    
    
    def setUp(self):
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(10,0)
        c3 = Coordinate.Coordinate(10,10)
        c4 = Coordinate.Coordinate(0,10)
        w1 = Wall.Wall((c1,c2))
        w2 = Wall.Wall((c2,c3))
        w3 = Wall.Wall((c3,c4))
        w4 = Wall.Wall((c4,c1))
        self.room = Room.Room((w1,w2,w3,w4))
        
        c1 = Coordinate.Coordinate(0,0)
        c2 = Coordinate.Coordinate(5,0)
        c3 = Coordinate.Coordinate(6,2)
        c4 = Coordinate.Coordinate(1,2)
        w1 = Wall.Wall((c1,c2))
        w2 = Wall.Wall((c2,c3))
        w3 = Wall.Wall((c3,c4))
        w4 = Wall.Wall((c4,c1))
        self.patio = Patio.Patio((w1,w2,w3,w4))
        
        c1 = Coordinate.Coordinate(1,0)
        c2 = Coordinate.Coordinate(1,8)
        c3 = Coordinate.Coordinate(5,0)
        c4 = Coordinate.Coordinate(5,8)
        w1 = Wall.Wall((c1,c2))
        w2 = Wall.Wall((c3,c4))
        self.coridor = Coridor.Coridor((w1,w2))
        
        self.subArea = SubArea.SubArea([])
        
    def test_listAreaEmpty(self):
        self.assertEqual(self.subArea.getListArea(),[])
        self.assertEqual(self.subArea.getSurface(),0)
        
    def test_addArea(self):
        self.assertEqual(self.subArea.getListArea(),[])
        self.assertEqual(self.subArea.getSurface(),0)
        self.subArea.addArea(self.room)
        self.assertEqual(self.subArea.getListArea(),[self.room])
        self.assertEqual(self.subArea.getSurface(),self.room.getSurface())
        
    def test_addMultiArea(self):
        self.assertEqual(self.subArea.getListArea(),[])
        self.assertEqual(self.subArea.getSurface(),0)
        self.subArea.addArea(self.room)
        self.subArea.addArea(self.coridor)
        self.subArea.addArea(self.patio)
        self.assertEqual(self.subArea.getListArea(),[self.room,self.coridor,self.patio])
        self.assertEqual(self.subArea.getSurface(),self.room.getSurface()+self.patio.getSurface()+
                         self.coridor.getSurface())
        
    def test_addArea_Fail(self):
        self.assertEqual(self.subArea.getListArea(),[])
        self.assertEqual(self.subArea.getSurface(),0)
        self.subArea.addArea(self.room)
        self.assertEqual(self.subArea.getListArea(),[self.room])
        self.assertEqual(self.subArea.getSurface(),self.room.getSurface())
        self.subArea.addArea(self.room)
        self.assertEqual(self.subArea.getListArea(),[self.room])
        self.assertEqual(self.subArea.getSurface(),self.room.getSurface())
        

        
"""        
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
        c33 = Coordinate.Coordinate(1,0)
        c44 = Coordinate.Coordinate(5,0)
        window1 = Window.Window((c3,c4))
        self.assertEqual(self.element.getListWindow(),[window])
    
  """      
if __name__ == '__main__':
    unittest.main()